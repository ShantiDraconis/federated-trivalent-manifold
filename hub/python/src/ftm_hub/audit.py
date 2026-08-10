from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json


STATUSES = frozenset({
    "PROVED", "FINITE_CERTIFICATE", "CONDITIONAL", "EQUIVALENT",
    "CONJECTURAL", "REFUTED", "OPEN",
})


class AuditError(ValueError):
    pass


@dataclass(frozen=True)
class Node:
    id: str
    problem: str
    title: str
    status: str
    depends_on: tuple[str, ...]
    evidence: tuple[str, ...]


class ResearchTree:
    def __init__(self, nodes: tuple[Node, ...]):
        self.nodes = nodes
        self.by_id = {node.id: node for node in nodes}
        self._validate()

    @classmethod
    def from_path(cls, path: str | Path) -> "ResearchTree":
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        nodes = tuple(Node(
            id=item["id"], problem=item["problem"], title=item["title"],
            status=item["status"], depends_on=tuple(item["dependsOn"]),
            evidence=tuple(item["evidence"]),
        ) for item in data["nodes"])
        return cls(nodes)

    def _validate(self) -> None:
        if len(self.by_id) != len(self.nodes):
            raise AuditError("node identifiers must be unique")
        for node in self.nodes:
            if node.status not in STATUSES:
                raise AuditError(f"invalid status for {node.id}: {node.status}")
            if node.id in node.depends_on:
                raise AuditError(f"self dependency at {node.id}")
            missing = set(node.depends_on) - self.by_id.keys()
            if missing:
                raise AuditError(f"missing dependencies for {node.id}: {sorted(missing)}")
        self._assert_acyclic()

    def _assert_acyclic(self) -> None:
        temporary: set[str] = set()
        permanent: set[str] = set()

        def visit(node_id: str) -> None:
            if node_id in permanent:
                return
            if node_id in temporary:
                raise AuditError(f"dependency cycle at {node_id}")
            temporary.add(node_id)
            for dependency in self.by_id[node_id].depends_on:
                visit(dependency)
            temporary.remove(node_id)
            permanent.add(node_id)

        for node in self.nodes:
            visit(node.id)

    def promotable_to_proved(self, node_id: str) -> bool:
        node = self.by_id[node_id]
        if node.status in {"REFUTED", "OPEN", "CONJECTURAL", "EQUIVALENT", "FINITE_CERTIFICATE"}:
            return False
        return all(self.by_id[dependency].status == "PROVED" for dependency in node.depends_on)

    def summary(self) -> dict[str, int]:
        result = {status: 0 for status in sorted(STATUSES)}
        for node in self.nodes:
            result[node.status] += 1
        return result

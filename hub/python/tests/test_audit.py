from pathlib import Path
import json

import pytest

from ftm_hub.audit import AuditError, ResearchTree


ROOT = Path(__file__).resolve().parents[2]


def test_repository_tree_is_valid():
    tree = ResearchTree.from_path(ROOT / "data" / "research-tree.json")
    assert len(tree.nodes) == 14
    assert tree.summary()["OPEN"] == 6


def test_open_and_finite_nodes_are_not_promotable():
    tree = ResearchTree.from_path(ROOT / "data" / "research-tree.json")
    assert not tree.promotable_to_proved("RH-C10")
    assert not tree.promotable_to_proved("PC-TEST")


def test_cycle_is_rejected(tmp_path):
    data = {"nodes": [
        {"id":"A","problem":"x","title":"a","status":"OPEN","dependsOn":["B"],"evidence":[]},
        {"id":"B","problem":"x","title":"b","status":"OPEN","dependsOn":["A"],"evidence":[]},
    ]}
    path = tmp_path / "tree.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    with pytest.raises(AuditError, match="cycle"):
        ResearchTree.from_path(path)

"""HKDF domain separation without logging key material."""

from dataclasses import dataclass


@dataclass(frozen=True)
class KeyContexts:
    logs: bytes = b"ftm/v1/log-encryption"
    transport: bytes = b"ftm/v1/transport-encryption"

    def validate(self) -> None:
        if not self.logs or not self.transport or self.logs == self.transport:
            raise ValueError("HKDF contexts must be non-empty and distinct")


def derive_keys(
    master: bytes, salt: bytes, contexts: KeyContexts = KeyContexts()
) -> tuple[bytes, bytes]:
    if len(master) < 32 or len(salt) < 16:
        raise ValueError("master and salt are too short")
    contexts.validate()
    try:
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.kdf.hkdf import HKDF
    except ImportError as exc:
        raise RuntimeError("install the 'crypto' extra; no insecure fallback is provided") from exc

    def one(info: bytes) -> bytes:
        return HKDF(algorithm=hashes.SHA256(), length=32, salt=salt, info=info).derive(master)

    return one(contexts.logs), one(contexts.transport)

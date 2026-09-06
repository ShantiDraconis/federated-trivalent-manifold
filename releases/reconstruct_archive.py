from hashlib import sha256
from pathlib import Path

EXPECTED = "EB8C778D559413CD871BEB39D32A537C2A5C04D52A54CC0F7127E584F2503B17"
ROOT = Path(__file__).resolve().parent
TARGET = ROOT / "pacote-completo-auditoria-rh.zip"

parts = sorted((ROOT / "chunks").glob("pacote-completo-auditoria-rh.zip.part*"))
if not parts:
    raise SystemExit("archive parts not found")

with TARGET.open("wb") as output:
    for part in parts:
        output.write(part.read_bytes())

actual = sha256(TARGET.read_bytes()).hexdigest().upper()
if actual != EXPECTED:
    TARGET.unlink(missing_ok=True)
    raise SystemExit(f"checksum mismatch: {actual}")

print(f"reconstructed {TARGET.name}: {actual}")

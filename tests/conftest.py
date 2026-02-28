from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"

# dodajemo src modul u sys.path kako bi ga prepoznao 'pytest' poziv iz korijenskog direktorijuma
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
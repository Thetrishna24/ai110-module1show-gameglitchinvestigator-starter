import sys
from pathlib import Path

# Ensure the project root (one level up from tests/) is on sys.path so tests
# can import modules like logic_utils.py located there.
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

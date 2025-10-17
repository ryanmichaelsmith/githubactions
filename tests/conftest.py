import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Ensure the repository root is on sys.path when pytest is invoked as a script.
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


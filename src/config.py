from pathlib import Path

# -------------------------------------------------------------------------------------
# Diretórios de uso geral
# -------------------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / 'data'
DATA_CLEAN = DATA_DIR / 'clean' / 'csv'
DATA_MERGED = DATA_DIR / 'merged'
DATA_RAW = DATA_DIR / 'raw' / 'csv'
DATA_TRANSF = DATA_DIR / 'transformed' / 'csv'
DATA_NORM = DATA_DIR / 'normalized' / 'csv'
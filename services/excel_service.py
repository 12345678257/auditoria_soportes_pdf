import pandas as pd
from pathlib import Path

def export_excel(path: Path, rows):
    df = pd.DataFrame(rows)
    df.to_excel(path, index=False)

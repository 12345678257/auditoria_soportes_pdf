import shutil
from pathlib import Path

def copy_preserve_structure(src_file: Path, origin_root: Path, dest_root: Path):
    relative_path = src_file.relative_to(origin_root)
    destination = dest_root / relative_path
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src_file, destination)

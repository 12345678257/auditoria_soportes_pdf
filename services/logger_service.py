import logging
from pathlib import Path

def setup_logger(base_path: Path):
    log_dir = base_path / "logs"
    log_dir.mkdir(exist_ok=True)

    logger = logging.getLogger("audit_engine")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.FileHandler(log_dir / "audit.log", encoding="utf-8")
        formatter = logging.Formatter(
            '{"time":"%(asctime)s","level":"%(levelname)s","msg":"%(message)s"}'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

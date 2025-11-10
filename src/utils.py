import logging
import math
from datetime import datetime, timezone

def setup_logger(name: str) -> logging.Logger:
    logging.basicConfig(
        level="INFO",
        format="%(asctime)s | %(levelname)s | %(message)s",
    )
    return logging.getLogger(name)

def utc_now():
    return datetime.now(timezone.utc)

def calculate_zscore(values):
    if len(values) < 2:
        return None
    mean = sum(values[:-1]) / (len(values) - 1)
    variance = sum((x - mean) ** 2 for x in values[:-1]) / max(1, len(values) - 2)
    stddev = math.sqrt(variance)
    latest = values[-1]
    if stddev == 0:
        return 0
    return (latest - mean) / stddev

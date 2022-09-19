import os
import sys
import logging

logging_str = "[%(asctime)s] %(name)s:%(levelname)s:: %(module)s:%(filename)s:%(funcName)s() => %(message)s"
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[  # as we want to print on terminal as well as in file
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout),
    ],
)

logger = logging.getLogger("deepclassifierLogger")

import os
from pathlib import Path
import logging

logging.basicConfig(
    format="[%(asctime)s] %(levelname)s: %(message)s",
    level=logging.INFO,
)
package_name = "DeepClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{package_name}/__init.py",
    f"src/{package_name}/components/__init.py",
    f"src/{package_name}/entity/__init.py",
    f"src/{package_name}/constants/__init.py",
    f"src/{package_name}/pipeline/__init.py",
    f"src/{package_name}/config/__init.py",
    f"src/{package_name}/utils/__init.py",
    # exception, logger, artifact can be added in src/package_name
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "configs/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "research/trials.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir, filename = os.path.split(filepath)
    if file_dir:
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Created Directory: {file_dir} for file: {filename}")
    if not os.path.exists(filepath) or (os.path.getsize(filepath) == 0):
        # checking file or else it will overwrite
        # 2nd condition to avoid already exists if files are empty
        with open(filepath, "w") as f:
            pass
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")

import os
from urllib import request
from zipfile import ZipFile
from deepclassifier import logger
from deepclassifier.entity import DataIngestionConfig
from deepclassifier.utils import get_size
from tqdm import tqdm  # ? Progress Bar
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig) -> None:
        self.config = config

    def download_file(self):
        logger.info("Trying to download file...")
        if not os.path.exists(self.config.local_data_file):
            logger.info("Download started...")
            filename, headers = request.urlretrieve(url=self.config.source_URL, filename=self.config.local_data_file)
            logger.info(f"{filename} downloaded. Headers:\n{headers}")
        else:
            size = get_size(Path(self.config.local_data_file))
            logger.info(f"File already exists of size: {size}")

    def _get_updated_list_of_files(self, list_of_files: list):
        return [f for f in list_of_files if f.endswith("jpg") and ("Cat" in f or "Dog" in f)]

    def _preprocess(self, zf: ZipFile, f: str, working_dir: str):
        target_filepath = os.path.join(working_dir, f)
        if not os.path.exists(target_filepath):
            zf.extract(f, working_dir)

        if os.path.getsize(target_filepath) == 0:
            os.remove(target_filepath)
            logger.info(f"File Remove: {target_filepath}")

    def unzip_clean(self):
        logger.info("Unzipping and Filtering Files")
        with ZipFile(file=self.config.local_data_file, mode="r") as zf:
            list_of_files = zf.namelist()
            updated_list_of_files = self._get_updated_list_of_files(list_of_files)
            for f in tqdm(updated_list_of_files):
                self._preprocess(zf, f, self.config.unzip_dir)
        logger.info("Unzipping Done")

from deepclassifier.components import DataIngestion
from deepclassifier.config import ConfigurationManager
from deepclassifier import logger

STAGE_NAME = " Data Ingestion Stage"


def main():
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.unzip_clean()


if __name__ == "__main__":
    try:
        logger.info(f" STAGE: {STAGE_NAME} STARTED ".center(100, "="))
        main()
        logger.info(f" STAGE: {STAGE_NAME} COMPLETED ".center(100, "="))
    except Exception as e:
        logger.exception(e)
        raise e

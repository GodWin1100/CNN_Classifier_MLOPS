from deepclassifier.components import DataIngestion
from deepclassifier.config import ConfigurationManager

try:
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.unzip_clean()
except Exception as e:
    raise e

print("hi")

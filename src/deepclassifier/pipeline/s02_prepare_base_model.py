from deepclassifier.config import ConfigurationManager
from deepclassifier.components import PrepareBaseModel
from deepclassifier import logger

STAGE_NAME = "Prepare Base Model"


def main():
    config = ConfigurationManager()
    prepare_base_model_config = config.get_prepare_base_model_config()
    prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
    prepare_base_model.get_base_model()
    prepare_base_model.update_base_model()


if __name__ == "__main__":
    try:
        logger.info(f" STAGE: {STAGE_NAME} STARTED ".center(100, "="))
        main()
        logger.info(f" STAGE: {STAGE_NAME} COMPLETED ".center(100, "="))
    except Exception as e:
        logger.exception(e)
        raise e

from deepclassifier.config import ConfigurationManager
from deepclassifier.components import Evaluation
from deepclassifier import logger

STAGE_NAME = "Evaluation"


def main():
    config = ConfigurationManager()
    evaluation_config = config.get_validation_config()
    evaluation = Evaluation(evaluation_config)
    evaluation.evaluation()
    evaluation.save_score()


if __name__ == "__main__":
    try:
        logger.info(f" STAGE: {STAGE_NAME} STARTED ".center(100, "="))
        main()
        logger.info(f" STAGE: {STAGE_NAME} COMPLETED ".center(100, "="))
    except Exception as e:
        logger.exception(e)
        raise e



from cnnClassifier.components.model_evaluation_mlflow import Evaluation
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier import logger


STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        evaluation_config = config.get_evaluation_config()
        evaluation = Evaluation(config=evaluation_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()
         
            
            
if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
    except Exception as e:
        logger.error(f"Error occurred in stage {STAGE_NAME}: {e}")
        raise e
    
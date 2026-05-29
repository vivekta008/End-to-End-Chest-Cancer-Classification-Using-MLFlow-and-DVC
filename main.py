from cnnClassifier import logger
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier.pipeline.stage_01 import DataIngestiontrainingPipeline
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier.pipeline.stage_01 import DataIngestiontrainingPipeline
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.constants import *
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from cnnClassifier.pipeline.stage_03_model_trainer import ModelTrainerPipeline
from cnnClassifier.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline
import dagshub



STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestiontrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")

except Exception as e:
    logger.error(f"Error occurred in stage {STAGE_NAME}: {e}")
    raise e


STAGE_NAME = "Prepare Base Model Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj =PrepareBaseModelPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")

except Exception as e:
    logger.error(f"Error occurred in stage {STAGE_NAME}: {e}")
    raise e


STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = ModelTrainerPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")

except Exception as e:
    logger.error(f"Error occurred in stage {STAGE_NAME}: {e}")
    raise e

STAGE_NAME = "Model Evaluation Stage"
try:
    
    dagshub.init(repo_owner='tavivek256', repo_name='End-to-End-Chest-Cancer-Classification-Using-MLFlow-and-DVC', mlflow=True)
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")

except Exception as e:
    logger.error(f"Error occurred in stage {STAGE_NAME}: {e}")
    raise e
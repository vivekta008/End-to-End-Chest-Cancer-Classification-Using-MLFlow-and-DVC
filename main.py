from cnnClassifier import logger
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier.pipeline.stage_01 import DataIngestiontrainingPipeline
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.constants import *


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestiontrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.error(f"Error occurred in stage {STAGE_NAME}: {e}")
    raise e
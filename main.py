#from src.E2E_WQ_ML_Project.logging import logger
#from src.E2E_WQ_ML_Project import logger
#logger.info(" this is our custom log in project constructer 2nd way")

from E2E_WQ_ML_Project import logger
from E2E_WQ_ML_Project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
#from E2E_WQ_ML_Project.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
#from E2E_WQ_ML_Project.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
#from E2E_WQ_ML_Project.stage_04_model_trainer import ModelTrainerTrainingPipeline
#from E2E_WQ_ML_Project.stage_05_model_evaluation import ModelEvaluationTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
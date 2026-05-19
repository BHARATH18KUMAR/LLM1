from LLM_text_detection.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

try:
    obj = DataIngestionTrainingPipeline()
    obj.main()

except Exception as e:
    raise e
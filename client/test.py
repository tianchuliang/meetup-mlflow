import mlflow
mlflow.set_tracking_uri("http://35.223.142.40:8888/")

with mlflow.start_run():
    mlflow.log_param("test", 1)
    
    mlflow.log_artifact("test_artifact.txt")
    
    mlflow.log_param("test2",2)
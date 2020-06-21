# Exmaple 1: Run server locally with all defaults
# mlflow server
# Exmaple 2: Run server remotely on cloud
# mlflow server --backend-store-uri /home/aliang/mlflow_runs --default-artifact-root /home/aliang/mlflow_artifacts --host 0.0.0.0:8888
# Example 3: Run Server remotely And store models on cloud storage
mlflow server --backend-store-uri /home/aliang/mlflow_runs --default-artifact-root /home/aliang/mlflow_artifacts --host 0.0.0.0:8888
# Exmaple 1: Run server locally with all defaults
# mlflow server --host 0.0.0.0:8888

# Exmaple 2: Run server remotely on cloud
# mlflow server --default-artifact-root ./artifacts --host 0.0.0.0:8888

# Example 3: Run Server remotely And store models on cloud storage
mlflow server --default-artifact-root gs://mldev_bucket_0/mlflow_artifacts --host 0.0.0.0:8888
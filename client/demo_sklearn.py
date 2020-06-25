# Credit: https://www.mlflow.org/docs/latest/python_api/mlflow.sklearn.html
import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn import tree
mlflow.set_tracking_uri("http://35.223.142.40:8888/")

def main():
    iris = load_iris()
    sk_model = tree.DecisionTreeClassifier()
    sk_model = sk_model.fit(iris.data, iris.target)
    # set the artifact_path to location where experiment artifacts will be saved

    #log model params
    mlflow.log_param("criterion", sk_model.criterion)
    mlflow.log_param("splitter", sk_model.splitter)

    # log model
    mlflow.sklearn.log_model(sk_model, "sk_models")

if __name__ == "__main__":
    try:
        with mlflow.start_run():
            main()
    except:
        mlflow.end_run()
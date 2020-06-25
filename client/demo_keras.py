# Credit: https://www.mlflow.org/docs/latest/python_api/mlflow.keras.html
import mlflow
import mlflow.sklearn
from sklearn.datasets import load_diabetes
mlflow.set_tracking_uri("http://35.223.142.40:8888/")
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import os

def main():
    X, Y = load_diabetes(return_X_y = True)

    # Build, compile, and train your model
    keras_model = keras.Sequential([
                                    layers.Dense(10, activation='relu'),
                                    layers.Dense(6, activation='relu'),
                                    layers.Dense(4, activation='relu'),
                                    layers.Dense(1),
                                ])
    
    x_train, x_val = X[:300], X[300:]
    y_train, y_val = Y[:300], Y[300:]
    keras_model.compile(optimizer="rmsprop", loss="mse", metrics=["accuracy"])
    results = keras_model.fit(
        x_train, y_train, epochs=200, batch_size = 24, validation_data=(x_val, y_val))
    
    for i in range(200):
        mlflow.log_metric("loss", results.history['loss'][i])
        mlflow.log_metric("val_loss", results.history['val_loss'][i])
    
    model_json = keras_model.to_json()
    with open("model.json", "w") as json_file:
        json_file.write(model_json)
    # serialize weights to HDF5
    keras_model.save_weights("model.h5")
    mlflow.log_artifact("model.json")
    mlflow.log_artifact("model.h5")
    os.remove("model.json")
    os.remove("model.h5")
    

if __name__ == "__main__":


    # Log metrics and log the model
    try:
        with mlflow.start_run():
            main()         
    except:
        mlflow.end_run()
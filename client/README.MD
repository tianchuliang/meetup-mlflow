Code for demonstration of setting up client side modeling experiments.
In this folder, we have two demo files to show case useage of MLflow. 
+ demo_keras.py shows a typical neural network training process, where we are logging loss and val_loss to remote MLFlow server
+ demo_sklearn.py shows a typical sklearn workflow, where we are tracking parameters and metrics onto MLflow server.

In both demo files, we are saving the artifacts to MLflow as well; these artifacts are directed (configured in server) to a Google Cloud Bucket. 
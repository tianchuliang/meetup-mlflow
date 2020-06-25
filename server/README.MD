Code to run a remote MLFlow tracking server

# Run Server on Cloud VM
+ Set up a GCP VM
+ Make sure Python, Anaconda, MLfow are installed on this GCP VM
+ Make sure to configure this VM to allow https traffic, in order to serve MLFlow tracking website, as well as take input REST requests.
+ See start_mlflow.sh for commands on running up the server
# Run Server on Cloud VM with Cloud storage bucket
+ Set up a GCP Cloud Storage Bucket
+ Since VM and Bucket are both on GCP, the communication between the two should be seamless (only need to make sure VM has "CLoud API Access Scopes" set to full access to all APIs.)
+ Also have to set GCP cloud bucket storage to allow external user to read/write objects
+ If you want to track a ML process running locally on a laptop, make sure your local laptop/dev environment has proper credentials to your GCP VM as well as cloud storage bucket.
# References
https://www.mlflow.org/docs/latest/tracking.html#google-cloud-storage
https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/docs/installing.md
https://cloud.google.com/storage/docs/gcs-fuse#using
https://www.mlflow.org/docs/latest/tracking.html#google-cloud-storage
https://googleapis.dev/python/google-api-core/latest/auth.html
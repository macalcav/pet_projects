# @hidden_cell
# The following code accesses a file in your IBM Cloud Object Storage. It includes your credentials.
# Remove those credentials before you share the notebook.

#########################
# load images from bucket
#########################
import os, types
import pandas as pd
from botocore.client import Config
import ibm_boto3
from ibm_botocore.client import Config, ClientError 
#https://www.programmersought.com/article/34363925958/

def __iter__(self): return 0

IBM_API_KEY=<IBM_API_KEY>
BUCKET_NAME=<BUCKET_NAME>

if os.environ.get('RUNTIME_ENV_LOCATION_TYPE') == 'external':
  ENDPOINT_URL = 'https://s3.us.cloud-object-storage.appdomain.cloud'
else:
  ENDPOINT_URL = 'https://s3.private.us.cloud-object-storage.appdomain.cloud'

COS_CLIENT = ibm_boto3.client(
  service_name='s3',
  ibm_api_key_id=IBM_API_KEY,
  ibm_auth_endpoint="https://iam.cloud.ibm.com/oidc/token",
  config=Config(signature_version='oauth'),
  endpoint_url=ENDPOINT_URL)

image_name='image.jpg'
response = COS_CLIENT.get_object(Bucket=BUCKET_NAME, Key=image_name)
file_contents = response["Body"].read()

f = open('image.jpg', 'wb')
f.write(file_contents)
f.close()

# Output images to html using python - Stack Overflow
# https://stackoverflow.com/questions/7389567/output-images-to-html-using-python
import base64
localImage_data_uri = base64.b64encode(open('image.jpg', 'rb').read()).decode('utf-8')

# Usage:
display(HTML(<img src="data:image/png;base64,{0}"'.format(localImage_data_uri) alt="LONGEST RUNNING DEFECT IN RHM HISTORY" style="width:170px;height:170px;margin-left:15px;float:left;">))

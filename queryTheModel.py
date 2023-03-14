import boto3
import json

# Create a Boto3 SageMaker client
sm_client = boto3.client('sagemaker-runtime')

# Set up the input data for the prediction request
input_data = {"data": "this is stuff that needs to be summarised. I want to see how good you are at summarization. Can you summarize please."}

# Set up the endpoint and model names
endpoint_name = 'pegasusEndpoint'
model_name = 'huggingface-pytorch-training-2023-03-13-16-06-29-579'

# Make the prediction request
response = sm_client.invoke_endpoint(EndpointName=endpoint_name, 
                                     Body=json.dumps(input_data),
                                     ContentType='application/json',
                                     TargetModel=model_name)

# Parse the prediction result
prediction_result = json.loads(response['Body'].read().decode())

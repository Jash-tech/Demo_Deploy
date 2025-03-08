import boto3

s3 = boto3.client("s3")



bucket_name = "streamfirstbuckets" 
model_file = "classifier.pkl"

client.upload_file(model_file, bucket_name, f"models/{model_file}")

print("Model uploaded successfully to S3!")

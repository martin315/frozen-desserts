"""An AWS Python Pulumi program"""

import pulumi
#from pulumi_aws import s3
import pulumi_aws as aws

# Create an AWS resource (S3 Bucket)
bucket = aws.s3.Bucket('my-bucket')

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)

# Override the AWS region for the deployment.
aws.config.region = 'us-west-2'
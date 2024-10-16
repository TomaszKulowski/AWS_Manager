import boto3

from botocore.exceptions import ClientError


class AWSManager:
    """
    A context manager for interacting with AWS S3 using the Boto3 library.

    Note:
        Before using this method, ensure that the AWS client has been created
        by either entering the context manager (using 'with AWSManager(...) as aws_manager:')
        or by explicitly calling 'create_client()' on the instance.

    Attributes:
        access_key_id (str): The AWS access key ID.
        access_key (str): The AWS secret access key.
        bucket_name (str): The name of the S3 bucket.
        prefix (str, optional): The prefix for filtering objects in the bucket.
        region (str): The AWS region where the S3 bucket is located.
    """
    def __init__(
            self,
            access_key_id: str,
            access_key: str,
            bucket_name: str,
            prefix: str = None,
            region: str = 'us-east-1',
    ):
        """
        Initializes the AWSManager instance.

        Args:
            access_key_id (str): The AWS access key ID.
            access_key (str): The AWS secret access key.
            bucket_name (str): The name of the S3 bucket.
            prefix (str, optional): The prefix for filtering objects in the bucket. Default is None.
            region (str): The AWS region where the S3 bucket is located. Default is 'us-east-1'.
        """
        self.access_key_id = access_key_id
        self.access_key = access_key
        self.bucket_name = bucket_name
        self.prefix = prefix
        self.region = region
        self.client = None

    def __enter__(self):
        """
        Initializes the AWS client when entering the context.
        """
        self.create_client()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Cleans up resources when exiting the context.
        """
        pass

    def create_client(self):
        """
        Creates a Boto3 S3 client using the provided AWS credentials and region.
        """
        session = boto3.Session(
            aws_access_key_id=self.access_key_id,
            aws_secret_access_key=self.access_key,
            region_name=self.region,
        )
        self.client = session.client('s3')

    def list_files(self):
        """
        Lists the files in the specified S3 bucket with the optional prefix.

        If files are found, their keys are printed. If no files are found,
        a message is printed indicating that no files were found.

        Raises:
            ClientError: If an error occurs while accessing the S3 service.
        """
        try:
            response = self.client.list_objects_v2(Bucket=self.bucket_name, Prefix=self.prefix)

            if 'Contents' in response:
                for content in response['Contents']:
                    print(content['Key'])

            else:
                print(f'No files found in the bucket "{self.bucket_name}" with prefix: "{self.prefix}".')

        except ClientError as error:
            print(error)

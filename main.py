from os import getenv

from dotenv import load_dotenv

from aws_manager import AWSManager


load_dotenv('.env')

ACCESS_KEY_ID = getenv('ACCESS_KEY_ID')
ACCESS_KEY = getenv('ACCESS_KEY')
BUCKET_NAME = 'developer-task'
PREFIX = 'TIE-rp'

EXAMPLE_FILE_PATH = '.env-example'
S3_FILE_PATH = 'TIE-rp/'
EXAMPLE_REGEX = '^[a-zA-Z]+$'


if __name__ == '__main__':
    with AWSManager(
        access_key_id=ACCESS_KEY_ID,
        access_key=ACCESS_KEY,
        bucket_name=BUCKET_NAME,
        prefix=PREFIX,
        region='eu-central-1',
    ) as aws_manager:
        aws_manager.list_files()
        aws_manager.upload_file(
            local_file_path=EXAMPLE_FILE_PATH,
            s3_file_path=S3_FILE_PATH,
        )
        aws_manager.list_files(regex_pattern=EXAMPLE_REGEX)


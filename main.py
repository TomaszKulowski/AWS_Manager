from os import getenv

from dotenv import load_dotenv

from aws_manager import AWSManager


load_dotenv('.env')

ACCESS_KEY_ID = getenv('ACCESS_KEY_ID')
ACCESS_KEY = getenv('ACCESS_KEY')
BUCKET_NAME = 'developer-task'
PREFIX = 'TIE-rp'


if __name__ == '__main__':
    with AWSManager(
        access_key_id=ACCESS_KEY_ID,
        access_key=ACCESS_KEY,
        bucket_name=BUCKET_NAME,
        prefix=PREFIX,
        region='eu-central-1',
    ) as aws_manager:
        aws_manager.list_files()

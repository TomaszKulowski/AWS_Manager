# AWS_Manager

`AWSManager` is a Python class that provides a convenient context manager for interacting with Amazon S3 using the Boto3 library. It allows you to list, upload, and delete files in an S3 bucket, with optional filtering using regular expressions.

## Features

- List files in a specified S3 bucket.
- Upload local files to an S3 bucket.
- Delete files from the S3 bucket based on a regex pattern.
- Supports AWS credentials management via environment variables.

## Requirements

- Python 3.x
- Boto3 library
- dotenv library (for managing environment variables)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/TomaszKulowski/AWS_Manager.git
   cd AWS_Manager
   ```

2. Install the requirements

   ```bash
   pip install -r requirements.txt
   ```

3. Create a .env file in the project root directory and add your AWS credentials:

   ```bash
   ACCESS_KEY_ID = your_access_key_id
   ACCESS_KEY = your_secret_access_key
   ```

## Usage
To run the example script and interact with your S3 bucket, run main.py script:

```bash
python main.py
```

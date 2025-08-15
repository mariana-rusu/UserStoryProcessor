import unittest
import boto3
from tests.integration.data import *
from lambda_function import lambda_handler
from datetime import datetime, timedelta
from tests.integration.Helper_Methods import HelperMethods


class TestPutMethod(unittest.TestCase):
    bucket_name = "user-stories-bucket-0001"
    s3_client = boto3.client("s3")

    def setUp(self):
        bucket_name = "user-stories-bucket-0001"
        self.s3_client = boto3.client("s3")
        files_to_delete = ["d4436e50-07e9-42f5-870f-657aa9116af2.json", "92256d43-ecc3-4e90-a49c-eb1d133714de.json"]
        for file in files_to_delete:
            self.s3_client.delete_object(Bucket=bucket_name, Key=file)

    def test_validate_datetime(self):
        file_name = "d4436e50-07e9-42f5-870f-657aa9116af2.json"
        min_modified_time = datetime.utcnow() - timedelta(days=1)
        lambda_handler(test_record_include_all_fields, None)

        try:
            response = self.s3_client.head_object(Bucket=self.bucket_name, Key=file_name)
            last_modified = response['LastModified']

            self.assertTrue(self, last_modified.timestamp() >= min_modified_time.timestamp())

        except self.s3_client.exceptions.ClientError as e:
            print(f"Error accessing S3 object: {e}")
            return e


    def test_with_all_fields_not_null(self):
        file_name = "d4436e50-07e9-42f5-870f-657aa9116af2.json"

        lambda_handler(test_record_include_all_fields, None)

        try:
            res = self.s3_client.get_object(Bucket=self.bucket_name, Key=file_name)
            object_content = res['Body'].read().decode('UTF-8')

            HelperMethods.validate_file_content(test_record_include_all_fields, object_content)

        except self.s3_client.exceptions.ClientError as e:
            print(f"Error accessing S3 object: {e}")
            return e

    def test_with_null_fields(self):
        file_name = "92256d43-ecc3-4e90-a49c-eb1d133714de.json"
        lambda_handler(test_record_missing_fields, None)

        try:
            response = self.s3_client.get_object(Bucket=self.bucket_name, Key=file_name)
            object_content = response['Body'].read().decode('UTF-8')

            HelperMethods.validate_file_content(test_record_missing_fields, object_content)

        except self.s3_client.exceptions.ClientError as e:
            print(f"Error accessing S3 object: {e}")
            return e
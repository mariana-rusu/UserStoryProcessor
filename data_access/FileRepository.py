import json
from business.IRepository import IRepository
import boto3


class FileRepository(IRepository):
    def __init__(self, s3=None):
        if s3:
            self.s3 = s3
        else:
            self.s3 = boto3.client('s3')

        self.bucket = 'user-stories-bucket-0001'

    def put_item(self, name, body):
        file = bytes(json.dumps(body).encode('UTF-8'))
        self.s3.put_object(Bucket=self.bucket, Key=name, Body=file)
        print('UserStory with Id: ' + body['user_story_id'] + ' saved into S3')
        print("Done Saving New Record in S3")
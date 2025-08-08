import unittest
from unittest.mock import Mock
from tests.unittest.data import file_body
from data_access.FileRepository import FileRepository


class TestPutItemMethod(unittest.TestCase):
    s3_client = Mock()
    file_repository = FileRepository(s3_client)

    def test_put_item_method(self):
        self.s3_client.put_object = Mock()

        self.file_repository.put_item(file_body['user_story_id'], file_body)

        self.s3_client.put_object.assert_called_once()

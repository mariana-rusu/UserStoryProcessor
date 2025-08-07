from application.UserStoryGenerator import UserStoryGenerator
from data_access.FileRepository import FileRepository

user_story_g = UserStoryGenerator()
file_repo = FileRepository()

def lambda_handler(event, context):
	print('------------------------')
	print(event)
	#1. Iterate over each record
	try:
		for record in event['Records']:
			#2. Handle event by type
			if record['eventName'] == 'INSERT':
				save_record_to_s3(record)
		print('------------------------')
		return "Success!"
	except Exception as e:
		print(e)
		print('------------------------')
		return "Error"


def save_record_to_s3(record):
	print("Saving New Record in S3")

	new_image = record['dynamodb']['NewImage']
	user_story = user_story_g.create_user_story(new_image['user_story_id']['S'], new_image)

	file_body = user_story.to_json()
	file_name = file_body['user_story_id'] + '.json'

	file_repo.put_item(file_name, file_body)


from business.UserStory import UserStory

class UserStoryGenerator:
    def __init__(self):
        pass

    def create_user_story(self, user_story_id: str, record: dict) -> UserStory:
        user_story = UserStory(user_story_id)

        if "summary" in record.keys():
            user_story.summary = record["summary"]['S']
        if "description" in record.keys():
            user_story.description = record["description"]['S']
        if "project_id" in record.keys():
            user_story.project_id = record["project_id"]['S']
        if "issue_type" in record.keys():
            user_story.issue_type = record["issue_type"]['S']
        if "assignee" in record.keys():
            user_story.assignee = record["assignee"]['S']
        if "labels" in record.keys():
            user_story.labels = record["labels"]['L']
        if "sprint" in record.keys():
            user_story.sprint = record["sprint"]['S']
        if "reporter" in record.keys():
            user_story.reporter = record["reporter"]['S']

        return user_story

class UserStory:
    def __init__(self, user_story_id: str):
        self.user_story_id = user_story_id
        self.summary = None
        self.description = None
        self.project_id = None
        self.issue_type = None
        self.assignee = None
        self.labels = None
        self.sprint = None
        self.reporter = None

    def to_json(self) -> dict:
        return self.__dict__
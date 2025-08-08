import json

class HelperMethods:
    @classmethod
    def validate_file_content(cls, record, file_content):
        new_image = record['Records'][0]['dynamodb']['NewImage']
        data = json.loads(file_content)

        if 'summary' not in new_image:
            assert data['summary'] is None
        else:
            assert new_image['summary']['S'] == data['summary']

        if 'description' not in new_image:
            assert data['description'] is None
        else:
            assert new_image['description']['S'] == data['description']

        if 'project_id' not in new_image:
            assert data['project_id'] is None
        else:
            assert new_image['project_id']['S'] == data['project_id']

        if 'issue_type' not in new_image:
            assert data['issue_type'] is None
        else:
            assert new_image['issue_type']['S'] == data['issue_type']

        if 'assignee' not in new_image:
            assert data['assignee'] is None
        else:
            assert new_image['assignee']['S'] == data['assignee']

        if 'labels' not in new_image:
            assert data['labels'] is None
        else:
            assert new_image['labels']['L'] == data['labels']

        if 'sprint' not in new_image:
            assert data['sprint'] is None
        else:
            assert new_image['sprint']['S'] == data['sprint']

        if 'reporter' not in new_image:
            assert data['reporter'] is None
        else:
            assert new_image['reporter']['S'] == data['reporter']



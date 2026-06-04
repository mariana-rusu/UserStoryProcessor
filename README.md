# User Stories Processor

An AWS Lambda function that listens to DynamoDB Streams and saves new user stories as JSON files to S3.

## Overview

When a new item is inserted into the DynamoDB table, a stream event triggers this Lambda. It maps the record to a `UserStory` domain object and uploads it as a JSON file to an S3 bucket.

## Architecture

```
lambda_function.py          ← Lambda handler / entry point
├── application/
│   └── UserStoryGenerator  ← Maps DynamoDB record format to domain object
├── business/
│   ├── UserStory           ← Domain model
│   └── IRepository         ← Abstract storage interface
└── data_access/
    └── FileRepository      ← S3 implementation via boto3
```

## How It Works

1. DynamoDB Streams triggers the Lambda on `INSERT` events
2. `UserStoryGenerator` maps the DynamoDB wire format to a `UserStory` object
3. `FileRepository` serializes it to JSON and uploads it to S3 as `<user_story_id>.json`

## User Story Fields

| Field           | Type   |
|----------------|--------|
| `user_story_id` | string |
| `summary`       | string |
| `description`   | string |
| `project_id`    | string |
| `issue_type`    | string |
| `assignee`      | string |
| `labels`        | list   |
| `sprint`        | string |
| `reporter`      | string |

## S3 Bucket

Files are stored in `user-stories-bucket-0001` with the key pattern `<user_story_id>.json`.

## Requirements

- Python 3.9+
- boto3
- AWS credentials with access to the target S3 bucket

## Installation

```bash
python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running Tests

**Unit tests** (no AWS credentials needed — S3 is mocked):
```bash
python3.9 -m unittest tests/unittest/test_put_item_method.py
```

**Integration tests** (requires real AWS credentials and the S3 bucket):
```bash
python3.9 -m unittest tests/integration/test_put_item_method.py
```

## CI/CD

GitLab CI pipeline with three stages:

| Stage            | Description                                      |
|-----------------|--------------------------------------------------|
| `build`          | Sets up Python 3.9 venv and installs dependencies |
| `test`           | Runs unit tests                                  |
| `build-artifact` | Packages Lambda deployment zip                   |

The deployment package (`my_deployment_package.zip`) includes all source code and pip dependencies, ready to upload to AWS Lambda.

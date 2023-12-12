import json


def main(event, context):
    print(json.dumps(event))
    response = {
        "statusCode": 200,
        "headers": {},
        "body": json.dumps({"message": "Hello World"}),
    }
    return response

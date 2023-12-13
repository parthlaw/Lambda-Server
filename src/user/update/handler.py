from schemas.response import Response, ResponseCodes
from utils.database import DB
from utils.get_secrets import get_secret
import json


def main(event, context):
    try:
        if "body" not in event:
            return Response(
                statusCode=ResponseCodes.BAD_REQUEST.value,
                body=json.dumps({"message": "Bad request"}),
                headers=json.dumps({}),
            )
        path_params = event.get('pathParameters', {})
        user_id = path_params.get('id')       
        print(json.dumps(event))
        creds = get_secret()
        db = DB(creds)
        resp = db.update_user(user_id,json.loads(event["body"]))
        return Response(statusCode=ResponseCodes.OK.value, body=json.dumps(resp), headers=json.dumps({}))
    except Exception as e:
        raise e

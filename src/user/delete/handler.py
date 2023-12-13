from schemas.response import Response, ResponseCodes
from utils.database import DB
from utils.get_secrets import get_secret
import json


def main(event, context):
    try:
        path_params = event.get('pathParameters', {})
        user_id = path_params.get('id')       
        print(json.dumps(event))
        creds = get_secret()
        db = DB(creds)
        resp = db.delete_user(user_id)
        if not resp:
            return Response(statusCode=ResponseCodes.NOT_FOUND.value, body=json.dumps({"message":"User not found"}), headers=json.dumps({}))
        return Response(statusCode=ResponseCodes.OK.value, body=json.dumps(resp), headers=json.dumps({}))
    except Exception as e:
        raise e

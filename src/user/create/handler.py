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
        print(json.dumps(event))
        creds = get_secret()
        db = DB(creds)
        resp = db.create_user(json.loads(event["body"]))
        if isinstance(resp,list):
            return Response(statusCode=ResponseCodes.BAD_REQUEST.value, body=json.dumps(resp), headers=json.dumps({}))
        return Response(statusCode=ResponseCodes.OK.value, body=json.dumps(resp), headers=json.dumps({}))
    except Exception as e:
        print("ERROR in LAMBDA",e)
        raise e

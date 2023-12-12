from schemas.response import Response, ResponseCodes
from utils.database import DB
from utils.get_secrets import get_secret
import json


def main(event, context):
    try:
        if "body" not in event:
            return Response(
                statusCode=ResponseCodes.BAD_REQUEST.value,
                body={"message": "Bad request"},
                headers={},
            ).__dict__
        print(json.dumps(event))
        creds = get_secret()
        db = DB(creds)
        resp = db.create_user(json.loads(event["body"]))
        print("Response", type(resp), resp)
        return {
                "statusCode":200,
                "body":json.dumps(resp)
                }
    except Exception as e:
        print("ERROR in LAMBDA",e)
        raise e

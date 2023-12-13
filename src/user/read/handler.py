from schemas.response import Response, ResponseCodes
from utils.database import DB
from utils.get_secrets import get_secret
import json


def main(event, context):
    try:
        creds = get_secret()
        db = DB(creds)
        resp = db.get_users()
        return Response(statusCode=ResponseCodes.OK.value, body=json.dumps(resp), headers=json.dumps({}))
    except Exception as e:
        raise e

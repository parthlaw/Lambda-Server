from schemas.response import Response, ResponseCodes


def main(event,context):
    if "body" not in event:
        return Response(
                statusCode=ResponseCodes.BAD_REQUEST.value,
                body={"message":"Bad request"},
                headers={}
                ).__dict__

from fastapi.responses import JSONResponse


def response(payload=None, status_code=200, error_message=None, success=None):
    content = {}
    if error_message is not None:
        content["message"] = error_message
    elif success is not None:
        content["success"] = success
        status_code = 200 if success else 500
    elif payload is not None:
        content["payload"] = payload

    return JSONResponse(status_code=status_code, content=content)

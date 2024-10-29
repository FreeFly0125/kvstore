from app.api.util import response


class APIException(Exception):
    def __init__(self, message=None, status_code=500):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code

    def getResponse(self):
        return response(status_code=self.status_code, error_message=self.message)


class NoJsonPayloadException(APIException):
    def __init__(self):
        super(NoJsonPayloadException, self).__init__(
            status_code=400, message="No JSON data in message body"
        )


class MalformedPayloadException(APIException):
    def __init__(self, description):
        super(MalformedPayloadException, self).__init__(
            status_code=400, message="The JSON payload was malformed: " + description
        )


class TenantNotFoundException(APIException):
    def __init__(self):
        super(TenantNotFoundException, self).__init__(
            status_code=400, message="The tenant with the name is not exist"
        )

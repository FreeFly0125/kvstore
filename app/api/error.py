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
            status_code=404, message="The tenant is not exist"
        )


class InvalidTokenException(APIException):
    def __init__(self):
        super(InvalidTokenException, self).__init__(
            status_code=403, message="Token is invalid"
        )


class DataNotExistException(APIException):
    def __init__(self):
        super(DataNotExistException, self).__init__(
            status_code=404,
            message="Data with the id is not existing within the tenant",
        )


class BatchInsertFailException(APIException):
    def __init__(self, description):
        super(BatchInsertFailException, self).__init__(
            status_code=500,
            message=f"Data batch insertion is failed. The status is rollbacked.\n{description}",
        )


class DataInsertFailException(APIException):
    def __init__(self, description):
        super(DataInsertFailException, self).__init__(
            status_code=500,
            message=f"Data insertion is failed. {description}",
        )


class KeyAlreadyExistException(APIException):
    def __init__(self):
        super(KeyAlreadyExistException, self).__init__(
            status_code=409,
            message="Data key is already exist.",
        )


class TenantAlreadyExistException(APIException):
    def __init__(self):
        super(TenantAlreadyExistException, self).__init__(
            status_code=409,
            message="Tenant with the name is already exist.",
        )


class TenantDeleteFailException(APIException):
    def __init__(self, description):
        super(TenantDeleteFailException, self).__init__(
            status_code=500,
            message=f"Tenant delete is failed. {description}",
        )


class TenantRegisterFailException(APIException):
    def __init__(self, description):
        super(TenantRegisterFailException, self).__init__(
            status_code=500,
            message=f"Register a tenant is failed. {description}",
        )


class TenantFetchFailException(APIException):
    def __init__(self, description):
        super(TenantFetchFailException, self).__init__(
            status_code=500,
            message=f"Fetching tenent info is failed. {description}",
        )


class DataFetchFailException(APIException):
    def __init__(self, description):
        super(DataFetchFailException, self).__init__(
            status_code=500,
            message=f"Fetching data object is failed. {description}",
        )


class DataRemoveFailException(APIException):
    def __init__(self, description):
        super(DataRemoveFailException, self).__init__(
            status_code=500,
            message=f"Removing data object is failed. {description}",
        )

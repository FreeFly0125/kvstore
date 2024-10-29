from functools import wraps
from app.api import error

required_fields = {
    "tenant_register": ["name", "cap_limit", "data_ttl"],
    "tenant_login": ["name"],
}


def validate(schema):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kw):
            payload = kw["tenant"].dict()
            if not payload:
                raise error.NoJsonPayloadException()
            for field in required_fields[schema]:
                if payload[field] is None:
                    raise error.MalformedPayloadException(f"{field} field is missed.")
            return f(*args, **kw)

        return wrapper

    return decorator

from functools import wraps
from app.api import error
from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from dotenv import load_dotenv
import os
import jwt

load_dotenv()
secret_key = os.getenv("SECRET_KEY")

required_fields = {
    "tenant_register": ["name", "cap_limit"],
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


security = HTTPBearer()


def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, secret_key, algorithms="HS256")
        return payload["tenant_id"]
    except Exception:
        raise error.InvalidTokenException()

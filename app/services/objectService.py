from app.db.dbconnect import SessionLocal
from app.db.schemas import ObjectSchema

import datetime
import uuid

dbHandler = SessionLocal()


def insert_new_data(
    key: str, value: str, data_ttl: datetime.datetime, tenant_id: str = None
):
    object_id = uuid.uuid4()
    created = datetime.datetime.now()
    expired = created + datetime.timedelta(hours=data_ttl)

    try:
        new_obj = ObjectSchema(
            objectID=object_id,
            tenantID=tenant_id,
            key=key,
            value=value,
            created=created,
            expired=expired,
        )
        dbHandler.add(new_obj)
        dbHandler.commit()
        return True
    except Exception:
        return False

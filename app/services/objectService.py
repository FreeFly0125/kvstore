from app.db.dbconnect import SessionLocal
from app.db.schemas import ObjectSchema, TenantSchema
from app.models.object import ObjectModel
from app.api import error

from sqlalchemy import and_
from typing import List
import datetime
import uuid

dbHandler = SessionLocal()


def get_data_info(key: str, tid: str):
    try:
        data_obj = (
            dbHandler.query(ObjectSchema)
            .filter(and_(ObjectSchema.key == key, ObjectSchema.tenantID == tid))
            .first()
        )

        if not data_obj:
            return None

        time_now = datetime.datetime.now()
        if data_obj.expired < time_now:
            dbHandler.delete(data_obj)

            tenant = (
                dbHandler.query(TenantSchema)
                .filter(TenantSchema.tenantID == tid)
                .first()
            )
            tenant.curCount -= 1

            dbHandler.commit()
            raise error.DataExpiredException()

        return data_obj
    except Exception as e:
        raise error.DataFetchFailException(e.message)


def insert_new_data(info: ObjectModel, tenant_id: str = None):
    object_id = uuid.uuid4()
    created = datetime.datetime.now()
    expired = created + datetime.timedelta(seconds=info.ttl)

    try:
        new_obj = ObjectSchema(
            objectID=object_id,
            tenantID=tenant_id,
            key=info.key,
            value=info.value,
            created=created,
            expired=expired,
        )
        dbHandler.add(new_obj)

        tenant = (
            dbHandler.query(TenantSchema)
            .filter(TenantSchema.tenantID == tenant_id)
            .first()
        )
        tenant.curCount += 1

        dbHandler.commit()
        return True
    except Exception as e:
        dbHandler.rollback()
        raise error.DataInsertFailException(e.message)


def batch_insert_data(infos: List[ObjectModel], tenant_id: str = None):
    objects_to_insert = []
    for info in infos:
        object_id = uuid.uuid4()
        created = datetime.datetime.now()
        expired = created + datetime.timedelta(seconds=info.ttl)

        new_obj = ObjectSchema(
            objectID=object_id,
            tenantID=tenant_id,
            key=info.key,
            value=info.value,
            created=created,
            expired=expired,
        )
        objects_to_insert.append(new_obj)

    try:
        dbHandler.add_all(objects_to_insert)

        tenant = (
            dbHandler.query(TenantSchema)
            .filter(TenantSchema.tenantID == tenant_id)
            .first()
        )
        tenant.curCount += len(infos)

        dbHandler.commit()
        return True
    except Exception as e:
        dbHandler.rollback()
        raise error.BatchInsertFailException(e.message)


def delete_data_info(key: str, tid: str):
    try:
        data_obj = (
            dbHandler.query(ObjectSchema)
            .filter(and_(ObjectSchema.key == key, ObjectSchema.tenantID == tid))
            .first()
        )
        if not data_obj:
            raise error.DataNotExistException()
        dbHandler.delete(data_obj)

        tenant = (
            dbHandler.query(TenantSchema).filter(TenantSchema.tenantID == tid).first()
        )
        tenant.curCount -= 1

        dbHandler.commit()
        return True
    except Exception as e:
        raise error.DataRemoveFailException(e.message)

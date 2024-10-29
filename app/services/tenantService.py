from app.db.dbconnect import SessionLocal
from app.db.schemas import TenantSchema
from app.models.tenant import TenantModel

dbHandler = SessionLocal()


def get_all_tenants():
    return dbHandler.query(TenantSchema).all()


def get_single_tenant_with_name(name: str):
    try:
        tenant = dbHandler.query(TenantSchema).filter(TenantSchema.name == name).first()
        return tenant if tenant else False
    except Exception:
        return False


def get_single_tenant_with_tid(tid: str):
    try:
        tenant = (
            dbHandler.query(TenantSchema).filter(TenantSchema.tenantID == tid).first()
        )
        return tenant if tenant else False
    except Exception as e:
        print("error:", e)
        return False


def insert_new_tenant(tenant: TenantModel, tid: str):
    try:
        new_tenant = TenantSchema(
            tenantID=tid,
            name=tenant.name,
            capSize=tenant.cap_limit,
            curCount=0,
            dataTtl=tenant.data_ttl,
        )
        dbHandler.add(new_tenant)
        dbHandler.commit()
        return True
    except Exception:
        return False


def delete_tenant(tid: str):
    try:
        tenant = (
            dbHandler.query(TenantSchema).filter(TenantSchema.tenantID == tid).first()
        )
        if tenant:
            dbHandler.delete(tenant)
            dbHandler.commit()
            return True
        else:
            return False
    except Exception:
        return False

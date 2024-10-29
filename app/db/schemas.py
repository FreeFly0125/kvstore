from app.db.dbconnect import Base
from sqlalchemy import Column, Integer, String, Date, JSON


class TenantSchema(Base):
    __tablename__ = "Tenant"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tenantID = Column(String, nullable=False)
    name = Column(String, nullable=False)
    capSize = Column(Integer, nullable=False)
    curCount = Column(Integer, nullable=False)
    dataTtl = Column(Integer, nullable=False)


class ObjectSchema(Base):
    __tablename__ = "Object"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tenantID = Column(String, nullable=False)
    key = Column(String, nullable=False)
    value = Column(JSON, nullable=False)
    curCount = Column(Integer, nullable=False)
    created = Column(Date, nullable=False)

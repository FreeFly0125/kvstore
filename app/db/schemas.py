from app.db.dbconnect import Base
from sqlalchemy import Column, Integer, String, Date


class Tenants(Base):
    __tablename__ = "Tenant"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tenantID = Column(String, nullable=False)
    name = Column(String, nullable=False)
    capSize = Column(Integer, nullable=False)
    curCount = Column(Integer, nullable=False)
    ttl = Column(Integer, nullable=False)


class Tenants(Base):
    __tablename__ = "Datastore"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tenantID = Column(String, nullable=False)
    key = Column(String, nullable=False)
    value = Column(Integer, nullable=False)
    curCount = Column(Integer, nullable=False)
    created = Column(Date, nullable=False)

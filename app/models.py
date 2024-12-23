from app.database import base

from sqlalchemy import Column, Integer, String, ForeignKey


class Employees(base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    datetime = Column(String)
    department_id = Column(Integer)
    job_id = Column(Integer)

class Departments(base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, index=True)
    department = Column(String)

class Jobs(base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, index=True)
    job = Column(String)

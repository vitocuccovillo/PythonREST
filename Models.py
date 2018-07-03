from peewee import *

db = SqliteDatabase("chinook.db")

class BaseModel(Model):
    """A base model that will use our Sqlite database."""
    class Meta:
        database = db


class Employees(BaseModel):
    EmployeeId = PrimaryKeyField()
    FirstName = CharField(null=False)
    LastName = CharField(null=False)

    class Meta:
        database = db

import datetime
from peewee import *
from flask_login import UserMixin

DATABASE = SqliteDatabase('meals.sqlite')

class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = DATABASE

class Meal(Model):
    name = CharField()
    owner = CharField()
    breed = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Meal], safe=True)
    print("TABLES Created")
    DATABASE.close()

    
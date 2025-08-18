# import logger_config
import os
from dotenv import load_dotenv
from peewee import Model, IntegerField, CharField
from playhouse.db_url import connect

load_dotenv(override=True)

# logger_config.setup_logger("config", "config.log")

db = connect(os.environ.get("DATABASE"))


class Customer(Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    age = IntegerField()

    class Meta:
        database = db
        table_name = "customers"


db.create_tables([Customer])

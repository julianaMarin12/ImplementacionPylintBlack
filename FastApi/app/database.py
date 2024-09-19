from dotenv import load_dotenv
from peewee import *
import os

load_dotenv()

database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user= os.getenv("MYSQL_USER"),
    passwd = os.getenv("MYSQL_PASSWORD"),
    host = os.getenv("MYSQL_HOST")
)

class ComputerModel(Model):

    id_computer = AutoField(primary_key=True)
    manufacturer = CharField(max_length=50)
    model = CharField(max_length=50)
    processor = CharField(max_length=50)
    memory_size = IntegerField()
    storage_capacity = IntegerField()
    operating_system = CharField(max_length=50)
    graphics_card = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "computers" 

class TableModel(Model):

    id_table = AutoField(primary_key=True)
    brand = CharField(max_length=50)
    model = CharField(max_length=50)
    price = DecimalField(max_digits=10, decimal_places=1)
    support = IntegerField()
    color = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "tables"

"""
This module handles the database configuration and the creation of database models using Peewee ORM.
It also loads environment variables for sensitive configurations like database credentials.

Imports:
    - load_dotenv (from dotenv): Loads environment variables from a .env file.
    - From peewee: Peewee ORM classes and fields used to define the database models.
    - os: Provides functions to interact with the operating system.
"""


from dotenv import load_dotenv
from peewee import Model, MySQLDatabase, AutoField, CharField, IntegerField, DecimalField
import os

# Load environment variables from a .env file to manage sensitive data like database credentials
load_dotenv()

# Create a MySQL database connection using environment variables
database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),  # The name of the MySQL database
    user=os.getenv("MYSQL_USER"),  # MySQL username
    passwd=os.getenv("MYSQL_PASSWORD"),  # MySQL password
    host=os.getenv("MYSQL_HOST")  # MySQL host (can be localhost or a remote server)
)

# Define the ComputerModel class, representing the 'computers' table in the database
class ComputerModel(Model):

    # Define the fields (columns) in the 'computers' table
    id_computer = AutoField(primary_key=True)  # Auto-incrementing primary key
    manufacturer = CharField(max_length=50)  # Manufacturer name (max 50 characters)
    model = CharField(max_length=50)  # Model name (max 50 characters)
    processor = CharField(max_length=50)  # Processor details (max 50 characters)
    memory_size = IntegerField()  # Memory size (RAM) as an integer field
    storage_capacity = IntegerField()  # Storage capacity in GB as an integer field
    operating_system = CharField(max_length=50)  # Operating system (max 50 characters)
    graphics_card = CharField(max_length=50)  # Graphics card details (max 50 characters)

    # Meta class defines additional information about the model
    class Meta:
        database = database  # Specify the database connection to use for this model
        table_name = "computers"  # Define the name of the table in the database

# Define the TableModel class, representing the 'tables' table in the database
class TableModel(Model):

    # Define the fields (columns) in the 'tables' table
    id_table = AutoField(primary_key=True)  # Auto-incrementing primary key
    brand = CharField(max_length=50)  # Brand of the table (max 50 characters)
    model = CharField(max_length=50)  # Model name of the table (max 50 characters)
    price = DecimalField(max_digits=10, decimal_places=1)  # Price up to 10 digits and 1 decimal
    support = IntegerField()  # Integer field to represent how many items the table can support
    color = CharField(max_length=50)  # Color of the table (max 50 characters)

    # Meta class defines additional information about the model
    class Meta:
        database = database # Specify the database connection to use for this model
        table_name = "tables"  # Define the name of the table in the database

from fastapi import APIRouter, Body  # Importing necessary modules from FastAPI
from models.table import Table  # Importing the Table model
from database import TableModel  # Importing the database model for Table

# Create a new APIRouter instance for handling table-related routes
table_route = APIRouter()

# POST endpoint to create a new table
@table_route.post("/")
def create_table(table: Table = Body(...)):
    """
    Create a new table record in the database.
    
    Args:
        table (Table): The table object passed in the request body, which contains 
                       details such as brand, model, price, support, and color.

    Returns:
        dict: A success message indicating that the table was created successfully.
    """
    # Create a new table entry in the database
    TableModel.create(
        brand=table.brand, 
        model=table.model, 
        price=table.price, 
        support=table.support, 
        color=table.color
    )
    return {"message": "Table created successfully"}

# GET endpoint to retrieve all tables
@table_route.get("/")
def get_table():
    """
    Retrieve all table records from the database.

    Returns:
        list: A list of dictionaries, each representing a table's details.
    """
    # Query the database for all tables with id_table greater than 0 and return as a list of dictionaries
    table = TableModel.select().where(TableModel.id_table > 0).dicts()
    return list(table)

# GET endpoint to retrieve a specific table by its ID
@table_route.get("/{table_id}")
def get_table(table_id: int):
    """
    Retrieve a specific table by its ID.

    Args:
        table_id (int): The unique identifier of the table to retrieve.

    Returns:
        dict: The table details if found, or an error message if not found.
    """
    try:
        # Fetch the table with the given ID
        table = TableModel.get(TableModel.id_table == table_id)
        return table
    except TableModel.DoesNotExist:
        # Return an error message if the table with the given ID does not exist
        return {"error": "Table not found"}

    
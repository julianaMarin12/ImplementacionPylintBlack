"""Main module 
FastAPI: This is the main class from FastAPI, used to create the web application.
asynccontextmanager: Contextlib module is used to create asynchronous context managers.
connection: Imported from database, representing the database connection.
ComputerModel, TableModel: Database models that define the structure of the tables in the database.
computer_route and table_route: Imported from routers.computer and routers.table. 
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
from helpers.api_key_auth import get_api_key
from database import database as connection
from database import ComputerModel, TableModel
from routers.computer import computer_route
from routers.table import table_route

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manages the lifespan of the FastAPI application, handling database
    connection setup on startup and closure on shutdown.

    This context manager:
    - Connects to the database if the connection is closed.
    - Creates the necessary tables if they do not exist.
    - Ensures the database connection is closed when the application shuts down.

    Args:
        app (FastAPI): The FastAPI application instance.

    Yields:
        None: Execution yields control back to the app while it runs.
    """

    if connection.is_closed():
        connection.connect()
        connection.create_tables([ComputerModel, TableModel])

    try:
        yield
    finally:
        if not connection.is_closed():
            connection.close()

app = FastAPI(lifespan=lifespan) # Initialize FastAPI app with lifespan management

app.include_router(
    computer_route, 
    prefix="/api/computers", 
    tags=["computers"], 
    dependencies=[Depends(get_api_key)],
)# Computer routes

app.include_router(
    table_route,
    prefix="/api/tables",
    tags=["tables"],
    dependencies=[Depends(get_api_key)],
)# Register table routes

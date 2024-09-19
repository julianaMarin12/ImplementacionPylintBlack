"""Main module 
FastAPI: This is the main class from FastAPI, used to create the web application.
asynccontextmanager: Contextlib module is used to create asynchronous context managers.
connection: Imported from database, representing the database connection.
ComputerModel, TableModel: Database models that define the structure of the tables in the database.
computer_route and table_route: Imported from routers.computer and routers.table. 
"""

from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import database as connection
from starlette.responses import RedirectResponse
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

@app.get("/", include_in_schema=False)
def read_root():
    """
    Root endpoint that redirects to the API documentation.

    Returns:
        RedirectResponse: A response object that redirects the client to the "/docs" URL.
    """
    return RedirectResponse(url="/docs")


app.include_router(computer_route, prefix="/api/computers", tags=["computers"])# Computer routes
app.include_router(table_route, prefix="/api/tables", tags=["tables"])# Register table routes

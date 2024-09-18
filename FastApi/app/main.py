from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import database as connection
from database import ComputerModel, TableModel
from routers.computer import computer_route
from routers.table import table_route

@asynccontextmanager
async def lifespan(app: FastAPI):

    if connection.is_closed():
        connection.connect()
        connection.create_tables([ComputerModel, TableModel])

    try:
        yield
    finally:
        if not connection.is_closed():
            connection.close()

app = FastAPI(lifespan=lifespan)

app.include_router(computer_route, prefix="/api/computers", tags=["computers"])
app.include_router(table_route, prefix="/api/tables", tags=["tables"])

from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import database as connection
from routers.computer import computer_route
from routers.table import table_route

@asynccontextmanager
async def lifespam(app: FastAPI):

    if(connection.is_closed()):
        connection.connect()

    try:
        yield

    finally:
        if not (connection.is_closed()):
            connection.close()

app = FastAPI(lifespan = lifespam)

app.include_router(computer_route, prefix="/api/computers", tags=["computers"])
app.include_router(table_route, prefix="/api/tables", tags=["tables"])

from fastapi import FastAPI, Body
from models.table import Table
from app.database import TableModel

table_route = FastAPI()

@table_route.post("/")
def create_table(table: Table = Body(...)):
    TableModel.create(brand = table.brand, model = table.model, price = table.price, support = table.support, color = table.color)
    return {"message": "Table created successfully"}

@table_route.get("/")
def get_table():
    table = TableModel.select().where(TableModel.id_table > 0).dicts()
    return list(table)

@table_route.get("/{table_id}")
def get_table(table_id: int):
    try:
        table = TableModel.get(TableModel.id_table == table_id)
        return table
    except TableModel.DoesNotExist:
        return {"error": "Table not found"}
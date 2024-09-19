from fastapi import APIRouter, Body
from models.computer import Computer
from database import ComputerModel

computer_route = APIRouter()

@computer_route.post("/")
def create_computer(computer: Computer = Body(...)):
    ComputerModel.create(manufacturer=computer.manufacturer, model = computer.model, processor = computer.processor, memory_size = computer.memory_size, storage_capacity = computer.storage_capacity, operating_system = computer.operating_system, graphics_card = computer.graphics_card)
    return {"message": "Computer created successfully"}

@computer_route.get("/")
def get_computer():
    computer = ComputerModel.select().where(ComputerModel.id_computer > 0).dicts()
    return list(computer)

@computer_route.get("/{computer_id}")
def get_computer(computer_id: int):
    try:
        computer = ComputerModel.get(ComputerModel.id_computer == computer_id)
        return computer
    except ComputerModel.DoesNotExist:
        return {"error": "Computer not found"}
    
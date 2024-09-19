from fastapi import APIRouter, Body  # Importing necessary modules from FastAPI
from models.computer import Computer  # Importing the Computer model
from database import ComputerModel  # Importing the database model for Computer

# Create a new APIRouter instance for handling computer-related routes
computer_route = APIRouter()

# POST endpoint to create a new computer
@computer_route.post("/")
def create_computer(computer: Computer = Body(...)):
    """
    Create a new computer record in the database.
    
    Args:
        computer (Computer): The computer object passed in the request body, 
                             which contains details such as manufacturer, model, 
                             processor, memory size, storage capacity, operating system, 
                             and graphics card.

    Returns:
        dict: A success message indicating that the computer was created successfully.
    """
    # Create a new computer entry in the database
    ComputerModel.create(
        manufacturer=computer.manufacturer, 
        model=computer.model, 
        processor=computer.processor, 
        memory_size=computer.memory_size, 
        storage_capacity=computer.storage_capacity, 
        operating_system=computer.operating_system, 
        graphics_card=computer.graphics_card
    )
    return {"message": "Computer created successfully"}

# GET endpoint to retrieve all computers
@computer_route.get("/")
def get_computer():
    """
    Retrieve all computer records from the database.

    Returns:
        list: A list of dictionaries, each representing a computer's details.
    """
    # Query the database for all computers with id_computer greater than 0 and return as a list of dictionaries
    computer = ComputerModel.select().where(ComputerModel.id_computer > 0).dicts()
    return list(computer)

# GET endpoint to retrieve a specific computer by its ID
@computer_route.get("/{computer_id}")
def get_computer(computer_id: int):
    """
    Retrieve a specific computer by its ID.

    Args:
        computer_id (int): The unique identifier of the computer to retrieve.

    Returns:
        dict: The computer details if found, or an error message if not found.
    """
    try:
        # Fetch the computer with the given ID
        computer = ComputerModel.get(ComputerModel.id_computer == computer_id)
        return computer
    except ComputerModel.DoesNotExist:
        # Return an error message if the computer with the given ID does not exist
        return {"error": "Computer not found"}

    
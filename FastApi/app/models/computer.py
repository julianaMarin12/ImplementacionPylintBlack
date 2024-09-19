"""Computer model model.
BaseModel:The base class for creating data models using pydantic.
validator: A decorator provided by pydantic to define custom validation methods for fields.
Field: A function used to specify constraints, metadata, and validation rules on fields. 
"""

from pydantic import BaseModel, validator, Field

class Computer(BaseModel):
    """Computer model 
    This model defines the structure and attributes of a computer entity.

    Attributes:
        id (int): Represents the unique identifier for the computer.
        manufacturer(str): The manufacturer of the computer. 
        model(str):The model name of the computer. This is a string field.
        processor(str):Describes the processor in the computer.
        memory_size (int): Represents the size of the computers memory in gigabytes. 
        storage_capacity: int:  This field represents the storage capacity of the computer.
        operating_system(str):The operating system installed on the computer.
        graphics_card(str): The graphics card used in the computer.
    """
    id: int
    manufacturer: str
    model: str
    processor: str
    memory_size: int
    storage_capacity: int = Field(..., gt=0, le= 1000)
    operating_system: str
    graphics_card: str

    """Memory size validation
    Validator:
        @validator('memory_size'):This is a custom validation method for the memory_size field.
        Validation logic: The method ensures the memory_size value.
    """

    @validator('memory_size')
    def display_size_must_be_positive_and_max_four(cls,v):
        """
        Verify that the memory size is positive and not greater than 129.
        Args:
            v (int): The value of the memory size to validate.
        Returns:
            int: The value validated if correct.
        Raises:
            ValueError: If the memory size is less than or equal to 0 or greater than 129.
        """
        if v <= 0 or v > 129:
            raise ValueError('display_size must be a positive float and cannot exceed 129')
        return v       
    
    class Config:
        anystr_strip_whitespace = True

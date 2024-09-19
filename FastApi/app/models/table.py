"""Table model model.
BaseModel:The base class for creating data models using pydantic.
validator: A decorator provided by pydantic to define custom validation methods for fields.
Field: A function used to specify constraints, metadata, and validation rules on fields. 
"""

from pydantic import BaseModel, validator

class Table(BaseModel):
    """Table model
    This model defines the structure and attributes of a table entity.

    Attributes:
        id (int): Represents the unique identifier for the computer. 
        brand (str): The brand name for the table.
        model (str): The model name for the table.
        price (float): The price of the table.
        support (int): The number of support points for the table.
        color (str): The color of the table.
    """
    id: int
    brand: str
    model: str
    price: float
    support: int
    color: str
    
    @validator('support')
    def support_must_be_positive_and_max_four(cls, v):
        if v <= 0 or v > 4:
            raise ValueError('support must be a positive integer and cannot exceed 4.')
        return v

    class Config:
        anystr_strip_whitespace = True

from pydantic import BaseModel, validator, Field 

class Computer(BaseModel):
    id: int
    manufacturer: str
    model: str
    processor: str
    memory_size: int 
    storage_capacity: int = Field(..., gt=0, le= 1000)
    operating_system: str
    graphics_card: str
    

    @validator('memory_size')
    def display_size_must_be_positive_and_max_four(cls, v):
        if v <= 0 or v > 129:
            raise ValueError('display_size must be a positive float and cannot exceed 129')
        return v

    class Config:
        anystr_strip_whitespace = True


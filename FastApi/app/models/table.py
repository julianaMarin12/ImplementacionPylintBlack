from pydantic import BaseModel, validator, Field

class Table(BaseModel):
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

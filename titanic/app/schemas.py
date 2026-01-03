
from pydantic import BaseModel, Field

class Passenger(BaseModel):
    Pclass: int = Field(..., ge=1, le=3)
    Sex: str
    Age: float = Field(..., ge=0)
    SibSp: int = Field(..., ge=0)
    Parch: int = Field(..., ge=0)
    Fare: float = Field(..., ge=0)
    Embarked: str

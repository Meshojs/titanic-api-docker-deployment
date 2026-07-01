from pydantic import BaseModel, Field


class PassengerInput(BaseModel):
    Pclass: int = Field(..., ge=1, le=3, description="Ticket class: 1, 2, or 3")
    Sex: str = Field(..., description="'male' or 'female'")
    Age: float = Field(..., ge=0, le=100)
    SibSp: int = Field(..., ge=0, description="Siblings/spouses aboard")
    Parch: int = Field(..., ge=0, description="Parents/children aboard")
    Fare: float = Field(..., ge=0)

    class Config:
        json_schema_extra = {
            "example": {
                "Pclass": 3,
                "Sex": "male",
                "Age": 22,
                "SibSp": 1,
                "Parch": 0,
                "Fare": 7.25
            }
        }


class PredictionOutput(BaseModel):
    survived: bool
    survival_probability: float
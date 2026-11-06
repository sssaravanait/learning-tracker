from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator

class UserCreate(BaseModel):
    """ Request body for registration. Validation happens before any DB operations. """

    name: str = Field(..., min_length=1, max_length=100, description="User's name")
    email: EmailStr = Field(..., description="User's email address")
    password: str = Field(..., min_length=8, max_length=16, description="User's password")

    @field_validator("email")
    @classmethod
    def normalize_email(cls, value: str) -> str:
        """ Normalize email to lowercase. """
        return value.strip().lower()
    
    @field_validator("name")
    @classmethod
    def strip_name(cls, value: str) -> str:
        """ Strip whitespace from name. """
        value = value.strip()
        if not value:
            raise ValueError("Name cannot be empty or whitespace only")
        return value


class UserRead(BaseModel):
    """ Response body for user data. """

    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: EmailStr
    created_at: datetime
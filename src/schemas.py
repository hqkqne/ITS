from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    username: str = Field(max_length=18, gt=0)
    email: EmailStr
    password: str = Field(..., min_length=8)
    # phone_number: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str


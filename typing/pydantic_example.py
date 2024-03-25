from datetime import date
from typing import List, Optional

from pydantic import BaseModel, EmailStr, ValidationError, constr, validator


class Address(BaseModel):
    street: str
    city: str
    zip_code: constr(regex=r'^\d{5}$')  # Constrains the zip code to exactly 5 digits

class Profile(BaseModel):
    first_name: str
    last_name: str
    birth_date: date
    email: EmailStr
    addresses: List[Address]
    email_verified: bool = False  # Default value

    @validator('birth_date')
    def check_age(cls, v):
        today = date.today()
        age = today.year - v.year - ((today.month, today.day) < (v.month, v.day))
        if age < 18:
            raise ValueError('User must be at least 18 years old')
        return v

    @validator('email_verified', always=True)
    def check_email_verification(cls, v, values):
        if 'email' in values and not v:  # Checking if email is provided and not verified
            raise ValueError('Email must be verified')
        return v

try:
    user = Profile(
        first_name="John",
        last_name="Doe",
        birth_date="2000-01-0",	
        email="john.doe@example",
        addresses=[
            Address(street = "123 Main St", city = "Anytown", zip_code= "12345"),
            {"street": "124 Main St", "city": "Anytown", "zip_code": "54321"}

        ],
        email_verified=True
    )
    print(user)
except ValidationError as e:
    print(e)

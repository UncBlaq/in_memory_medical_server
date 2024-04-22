from pydantic import BaseModel

class Doctor(BaseModel):
    id : int
    name: str
    specialization: str
    phone : str
    is_available: bool = True

class DoctorCreate(BaseModel):
    name : str
    specialization: str
    phone : str





doctors = {
    1 : Doctor(
        id = "1",
        name = "Doctor1",
        specialization = "Dermatologist",
        phone = "0700000000",
        is_available = False
    ),
    2 : Doctor(
        id = "2",
        name = "Doctor2",
        specialization = "Cardiologist",
        phone = "0800000000",
        is_available = True
    ),
    3 : Doctor(
        id = "3",
        name = "Doctor3",
        specialization = "Neurologist",
        phone = "0900000000",
        is_available = True
    )
}
from typing import List
from enum import Enum

from pydantic import BaseModel

from schemas.patient import Patient, patients
from schemas.doctor import Doctor, doctors

# Helps to change status of Appointments
class AppointmentStatus(Enum):
    completed = 'COMPLETED'
    active = "ACTIVE"
    canceled = "CANCELLED"
    


class Appointment(BaseModel):
    id : int
    patient : int | Patient
    doctor : int | Doctor
    date : str
    status : str = AppointmentStatus.active.value


class AppointmentCreate(BaseModel):
    patient : int | Patient
    date : str
 


appointments : List = [
    Appointment(
        id = 1,
        patient = patients.get(1),
        doctor = doctors.get(1),
        date = "April 20th 2024",
        status = AppointmentStatus.active.value
    )
]
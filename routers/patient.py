from typing import Annotated

from fastapi import APIRouter, status, Depends

from services.patient import PatientService
from schemas.appointment import appointments, AppointmentStatus
from schemas.patient import PatientCreate, patients

router = APIRouter()

@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_patient(payload : PatientCreate):
    data = PatientService.create_doctor(payload)
    return data


@router.get("/get", status_code= status.HTTP_200_OK)
def get_patients():
    data = PatientService.process_patients()
    return {
        "message" : "Success",
        "data" : data
    }

@router.get("/get/{id}", status_code=status.HTTP_200_OK)
def get_patient_by_id(id : int):
    data = PatientService.process_patient_by_id(id)
    return data

@router.put("/edit", status_code=status.HTTP_202_ACCEPTED)
def edit_patient(patient_id : int, payload : PatientCreate):
    curr_patient = PatientService.fetch_patient_by_id(patient_id)
    curr_patient.name = payload.name
    curr_patient.age = payload.age
    curr_patient.gender = payload.gender
    curr_patient.weight = payload.weight
    curr_patient.height = payload.height
    curr_patient.phone = payload.phone

    return {
        "message" : "Doctor Successfully updated",
        "data" : curr_patient
    }

@router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient(patient_id : int):
    curr_patient = PatientService.fetch_patient_by_id(patient_id)
   
#if a patient with active  Appointment is deleted from the database, the said patient appointment's is cancelled 
    for appointment in appointments:
        if appointment.patient == curr_patient:
            appointment.status = AppointmentStatus.canceled.value

#And the doctor assigned to that appointment is available again
        appointed_doctor = appointment.doctor
        appointed_doctor.is_available = True

    del patients[patient_id]

     #Response not shown in response header as status is set to no content for delete operation

    return {
        "message" : "Patient deleted successfully"
    }
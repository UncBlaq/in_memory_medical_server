from fastapi import APIRouter, status

from schemas.doctor import doctors, DoctorCreate
from schemas.appointment import appointments, AppointmentStatus
from services.doctor import DoctorService


router = APIRouter()

@router.post("/create", status_code= status.HTTP_201_CREATED)
def create_doctor(payload : DoctorCreate):
    data = DoctorService.create_doctor(payload)
    return {
        "message" : "Doctor Successfully created",
        "data" : data
    }


@router.get("/get", status_code=status.HTTP_200_OK)
def get_doctors():
    data = DoctorService.process_doctors(doctors)
    return {
        "message" : "Successful",
        "data" : data
    }


@router.get("/get/{id}", status_code=status.HTTP_200_OK)
def get_doctor_by_id(id: int):
    data = DoctorService.process_doctor_by_id(id)
    return {
        "message" : "Successful",
        "data" : data
    }


@router.put("/edit/{id}", status_code=status.HTTP_202_ACCEPTED)
def edit_doctor(doctor_id : int, payload : DoctorCreate):
    curr_doctor = DoctorService.fetch_doctor_id(doctor_id)

    curr_doctor.name = payload.name
    curr_doctor.specialization = payload.specialization
    curr_doctor.phone = payload.phone
    return {
        "message" : "Doctor Successfully updated",
        "data" : curr_doctor
    }


@router.delete("/delete/{id}",  status_code= status.HTTP_204_NO_CONTENT)
def delete_doctor(doctor_id : int):
    #If doctor with provided Id has an active appointment, The appointment gets cancelled and patient can rebook an Appointment
    curr_doctor = DoctorService.fetch_doctor_id(doctor_id)
    if curr_doctor.is_available is False:
        for appointment in appointments:
            if appointment.doctor == curr_doctor:
                appointment.status = AppointmentStatus.canceled.value

    del doctors[doctor_id]
    #Response not shown in response header as status is set to no content for delete operation

    return {
        "message": f"Doctor with id {doctor_id} has been deleted hence not available, Active appointment is also cancelled. Appointed patient to doctor id '{doctor_id}' can rebook an Appointment"
    }
       


@router.patch("/set_to_unavailable", status_code=status.HTTP_202_ACCEPTED)
def set_avalilability_status(doctor_id : int):
    curr_doctor = DoctorService.fetch_doctor_id(doctor_id)
    #Code fragment sets availablity of provided doctor's id to false
    curr_doctor.is_available = False
    for appointment in appointments:
        if appointment.doctor == curr_doctor:
                appointment.status = AppointmentStatus.canceled.value
    return {
        "message": f"Doctor with id {doctor_id} is not available, all current appointments are also cancelled. Appointed patient to doctor id '{doctor_id}' can rebook an Appointment",
    }
       

    


    
    
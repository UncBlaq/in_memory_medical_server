from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException

from services.appointment import AppointmentService
from schemas.appointment import AppointmentCreate, appointments, AppointmentStatus
from schemas.doctor import doctors

router = APIRouter()


#Only patients creates Appointments and if patient not available, proper response codes are given from fuction in service
@router.post("/book", status_code= status.HTTP_201_CREATED)
def book_appointment(payload : AppointmentCreate):
    data = AppointmentService.create_appointment(payload)
    return {
        "message" : "Appointment Successfully created",
        "data" : data
    }

@router.get("/get", status_code=status.HTTP_200_OK)
def get_appointments():
     return appointments

@router.get("/get/{id}", status_code=status.HTTP_200_OK)
def get_appointment_by_id(id : int):
      appointment = AppointmentService.process_appointment_by_id(id)
      print(appointment)
      return {
            "message" : f"Appointment with id '{id} fetched successfully",
            "data" : appointment   
      }            
    
@router.put("/process_appointments/{id}", status_code=status.HTTP_202_ACCEPTED)
def process_appointments(appointment_id : Annotated[int, Depends(AppointmentService.does_appointments_exist)]):
    #If an Appointment is already processed, then the appointed doctor will be free again
    doctors_values = list(doctors.values())
    for doctor in doctors_values:
                if appointment_id == doctor.id:
                    doctor.is_available = True
#Status changes to completed
    for appointment in appointments:
        if appointment.id == appointment_id:
            # Checks If appointment with provided id was already cancelled
            if appointment.status == AppointmentStatus.canceled.value:
                 return {
                      "message": "This appointment was already canceled hence cannot be processed"
                 }
            #Else Process the appointment
            appointment.status = AppointmentStatus.completed.value

            return {
            "message" : "Appointment Processed Successfully"
            } 

@router.put("/cancel_appointment/{id}", status_code=status.HTTP_202_ACCEPTED)
def cancel_appointment(appointment_id : Annotated [int, Depends(AppointmentService.does_appointments_exist)]):
        #If an appointment is cancelled, the appointed doctor gets to be available again
        doctors_values = list(doctors.values())
        for doctor in doctors_values:
                if appointment_id == doctor.id:
                    doctor.is_available = True
    
    #status changes to cancelled
        for appointment in appointments:
            if appointment.id == appointment_id:
                     # Checks If appointment with provided id was already processed
                if appointment.status == AppointmentStatus.completed.value:
                            return {
                      "message": "This appointment was already processed hence cannot be cancelled"
                 }
                     
                appointment.status = AppointmentStatus.canceled
                return {
                 "message" : "Appointment Cancelled Successfully"
                    }
     
     
     


        

            

    
    
    
    
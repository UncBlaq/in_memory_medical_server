from fastapi import HTTPException, status, Depends

from schemas.appointment import Appointment, appointments, AppointmentCreate, AppointmentStatus
from schemas.patient import patients
from schemas.doctor import doctors

class AppointmentService:
     
     @staticmethod
     def check_doctor_availability():
         doctors_values = list(doctors.values())
         for doctor in doctors_values:
             if doctor.is_available == True:
                return doctor
         raise HTTPException(
             status_code=status.HTTP_404_NOT_FOUND,
             detail="No available doctors at the moment. Check back later to book your Appointment"
         )
     

     @staticmethod
     def patient_availability(payload : AppointmentCreate):
         if payload.patient not in patients:
             raise HTTPException(
                 status_code=status.HTTP_404_NOT_FOUND,
                 detail= f"Patient with id '{payload.patient}' not registerd in our System"
             )
         return payload.patient

     @staticmethod
     #Creates Appointment
     def create_appointment(payload : AppointmentCreate):
        appointment_id = len(appointments) + 1
        current_patient = AppointmentService.patient_availability(payload)
        available_doctor = AppointmentService.check_doctor_availability()
        appointment = Appointment(
            id = appointment_id,
            patient = current_patient,
            doctor = available_doctor,
            date = payload.date,
            status = AppointmentStatus.active.value
        )

        #Code fragment ensures appointed doctor availability is set to false which makes him unavailable
        available_doctor.is_available = False
        appointments.append(appointment)
        return appointment
     
     @staticmethod
     def does_appointments_exist(appointment_id : int):
         
         appointment_ids = [appointment.id for appointment in appointments]
         if appointment_id not in appointment_ids:
            raise HTTPException(
                 status_code= status.HTTP_404_NOT_FOUND,
                 detail= f"Appointment with id '{appointment_id}' not found"
             )
         return appointment_id
     
     @staticmethod
     def return_appointed_doctor(appointment_id : int):
         for doctor in doctors:
             if appointment_id == doctor:
                 return doctor
             

     @staticmethod
     #feteches appointment with provided id
     def process_appointment_by_id(id : int):
         curr_appointment = None

         for appointment in appointments:
             if appointment.id == id:
                 curr_appointment = appointment
                 break
         if not curr_appointment:
                 raise HTTPException(
                     status_code=status.HTTP_404_NOT_FOUND,
                     detail= f"Appointment with id '{id}' not found"
                 )

         return curr_appointment
    
    
     
        

             
 

        
         
  
             

       

         
        


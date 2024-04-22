from fastapi import HTTPException, status

from schemas.doctor import doctors, DoctorCreate, Doctor

class DoctorService:

    @staticmethod
# Fetches all doctors
    def process_doctors(doctors):
        data = []
        for doctor_id in doctors:
            data.append(doctors[doctor_id])
        return {
            "message": "Successful",
            "data" : data
        }
    
    @staticmethod
    #fetches doctor with provided id
    def process_doctor_by_id(id):
        data = doctors.get(id)
        if data is None:  
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail= f"Doctor with id '{id}' not found"
            )
        return data

    @staticmethod
#creates  a doctor
    def create_doctor(payload : DoctorCreate):
        id = len(doctors) + 1
        doctor = Doctor(
            id = id,
            **payload.model_dump()
        )
        doctors[id] =doctor
        return doctor
        
    @staticmethod
    #fetches doctor from database and returns proper response if doctor with provided id is unavailable, for edit and delete of a doctor
    def fetch_doctor_id(doctor_id : int):
        curr_doctor = None
        doctors_values = list(doctors.values())
        for doctor in doctors_values:
                    if doctor.id == doctor_id:
                        curr_doctor = doctor
                        break
                        
        if not curr_doctor: 
            raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Doctor with id {doctor_id} not available"
                        )
        return curr_doctor
        

        
        

     


from fastapi import HTTPException, status

from schemas.patient import patients, Patient, PatientCreate

class PatientService:

    @staticmethod
    #gets all patients in the database
    def process_patients():
        data = []
        for patient_id in patients:
            data.append(patients[patient_id])
        return {
            "message": "Successful",
            "data" : data
        }
    
    @staticmethod
    #Provides patient details with provided id

    def process_patient_by_id(id : int):
        data = patients.get(id)
        if data is None:  
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail= f"Patient with id '{id}' not found"
            )
        return data
    
    @staticmethod

    def create_doctor(payload : PatientCreate):
        id = len(patients) + 1
        patient = Patient(
            id = id,
            **payload.model_dump()
        )
        patients[id] = patient
        return patient
    
    @staticmethod

    #fetches id and if not available, returns proper response
    def fetch_patient_by_id(patient_id):
        curr_patient = None
        patient_values = list(patients.values())
        for patient in patient_values:
                    if patient.id == patient_id:
                        curr_patient = patient
                        break
                        
        if not curr_patient: 
            raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Patient with id {patient_id} not available"
                        )
        return curr_patient

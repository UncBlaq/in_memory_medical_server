from pydantic import BaseModel

class Patient(BaseModel):
    id : int
    name : str
    age : int
    gender : str
    weight : str
    height : str
    phone : str

class PatientCreate(BaseModel):
    name : str
    age : int
    gender : str
    weight : str
    height : str
    phone : str


patients = {
   1 : Patient(
       id = 1,
       name = "patient1",
       age = 25,
       gender = "Male",
       weight = "60",
       height = "4.5ft",
       phone = "07000000000"
   ),
   2 : Patient(
       id = 2,
       name = "patient2",
       age = 25,
       gender = "Male",
       weight= "65",
       height = "6ft",
       phone = "08000000000"
   )
}
from fastapi import FastAPI, status

import routers.appointment
import routers.doctor
import routers.patient

app = FastAPI()

app.include_router(
    router= routers.doctor.router,
    prefix="/doctors",
    tags=["Doctors"]
)

app.include_router(
    router= routers.patient.router,
    prefix= "/patients",
    tags= ["Patients"]
)

app.include_router(
    router= routers.appointment.router,
    prefix = "/appointments",
    tags= ["Appointments"]
)

@app.get("/Home", status_code=status.HTTP_200_OK, tags=["Home Page"])
def home():
    return {
        "message" :"Welcome to our medical Application!"
    }
import uvicorn
from fastapi import FastAPI

from application.routes import users, vehicle_plate

app = FastAPI(title="vehicle plate validator backend")

app.include_router(vehicle_plate.router)
app.include_router(users.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)

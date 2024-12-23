import uvicorn
from fastapi import FastAPI

app = FastAPI(title="vehicle plate validator backen")


@app.get("/plates")
async def get_plates():
    return {"message": "Welcome to FastAPI"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)

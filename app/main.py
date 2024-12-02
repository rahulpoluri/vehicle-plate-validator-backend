from fastapi import FastAPI

app = FastAPI(title="vehicle plate validator backend")


@app.get("/plates")
async def get_plates():
    return {"message": "Welcome to FastAPI"}

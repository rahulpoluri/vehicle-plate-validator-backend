import os
from datetime import datetime, timedelta

import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

# from passlib.hash import pbkdf2_sha256

oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = os.getenv("SECRET_KEY")
TOKEN_EXPIRY_MINUTES = os.getenv("TOKEN_EXPIRY_MINUTES", 60)
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")


def generate_timed_token(username: str, password: str):
    payload = {
        "username": username,
        "password": password,
        "exp": datetime.utcnow()
        + timedelta(minutes=int(TOKEN_EXPIRY_MINUTES)),
    }
    jwt_token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return jwt_token


def generate_forever_token(username: str, password: str):
    payload = {"username": username, "password": password}
    jwt_token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return jwt_token


def generate_token(username, password, role):
    if role == "machine":
        return generate_forever_token(username, password)
    else:
        return generate_timed_token(username, password)


def verify_username_and_password(
    token: OAuth2PasswordBearer = Depends(oauth2_schema),
):
    pass
    # check if username exists in db
    # if yes get the password hash for it
    # if pbkdf2_sha256.verify(password, password_hash):
    #     return True
    # else:
    #     return False

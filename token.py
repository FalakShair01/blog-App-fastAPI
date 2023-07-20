from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Annotated
from fastapi import Depends, HTTPException, status
from .schemas import TokenData



SECRET_KEY = "137e57550a20b1c591bf350ae6cb7ff3362ce1dfaaa700a5424b2c7d9ecbfdf9"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email==email)
    except JWTError:
        raise credentials_exception
        
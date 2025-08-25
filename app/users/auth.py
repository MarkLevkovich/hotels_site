from passlib.context import CryptContext
from datetime import datetime, timedelta, UTC
from jose import jwt



pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(UTC) + timedelta(minutes=30)
    to_encode.update({'exp':expire})
    encoded_jwt = jwt.encode(
        to_encode,'qwerty123','HS256'
    )
    return encoded_jwt

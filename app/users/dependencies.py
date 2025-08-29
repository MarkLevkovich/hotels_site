from fastapi import Request, HTTPException, status, Depends
from jose import jwt, JWTError
from datetime import datetime, UTC
from app.config import SECRET_KEY, ALGORITHM
from app.exeptions import ExpiredTokenException, AbsentTokenException, NoUserIDException, NoUserException, JWTException
from app.users.dao import UsersDAO


def get_token(request: Request):
    token = request.cookies.get('booking_access_token')
    if not token:
        raise AbsentTokenException
    return token

async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, SECRET_KEY, ALGORITHM
        )
    except JWTError:
        raise JWTException

    expire: str = payload.get('exp')
    user_id: str = payload.get('sub')

    if (int(expire) < datetime.now(UTC).timestamp()) or not expire:
        raise ExpiredTokenException
    if not user_id:
        raise NoUserIDException

    user = await UsersDAO.find_by_id(int(user_id))

    if not user:
        raise NoUserException
    return user

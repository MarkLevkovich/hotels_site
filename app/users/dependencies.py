from fastapi import Request, HTTPException, status, Depends
from jose import jwt, JWTError
from datetime import datetime, UTC
from app.config import SECRET_KEY, ALGORITHM
from app.users.dao import UsersDAO


def get_token(request: Request):
    token = request.cookies.get('booking_access_token')
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return token

async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, SECRET_KEY, ALGORITHM
        )
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    expire: str = payload.get('exp')
    user_id: str = payload.get('sub')

    if (int(expire) < datetime.now(UTC).timestamp()) or not expire:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    user = await UsersDAO.find_by_id(int(user_id))

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return user

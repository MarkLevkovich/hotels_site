from fastapi import HTTPException, status


UserAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail='[!] User already exists [!]'
)

IncorrectEmailOrPasswordException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='[!] Incorrect email or password [!]'
)

ExpiredTokenException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='[!] Token expire! [!]'
)

AbsentTokenException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='[!] Token absent! [!]'
)

NoUserException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='[!] No user with this id! [!]'
)

NoUserIDException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='[!] No user ID! [!]'
)

JWTException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='[!] JWT Error! [!]'
)

NoRoomException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail='[!] No free rooms, sorry! [!]'
)
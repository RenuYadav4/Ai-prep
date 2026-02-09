from passlib.context import CryptContext   #type: ignore
from datetime import datetime, timedelta
from jose import jwt  #type: ignore
from dotenv import load_dotenv  #type: ignore
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRES = int(os.getenv("ACCESS_TOKEN_EXPIRES", 30))

pwd_context =  CryptContext(schemes=["bcrypt"], deprecated="auto")


# hashing the password
# - takes plain password
# - returns bcrypt hased password
# - Automatically adds salt
# - pwd_context.hash()  = bcrypt.hash() 
def hash_password(password:str)->str:
    return pwd_context.hash(password)

# pwd_context.verify() = bcrypt.compare()
def verify_password(password:str, hashed: str)-> bool:
    return pwd_context.verify(password,hashed)

def create_access_token(data: dict, expires_delta: timedelta | None=None):
    to_encode = data.copy()
    expire = datetime.utcnow()+(expires_delta or timedelta(minutes=15))
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode, SECRET_KEY,algorithm=ALGORITHM)


# dateTime -> gives current date and time
# timedelta -> represents a time duration
#  utc -> jwt requires utc time 
#  datetime.utcnow() returns current utc time
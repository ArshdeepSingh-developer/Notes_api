# app/auth.py

from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from app.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES



# Password hashing configuration
pwd_context = CryptContext(
    schemes=["bcrypt"], 
    deprecated="auto"
)


# ==============================
# PASSWORD FUNCTIONS
# ==============================

# Hash plain password before storing
def hash_password(password: str):
    return pwd_context.hash(password)


# Verify entered password during login
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# ==============================
# TOKEN CREATION
# ==============================

def create_access_token(data: dict):
    """
    data: dictionary containing user information
    We encode it into JWT token
    """

    to_encode = data.copy()

    # Add expiry time
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    # Create JWT token
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt
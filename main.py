from fastapi import FastAPI, HTTPException, Depends, Header
from jose import jwt
from datetime import datetime, time, timedelta, timezone

app = FastAPI()


SECRET_KEY = "mysecretkey"

ALGORITHM = "HS256"

# Create Token
def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({
        "exp": expire
    })
    token = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)

    return token




#Login API Token Generate
@app.post("/login")
def login(username: str, password: int):
    if username != "admin" or password != 12345:
        raise HTTPException(status_code=401, detail="Invalid Username and Password!")
    token = create_token({
        "sub": username
    })
    return{
        "access_token": token
    }


# Token verification
def verify_token(token: str = Header(None)):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(status_code=401, detail="Inavalid or expired token")

    
# Protected Route
@app.get("/secure")
def secure_data(user = Depends(verify_token)):
    return{
        "message": "Secure data accessed",
        "user": user
    }
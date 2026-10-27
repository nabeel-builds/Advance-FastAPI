from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

# Home Route
'''
@app.get("/")
def home():
    return{"message": "Hello World"}
'''
    


# Path parameter
# /users/1
'''
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return{
        "user_id": user_id
    }
'''


# Query Parameter
#/users?name=nabeel
#/products?price=1000
'''
@app.get("/users")
def get_users(name: str = None):
    return{"Name": name}


@app.get("/products")
def get_users(limit: int = 10):
    return{"limit": limit}
'''



# Multiple Query Parameter
#/items?name=Laptop&price=40000
'''
@app.get("/items")
def get_users(name: str = None, price: int = 0):
    return{
        "name": name,
        "price": price
    }
'''



@app.post("/create-user")
def create_user(user:User):
    return{
        "message": "User Created",
        "data": user
    }

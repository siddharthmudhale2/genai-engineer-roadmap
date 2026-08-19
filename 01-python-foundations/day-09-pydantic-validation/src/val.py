from pydantic import BaseModel, ValidationError

class User(BaseModel):
    name : str
    age : int
    
try:
    user = User(
        name = "Sidd",
        age = "hello"
    )
except ValidationError as error:
    print(error)

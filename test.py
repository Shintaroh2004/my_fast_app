from pydantic import BaseModel

class User(BaseModel):
    id:int
    name:str

string='{"id":100,"name":"hogege"}'
user=User.model_validate_json(string)

print(user)

print(type(user))
from ast import If
from os import name

from fastapi import FastAPI, Body, Request

app= FastAPI()

"""
@app.get("/")
async def root():
    return {"message": "Hello World"}
"""

# ======================================================================

"""
@app.get("/users/{user_id}") # get user_id from request body which is on swagger. 
def get_user(user_id):
    return {"user_id": user_id}

# Input: http://127.0.0.1:8000/users/3
# output:{"user_id": "3"}

"""
# ======================================================================

# Data Type Validation
"""
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

input: http://127.0.0.1:8000/users/abc: will give error user_id isn't integer.
"""

# ======================================================================

# Query Parameters
# Like : /uses?name=mohit, /products?price=1000

"""
# 1. Basic Implementation:

@app.get("/users")
def get_user(name):
    return {"name": name}

# input: http://127.0.0.1:8000/users?name=10
# output: {"name":"10"}
"""

"""
# 2. Optional Query Parameters:

@app.get("/users")
def get_user(name: str = None):
    return {"name": name}

# input: http://127.0.0.1:8000/users?name=1s2e
# output: {"name":"1s2e"}
"""

"""
# 3. Default Values:

@app.get("/products")
def get_user(limit: int = 10): # default is 10 if give any then it will set . 
    return {"limit" :limit }

# input: http://127.0.0.1:8000/products
# output: {"limit":10}

"""

"""
# 4. Multiple Query Parameters: 

@app.get("/items")
def get_user(name: str = None, price: int = 0):
    return {"name": name, "price": price}

# input: http://127.0.0.1:8000/items
# output: {"name":null,"price":0}
"""

# ======================================================================

# Agar tum URL ke query parameters ko dynamically receive karna chahte ho, toh Request object use kar sakte ho:

"""
@app.get("/users")
async def get_users(request: Request):
    query_params = dict(request.query_params)
    return query_params

# input: http://127.0.0.1:8000/users?id=90&age=kishan
# output: {"id":"90","age":"kishan"}
"""
# ======================================================================

## Implementing POST APIs in FastAPI ##

"""
@app.post("/create-user")
def create_user(name:str, age:int):
    return{"name": name, "age":age}

# input: http://127.0.0.1:8000/create-user?name=kishan&age=23
# output: {"name":"kishan","age":23}
"""
"""
# Handling JSON:
@app.post("/create-user")
def create_user( user : dict ) :
	return {
	"msg": "User created",
	"data": user }
# here we can give number of arguments in the request body in json form

# input:{
#   "name": 
#          {
#           "first": "kishan",
#           "last": "namedev"
#          }
# }

# output: {
#   "msg": "User created",
#   "data": {
#     "name": {
#       "first": "kishan",
#       "last": "namedev"
#     }
#   }
# }

"""
# ======================================================================

# ############## Data Validation with Pydantic ##############

"""
from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
		
class User(BaseModel):
	name: str
	age: int
	
@app.post("/create-user")
def create_user(user: User):
    return{"user": user}

# Input: 
# {
#   "name": "kishan",
#   "age": 3
# }

# Output: 
# {
#   "user": {
#     "name": "kishan",
#     "age": 3
#   }
# }
"""



# Introduction to Pydantic Models:
"""
from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()
class User(BaseModel):
	name: str
	age: int
	email: str

@app.post("/create-user")
def create_user(user: User):
	return{
	"msg" : " User created",
	"data": user
}

# input:{
#   "name": "radha",
#   "age": 16,
#   "email": "radhmohaju@gmail.com"
# }

# output: {
#   "msg": " User created",
#   "data": {
#     "name": "radha",
#     "age": 16,
#     "email": "radhmohaju@gmail.com"
#   }
# }
"""

# Automatic Data Validation:
"""
from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()

class Address(BaseModel):
	city: str
	state: str
	pincode: int
class User(BaseModel):
	name: str
	age: int
	address: Address # this "Address" link with above class Address
	
@app.post("/create-user")
def create_user(user: User):
	return{
	"msg" : " User created",
	"data": user
}

# Request body schema will be look like this: 
# {"name": "string",
#   "age": 0,
#  "address":{
#     "city":"string",
#     "pincode": 0}
# }

# input:{
#   "name": "kishan",
#   "age": 21,
#   "address": {
#     "city": "indore",
#     "state": "MP",
#     "pincode": 4520
#   }
# }
# output: {
#   "msg": " User created",
#   "data": {
#     "name": "kishan",
#     "age": 21,
#     "address": {
#       "city": "indore",
#       "state": "MP",
#       "pincode": 4520
#     }
#   }
# }
"""


################# FastAPI CRUD Operations: #####################

# from fastapi import FastAPI
# from pydantic import BaseModel
# app= FastAPI()

# todos=[]
# class Todo(BaseModel):
# 	id: int
# 	title: str
# 	completed: bool

# # to post the todo
# @app.post("/todos")
# def create_todo(todo: Todo):
# 	todos.append(todo)
# 	return {"message": "Todo added", "data": todo}
	
# # to get all todos
# @app.get("/todos")
# def get_todo():
# 	return todos
	
# # to get particular todo using path params
# @app.get("/todos/{todo_id}")
# def  get_id(todo_id: int):
# 	for todo in todos:
# 		if todo.id==todo_id:
# 			return todo
# 	return {"error": "Todo not found"}

# # to update
# @app.put("/todos/{todo_id}")
# def  update_todo(todo_id: int):
# 	for todo in todos:
# 		if todo.id==todo_id:
# 			return todo
# 	return {"error": "Todo not found"}









# todos={
#     1: {"task": "Do laundry", "completed": False},
#     2: {"task": "Buy groceries", "completed": True},
#     3: {"task": "Clean the house", "completed": False} 
#     #  {"task": "Do laundry", "completed": False},
#     #  {"task": "Buy groceries", "completed": True},
#     #  {"task": "Clean the house", "completed": False}  
# }






# # GET Method to retrieve all todos
# @app.get("/todos")
# async def get_todos():
#     return todos

# # POST Method to create a new todo
# @app.post("/todos/create")
# async def create_todo(new_todo=Body(...)):
#     new_id = max(todos.keys()) + 1
#     todos[new_id] = new_todo
#     # todos.append(new_todo)
#     return {
#         "message": "Todo created successfully",
#         "todo": new_todo
#     }

# # PUT Method to update an existing todo
# @app.put("/todos/update/{todo_id}") 
# async def update_todo(todo_id: int, updated_todo=Body(...)):
#     if todo_id in todos:
#         todos[todo_id] = updated_todo
#         return {
#             "message": "Todo updated successfully",
#             "todo": updated_todo
#         }
#     else:
#         return {"message": "Todo not found"}

# # DELETE Method to delete a todo
# @app.delete("/todos/delete/{todo_id}")
# async def delete_todo(todo_id: int):
#     if todo_id in todos:
#         deleted_todo = todos.pop(todo_id)
#         return {
#             "message": "Todo deleted successfully",
#             "todo": deleted_todo
#         }
#     else:
#         return {"message": "Todo not found"}

# def get_completed_todos():
#     completed_todos = {id: todo for id, todo in todos.items() if todo["completed"]}
#     return completed_todos

# from fastapi import FastAPI, Request

# app = FastAPI()

# @app.get("/users")
# async def get_users(request: Request):
#     query_params = dict(request.query_params)
#     return query_params
from fastapi import FastAPI
from typing import Optional

# simple web server
app = FastAPI()


# root endpoint
@app.get("/")
async def read_root():
    return {"message": "Hello World"}


# end point with path parameter
# @app.get('/greet/{name}')
# async def greet(name : str) -> dict:
#     return {"message" : f"Hello {name}"}


# end point with query parameter
@app.get("/greet")
async def greet(name: str) -> dict:
    return {"message": f"Hello {name}"}


# query parameter with path parameter
@app.get("/greet/{name}")
async def greet_withage(name: str, age: int) -> dict:
    return {"message": f"Hello {name} ", "age": age}


# optional parameters
# @app.get("/")
# async def greet_name(name: Optional[str] = "User", age: int = 0) -> dict:
#     return 0

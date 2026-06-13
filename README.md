```
A project touchbasing concepts of fast api
```



Uv init 

Uv run main.py 

Uv add PACKAGES

UV run uvicorn main:app —reload 

main:app -> filename:fastapiObject name


Notes:
>we are using uv package manager so "uv init" is going to initiate a python project for us,
>post initiatlizing we have also used "git init" to initiate the git versioning and pushed the initial to github as main branch. 
>"uv run main.py" is going to run the python file for us
>"uv add fastapi uvicorn" – is going to include these two packages as part of the pyproject.toml list. (similar top package.json)
>get,post,put,patch,delete
> params on routes are within "{}", @app.get("/books/{authorName})
> query params are not declared on routes @app.get("/book") and inside function we need to havea variable def_function_with_Params(authorname:str)
>use PYDANTIC to design data types, and for data validation


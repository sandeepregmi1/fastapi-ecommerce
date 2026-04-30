# /home/sandeep/Projects/fastapi-ecommerce/app/main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI is working 🚀"}
    #Root page can be accessed with http://127.0.0.1:8000 and it is root endpoint i.e the base URL of the application or the main page of the application
    # / is the root endpoint
    

#About route endpoint or About page

@app.get("/about")
def about():
    return {"message": "This is a simple FastAPI application"}

#  About page can be accessed with http://127.0.0.1:8000/about

@app.get("/contact")
def contact():
    return {"message": "Sandeep Regmi , +977 9804132622"}
#Contact page can be accessed with http://127.0.0.1:8000/contact


#Dynamic routing 
# Dynamic routing is a way to create routes that can be accessed with different values
# In other words, we can create routes that can be accessed with different values
# The values are passed as parameters to the function
# The parameters are passed as parameters to the function


#Example of dyanamic routing

# Path Parameters


@app.get("/products/{id}")
def get_products(id:int):
    return{"product_id":id}
# http://127.0.0.1:8000/products/1 will give the output as {"product_id":1} and
# # we can change the id dynamically like http://127.0.0.1:8000/products/2 , http://127.0.0.1:8000/products/3 and so on

# Query Parameters
# Query parameters are optional parameters that are passed as parameters to the function

@app.get("/search")
def search(name:str):
    return{"searching for the query:":name}

#http://127.0.0.1:8000/search?name=shirt can be accessed with http://127.0.0.1:8000/search?name=shirt 
# it returns {"query": "shirt"}


# the main differnece between path vs query parameters:
# path parameters are mandatory and are part of the URL
# query parameters are optional and are not part of the URL
# like path http://127.0.0.1:8000/products/1 is mandatory to add 1 "id" after /products/ 
# and query parameters http://127.0.0.1:8000/search?name=shirt can be accessed with http://127.0.0.1:8000/search?name=shirt 
#it returns {"query": "shirt"}
#and if we access without  http://127.0.0.1:8000/search it will not give an error because it is optional

@app.get("/product")
def get_product():
    return [
        {"id": 1, "name": "T-Shirt", "price": 500},
        {"id": 2, "name": "Shoes", "price": 2000}
    ]

# http://127.0.0.1:8000/product or http://127.0.0.1:8000/product?limit=1


@app.get("/product/{id}")
def get_product(id:int):
    product = [{"id": 1, "name": "T-Shirt", "price": 500},{"id": 2, "name": "Shoes", "price": 2000}]
    productf = ["apple","mango","banana","orange","grape"]

    return product[id-1],productf[id-1]

# http://127.0.0.1:8000/product/1 or http://127.0.0.1:8000/product/2
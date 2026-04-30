
from fastapi import FastAPI

# Create FastAPI application instance
app = FastAPI()


#  ROOT ENDPOINT
@app.get("/")
def root():
    """
    Root endpoint (Homepage)
    URL: http://127.0.0.1:8000/
    """
    return {"message": "FastAPI is working "}


# ℹ ABOUT ENDPOINT
@app.get("/about")
def about():
    """
    About page of the application
    URL: http://127.0.0.1:8000/about
    """
    return {"message": "This is a simple FastAPI application"}


# CONTACT ENDPOINT
@app.get("/contact")
def contact():
    """
    Contact information
    URL: http://127.0.0.1:8000/contact
    """
    return {"message": "Sandeep Regmi , +977 9804132622"}


# DYNAMIC ROUTING

# Path Parameter Example

@app.get("/products/{id}")
def get_products(id: int):
    """
    Get product using dynamic ID (Path Parameter)

    Example:
    http://127.0.0.1:8000/products/1

    Notes:
    - 'id' is REQUIRED
    - Must be integer (type validation)
    """
    return {"product_id": id}


#  Query Parameter Example
@app.get("/search")
def search(name: str):
    """
    Search endpoint using query parameter

    Example:
    http://127.0.0.1:8000/search?name=shirt

    Notes:
    - 'name' is OPTIONAL (can be improved with default value later)
    - Passed using ?key=value format
    """
    return {"search_query": name}


#  PRODUCT APIs (STATIC DATA)

# Get all products
@app.get("/product")
def get_all_products():
    """
    Returns list of all products

    URL:
    http://127.0.0.1:8000/product
    """
    return [
        {"id": 1, "name": "T-Shirt", "price": 500},
        {"id": 2, "name": "Shoes", "price": 2000}
    ]


#  Get product by ID
@app.get("/product/{id}")
def get_product_by_id(id: int):
    """
    Get single product using ID

    URL:
    http://127.0.0.1:8000/product/1

    Notes:
    - Uses list indexing (id - 1)
    - Not safe for large IDs (can cause IndexError)
    - In real apps → use database
    """

    products = [
        {"id": 1, "name": "T-Shirt", "price": 500},
        {"id": 2, "name": "Shoes", "price": 2000}
    ]

    fruits = ["apple", "mango", "banana", "orange", "grape"]

    return {
        "product": products[id - 1],
        "fruit": fruits[id - 1]
    }


"""
✔ Root endpoint → /
✔ Static routes → /about, /contact
✔ Path parameter → /products/{id}
✔ Query parameter → /search?name=shirt
✔ Product APIs → /product, /product/{id}

KEY DIFFERENCE:
- Path Parameter → Required, part of URL
- Query Parameter → Optional, after '?'

IMPORTANT:
- FastAPI auto converts dict → JSON
- Type hints (id: int) = validation
"""
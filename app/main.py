
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

# Cart API (query parameter)
@app.get("/cart")
def get_cart(id: int = 1):
    """Get cart item → /cart?id=1"""

    cart_items = [
        {"id": 1, "name": "Shirt", "price": 500},
        {"id": 2, "name": "Shoes", "price": 2000},
        {"id": 3, "name": "T-shirt", "price": 2000},
    ]

    if id < 1 or id > len(cart_items):
        return {"error": "Invalid cart item ID"}

    return {"cart_item": cart_items[id - 1]}


# Orders API (path parameter)
@app.get("/orders/{id}")
def get_orders(id: int):
    """Get order → /orders/1"""

    order_items = [
        {"id": 1, "status": "pending", "total": 500},
        {"id": 2, "status": "completed", "total": 1000},
        {"id": 3, "status": "cancelled", "total": 1500},
    ]

    if id < 1 or id > len(order_items):
        return {"error": "Invalid order ID"}

    return {"order": order_items[id - 1]}


# Notes for revision
"""
Root → /
Static routes → /about, /contact
Path parameter → /products/{id}, /orders/{id}
Query parameter → /search?name=shirt, /cart?id=1

Path parameter:
- required
- part of URL

Query parameter:
- optional
- after '?'

FastAPI automatically converts dictionary to JSON
Type hints (id: int) provide validation
"""
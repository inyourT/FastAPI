from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return {"message": "wellcome to Kicaw Dev"}

products = [
    Product(id=1, name="phone", description="budget phone", price=99, quantity=10),
    Product(id=2, name="laptop", description="laptop gaming", price=999, quantity=11),
    Product(id=3, name="pen", description="A blue ink pan", price=199, quantity=9),
    Product(id=4, name="table", description="A modern table", price=2222, quantity=6),
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return {"error": "produk tidak ada"}

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product

@app.put("/product")
def update_prpduct(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product Updated Succesfully"
    return "no product"

@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product Deleted"
    return "product not found"
from fastapi import FastAPI, Query
from typing import List, Optional
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Database setup
def init_db():
    conn = sqlite3.connect("shop_smart.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        brand TEXT,
                        macros TEXT,
                        category TEXT,
                        price REAL,
                        rating REAL)''')
    conn.commit()
    conn.close()

init_db()

class Product(BaseModel):
    name: str
    brand: str
    macros: str
    category: str
    price: float
    rating: float

@app.post("/add_product/")
def add_product(product: Product):
    conn = sqlite3.connect("shop_smart.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, brand, macros, category, price, rating) VALUES (?, ?, ?, ?, ?, ?)",
                   (product.name, product.brand, product.macros, product.category, product.price, product.rating))
    conn.commit()
    conn.close()
    return {"message": "Product added successfully"}

@app.get("/search/")
def search_products(
    keyword: Optional[str] = Query(None),
    price_min: Optional[float] = Query(None),
    price_max: Optional[float] = Query(None),
    rating_min: Optional[float] = Query(None),
    category: Optional[str] = Query(None)
):
    conn = sqlite3.connect("shop_smart.db")
    cursor = conn.cursor()
    query = "SELECT * FROM products WHERE 1=1"
    params = []

    if keyword:
        query += " AND (name LIKE ? OR brand LIKE ? OR macros LIKE ? OR category LIKE ?)"
        params.extend([f"%{keyword}%"] * 4)
    if price_min is not None:
        query += " AND price >= ?"
        params.append(price_min)
    if price_max is not None:
        query += " AND price <= ?"
        params.append(price_max)
    if rating_min is not None:
        query += " AND rating >= ?"
        params.append(rating_min)
    if category:
        query += " AND category = ?"
        params.append(category)

    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()

    return {"products": results}

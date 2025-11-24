import sqlite3

def init_db():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    price REAL,
    brand TEXT
);
""")

    products = [
        ("iPhone 14", "phone", 799, "Apple"),
        ("Samsung A52", "phone", 450, "Samsung"),
        ("Pixel 6a", "phone", 399, "Google"),
        ("HP Laptop 15s", "laptop", 550, "HP"),
        ("Dell Inspiron 3511", "laptop", 620, "Dell"),
        ("Sony WH-1000XM4", "headphones", 300, "Sony")
    ]

    cursor.executemany(
        "INSERT INTO products (name, category, price, brand) VALUES (?, ?, ?, ?)", 
        products
    )
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()

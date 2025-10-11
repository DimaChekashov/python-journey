from database import create_connection

def add_product(name, price, category):
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO products (name, price, category) 
        VALUES (?, ?, ?)
    ''', (name, price, category))
    
    conn.commit()
    conn.close()

products = [
    ("Ноутбук", 50000, "Электроника"),
    ("Стул", 2500, "Мебель"),
    ("Книга", 500, "Книги")
]

for product in products:
    add_product(*product)
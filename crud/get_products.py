from database import create_connection

def get_products():
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    
    total_price = sum(product[2] for product in products)
    categories = set(product[3] for product in products)
    
    print(f"Общая стоимость: {total_price} руб.")
    print(f"Категории: {categories}")
    
    return products

get_products()
from database import create_connection

def get_expenses():
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    conn.close()
    
    for expense in expenses:
        id, name, value, timestamp = expense
        print(f'date: {timestamp}, name: {name}, value: {value}')
    
    return expenses

def add_expense(name, price):
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO expenses (name, price) 
        VALUES (?, ?)
    ''', (name, price))
    
    conn.commit()
    conn.close()

import sqlite3

DB_NAME = 'tasks.db'

connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()
print('Database created successfully')
cursor.close()

def create_table():
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed BOOLEAN DEFAULT FALSE
            )
        ''')
        print('Table created successfully')

def add_task(title):
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO tasks (title) VALUES (?)',
            (title,)
        )
        print(f'Task \'{title}\' added successfully')
        
def get_all_tasks():
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM tasks')
        return cursor.fetchall()
    
def show_tasks():
    tasks = get_all_tasks()
    for task in tasks:
        status = "✅" if task[2] else "⏳"
        print(f"{status} {task[1]}")
        
def complete_task(task_id):
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(
            'UPDATE tasks SET completed = TRUE WHERE id = ?',
            (task_id,)
        )
        print(f'Task {task_id} completed successfully')
    
def delete_task(task_id):
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(
            'DELETE FROM tasks WHERE id = ?',
            (task_id,)
        )
        print(f'Task {task_id} deleted successfully')
        
create_table()
add_task('Task 1')
show_tasks()
complete_task(1)
show_tasks()
delete_task(1)
show_tasks()
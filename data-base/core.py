from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, insert, update, delete

engine = create_engine('sqlite:///users.db', echo=True)
print("✅ Подключение создано!")

metadata = MetaData()
users_table = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
)

metadata.create_all(engine)
print("✅ Таблица создана!")

with engine.connect() as connection:
    insert_query = insert(users_table).values([
        {'name': 'Bob'},
        {'name': 'Alice'},
        {'name': 'John'},
    ])
    
    result = connection.execute(insert_query)
    print(f' {result.rowcount} записей добавлены')
    
    select_query = users_table.select()
    result = connection.execute(select_query)
    users = result.fetchall()
    print(f'List of users:')
    for user in users:
        print(user)
        
    update_query = update(users_table).where(
        users_table.c.id == 1
    ).values(
        name='Bob the Great'
    )
    result_update = connection.execute(update_query)
    print(f'{result_update.rowcount} записей обновлены')
    
    result = connection.execute(select_query)
    users = result.fetchall()
    print(f'List of users:')
    for user in users:
        print(user)
        
    delete_query = delete(users_table).where(
        users_table.c.id == 3
    )
    result = connection.execute(delete_query)
    print(f'{result.rowcount} записей удалены')
    
    result = connection.execute(select_query)
    users = result.fetchall()
    print(f'List of users:')
    for user in users:
        print(user)
        
    connection.commit()
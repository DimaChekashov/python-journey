import os

def create_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)
        
def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()
    
def delete_file(file_name):
    os.remove(file_name)
    
create_file('test.txt', "Hello, world 1!")
create_file('test-2.txt', "Hello, world 2!")
create_file('test-3.txt', "Hello, world 3!")

print(read_file('test.txt'))
print(read_file('test-2.txt'))
print(read_file('test-3.txt'))

delete_file('test.txt')
delete_file('test-2.txt')
delete_file('test-3.txt')
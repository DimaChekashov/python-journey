import os
import json

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

with open('big_file.txt', 'w') as file:
    for i in range(1000):
        file.write(f"Строка номер {i+1}\n")
        
delete_file('big_file.txt')

# Dictionary
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "language": ["Python", "JavaScript", "C++"]
}

json_string = json.dumps(data, ensure_ascii=False, indent=2)
print("JSON string:")
print(json_string)

parsed_data = json.loads(json_string)
print("Parsed data:", parsed_data)

with open("test.json", 'w', encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)
    
with open('test.json', 'r', encoding='utf-8') as file:
    loaded_data = json.load(file)
    print("Loaded data:",loaded_data)
    
delete_file('test.json')
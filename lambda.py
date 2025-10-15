multipy = lambda x, y: x * y

add = lambda x, y: x + y

division = lambda x, y: x / y

print(multipy(2, 3))

try:
    print(division(2, 0))
except ZeroDivisionError:
    print("Cannot divide by zero")
    
print(add(2, 3))

try:
    value = add(2, 10)
    if value == 12:
        raise ValueError("Value cannot be 12")
except ValueError:
    print("Value cannot be 12")
def calculator(num1,num2,operation = "+"):
    if operation == '+':
        return num1 + num2
    if operation == '-':
        return num1 - num2
    if operation == '*':
        return num1 * num2
    if operation == '/':
        return num1 / num2

print(calculator(3, 2)) # 5
print(calculator(3, 2, '*')) # 6
print(calculator(3, 2, '-')) # 1)
q = int(input("Enter the first number:"))

s = int(input("Enter the second number:"))

operand = input("Enter the operation (+, -, *, /): ")

if operand == '+':
    print(q, "+", s, "=", q + s)
elif operand == '-':
    print(q, "-", s, "=", q - s)
elif operand == '*':
    print(q, "*", s, "=", q * s)
elif operand == '/':
    print(q, "/", s, "=", q / s)
else:
    print("Invalid operation")    
    
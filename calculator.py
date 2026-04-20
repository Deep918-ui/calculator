def calculate(n1, n2, op):
    if op == '+': return n1 + n2
    elif op == '-': return n1 - n2
    elif op == '*': return n1 * n2
    elif op == '/': return n1 / n2 if n2 != 0 else "Error: Division by zero"
    else: return "Invalid operator"

while True:
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        print(f"Result: {calculate(num1, num2, operator)}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

    if input("Continue? (y/n): ").lower() != 'y':
        break

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b

if __name__ == '__main__':
    while True:
        try:
            expr = input('Enter expression (e.g., 3 + 4): ')
            parts = expr.split()
            a = float(parts[0])
            op = parts[1]
            b = float(parts[2])
            if op == '+':
                print(add(a, b))
            elif op == '-':
                print(subtract(a, b))
            elif op == '*':
                print(multiply(a, b))
            elif op == '/':
                print(divide(a, b))
            else:
                print('Unsupported operator')
        except Exception as e:
            print('Error:', e)
            continue
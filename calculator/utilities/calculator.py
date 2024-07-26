def add(x, y):
    "the sum of x + y"
    return x + y

def subtract(x, y):
    "the difference x - y"
    return x - y

def multiply(x, y):
    "the product of x * y"
    return x * y

def divide(x, y):
    "the quotient of x / y"
    return x / y

def main():
    "Main function"
    x, y = 2, 2

    print(f"{x} + {y} = {add(x, y)}")
    print(f"{x} - {y} = {subtract(x, y)}")
    print(f"{x} * {y} = {multiply(x, y)}")
    print(f"{x} / {y} = {divide(x, y)}")

if __name__ == "__main__":
    main()

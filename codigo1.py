def get_valid_number(prompt_num):
    while True:
        number = input(prompt_num)

        if number.lower() == "q":
            return None
        
        try:
            num = float(number)
        except ValueError:
            print("Enter a valid number")
            continue

        return num
    
def get_valid_operator():
    while True:
        operator = input("Enter a valid operator(+, -, *, /): ")

        if operator in ["+", "-", "*", "/"]:
            return operator
        print("Enter a valid operator")

def calculate(op, a, b):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            try: 
                return a / b
            except ZeroDivisionError:
                print("second number cannot be zero")
                return None

def main():
    print("=== SIMPLE CALCULATOR ===")         

    while True:
        number = get_valid_number("Enter a number(q to quit): ")

        if number is None:
            break

        number2 = get_valid_number("Enter another number: ")

        if number2 is None:
            break

        operator = get_valid_operator()

        result = calculate(operator, number, number2)

        if result is not None:
            print(f"Result is {result}")

if __name__ == "__main__":
    main()
    



    



       
       
        
        
        
    
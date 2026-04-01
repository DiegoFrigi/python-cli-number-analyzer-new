num1 = float(input("Enter a number: "))
operator = input("Enter an operator(+, -, *, /): ")
num2 = float(input("Enter another number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print("You need to write an operator!")  


first_value = -3
second_value = 4
operator = "/"

if first_value is None or second_value is None:
    print("Can't divide None Value")
else:
    if operator == "+":
        print(first_value + second_value)
    elif operator == "-":
        print(first_value - second_value)
    elif operator == "*":
        print(first_value * second_value)
    elif operator == "/":
        if second_value == 0:
            print("Can't divide by zero")
        else:
            print(first_value / second_value)
    else:
        print("Operator is wrong. Choose from given: + 1 / *")





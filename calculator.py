def get_number(number):
    while True:
        operand = input(f"Enter Number {number} : ")
        try:
            return float(operand)

        except ValueError:
            print("Invalid Input, try again")
operand = get_number(1)
operand2 = get_number(2)


sign = input("Add Sign: ")

result = 0
print(operand, sign, operand2)
if sign == "+":
    result = operand + operand2
elif sign == "-":
    result = operand - operand2
elif sign == "*":
    result = operand * operand2
elif sign == "/":
    if operand2 != 0:
        result = operand / operand2
    else:
        print("Divided by zero")
elif sign == "=":
    result = operand == operand2
elif sign == "<":
    result = operand < operand2
elif sign == ">":
    result = operand > operand2
elif sign == "<=":
    result = operand <= operand2
elif sign == "%":
    result = operand % operand2
elif sign == "//":
    if operand2 != 0:
        result = operand // operand2
    else:
        print("Please provide a valid data, i.e. greater than zero")
elif sign == "**":
    result = operand ** operand2
else:
    print("Please provide a valid sign")

print(result)



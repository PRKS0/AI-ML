def Calc(num1, num2, operator = "add"):
    if operator == "add":
        return num1 + num2
    elif operator == "subtract":
        return num2 - num1
    elif operator == "divide":
        return num2/num1
    elif operator == "multiply":
        return num1 * num2


print(Calc(1, 2, "add"))
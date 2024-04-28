input = input("Expression: ")
x, y, z = input.split(" ")

if y == "+":
    print(float(x) + float(z))
elif y == "-":
    print(float(x) - float(z))
elif y == "*":
    print(float(x) * float(z))
elif y == "/":
    if z != "0":
        print(float(x) / float(z))
    else:
        print("You can't divide by 0")


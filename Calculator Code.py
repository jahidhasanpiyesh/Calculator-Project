# Calculator project ?
# create input two value and one operator
print("Using Two Value And One Operator\n")
F = float(input("Enter The First Number:"))
OP = str(input("Enter The Must Use Seven Operator-[+] [-] [*] [/] [%] [**] [//] :"))
S = float(input("Enter The Second Number:"))
# Apply to condition !
# using if-elif-else Three condition
if OP == "+":
    print("Addition Value : ", F + S)
elif OP == "-":
    print("Subtraction Value :", F - S)
elif OP == "*":
    print("Multiplication Value :", F * S)
elif OP == "/":
    print("Division Value :", F / S)
elif OP == "%":
    print("Modulus Value :", F % S)
elif OP == "**":
    print("Exponentiation Value :", F ** S)
elif OP == "//":
    print("Floor division Value :", F // S)
else:
    print("Wrong Operators")

# simple project for Calculator
# call the def function ?
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Please Select Operation:\n"
      "1. add\n"
      "2. subtract\n"
      "3. multiply\n"
      "4. divide")

Select = int(input("Select Your Math Operation 1, 2, 3, 4 : "))
# input this two int type data !
s1 = int(input("Enter This First Numbers:"))
s2 = int(input("Enter This Second Numbers:"))

# used condition --if-elif-else
if Select == 1:
    print(s1, "+", s2, "=", add(s1, s2))
elif Select == 2:
    print(s1, "-", s2, "=", subtract(s1, s2))
elif Select == 3:
    print(s1, "*", s2, "=", multiply(s1, s2))
elif Select == 4:
    print(s1, "/", s2, "=", divide(s1, s2))
else:
    print("Invalid Input")

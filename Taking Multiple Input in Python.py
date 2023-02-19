#  Taking Multiple Input in Python

A = int(input("A ="))
B = int(input("B ="))

print(A + B)

x, y = input("Enter the number : ").split()
print(x,y,type(x))

x, y = [int(x) for x in input("Enter two values: ").split("")]
print("First number is {} and second number is {}".format(x, y))

x, y = input("Enter the number : ").split("-")
print(x,y)

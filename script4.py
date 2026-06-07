a=float(input("Enter first number here:- "))
operator=input("Enter the operator you want to use:- ")
b=float(input("Enter second number here:- "))
if operator == "+":
    print(a+b)
elif operator=="-":
    print(a-b)
elif operator== "*":
    print(a*b)
elif operator=="/":
    print(a/b)
elif operator=="%":
    print(a%b)  # helps us in finding the remainder
elif operator=="**":
    print(a**b)   # helps us calculate a to the power b
elif operator=="root":
    print(a**(1/b))
else:
    print("invalid operator")

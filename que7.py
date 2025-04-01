def addition(a,b):
    add=a+b
    return add

def subtraction (a,b):
    subtract=a-b
    return subtract

def multiplication(a,b):
    multiply=a*b
    return multiply

def division(a,b):
    division=a/b
    return division

def modulus(a,b):
    modulus=a%b
    return modulus

def exponent(a,b):
    exponent=a**b
    return exponent

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))

add=addition(a,b)
print(f"The add is ",add)
subtract=subtraction(a,b)
print(f"The subtract ",subtract)
multiply=multiplication(a,b)
print(f"The multiply ",multiply)
division=division(a,b)
print(f"The division ",division)
modulus=modulus(a,b)
print(f"The modulus",modulus)
exponet=exponent(a,b)
print(f"The exponent ",exponent)
def integer_value():  # Create a function
    num1 = int(input("Enter a first number: "))  # Take user input
    num2 = int(input("Enter a second number: "))  # Take another input
    division = num1 / num2  # Divide both values
    return division  # Return the result of division

division = integer_value()  # Call the function and store the result in 'division'
print("The number is", division)  # Output the result


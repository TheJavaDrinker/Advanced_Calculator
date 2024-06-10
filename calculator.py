import math

def num_not_saved_invalid():
    save_number = False
    function = None
    print("Unfortunately, as this number is undefined, you will not be able to save it.")
    numbers = input("Will we be working with 1 or 2 numbers now? ")

def num_not_saved_user():
    save_number = False
    function = None
    numbers = input("Will we be working with 1 or 2 numbers now? ")

def add_numbers(num1, num2): # Takes the two values, adds them together and returns the result
    result = num1 + num2
    return result

def subtract_numbers(num1, num2): # Takes the two values, subtracts the second value from the first and returns the result
    result = num1 - num2
    return result

def multiply_numbers(num1, num2): # Takes the two values, multiplies them together and returns the result
    result = num1 * num2
    return result

def divide_numbers(num1, num2): # Takes the two values, divides the first value by the second and returns the result
    if num2 == 0: # E.g. 1/0, 25/0, 0/0 triggers this case
        result = "Undefined, due to the fact that anything divided by 0 cannot be computed."
        return result
    else: # All other valid inputs
        result = num1 / num2
        return result
    
def raise_numbers(num1, num2): # Takes the two values, raises the first value by the second and returns the result
    result = num1 ** num2
    return result

def root_number(num1): # Takes the value, square-roots it and returns the result
    if num1 < 0: # E.g. sqrt(-1), sqrt(-5), sqrt(-0.5) triggers this case
        result = "Undefined, due to the fact that negative numbers cannot be square-rooted, as they are represented by 'i' by most mathematicians and are too complex for the realms of this calculator."
        return result
    else: # All other valid inputs
        result = math.sqrt(num1)
        return result
    
def sine_number(num1): # Takes the value and returns the sine value in radians
    result = math.sin(num1)
    return result

def cosine_number(num1): # Takes the value and returns the cosine value in radians
    result = math.cos(num1)
    return result

def tangent_number(num1): # Takes the value and returns the tangent value in radians
    result = math.tan(num1)
    return result

def greatest_common_divisor(num1, num2): # Takes the two values, determines what the highest factor each each of the numbers share and returns the result
    num1_converted = int(num1)
    num2_converted = int(num2)
    if num1_converted != num1 or num2_converted != num2: # E.g. num1 = 0.5, num2= 2.5, and num1 and num2 = 1.0000000000001 trigger this case
        result = "Undefined, as you cannot find the greatest common divisor of a decimal."
        return result
    else: # All other valid inputs
        result = math.gcd(num1_converted, num2_converted)
        return result

def lowest_common_multiple(num1, num2): # Takes the two values, determines the smallest multiple that each value has in common, and returns the result.
    num1_converted = int(num1)
    num2_converted = int(num2)
    if num1_converted != num1 or num2_converted != num2:
        result = "Undefined, as you cannot find the lowest common multiple of a decimal."
        return result
    else: # All other valid inputs
        result = math.lcm(num1_converted, num2_converted)
        return result

def percentage_value(num1): # Takes the value, finds the percent value (divided by a hundred) and returns the result
    result = num1/100
    return result

def permille_value(num1): # Takes the value, finds the permille value (divided by a thousand) and returns the result
    result = num1/1000
    return result

def basis_point_value(num1): # Takes the value, finds the basis-point value (divided by ten thousand) and returns the result
    result = num1/10000
    return result

def parts_per_cent_mille(num1): # Takes the value, finds the parts-per-cent-mille value (divided by a hundred thousand) and returns the result
    result = num1/100000
    return result

def parts_per_million(num1): # Takes the value, finds the parts-per-million value (divided by a million) and returns the result
    result = num1/1000000
    return result

def natural_logarithmic_value(num1): # Takes the value, finds how many numbers would need to be multiplied to get that value (in base e) and prints the result
    if num1 == 0: # Only 0 triggers this case
        result = "Undefined, as you cannot get zero by raising anything to the power of anything else."
        return result
    elif num1 < 0: # E.g. -1, -500, -0.5 triggers this case
        result = "Undefined, as you cannot get a number that is less than zero by raising anything to the power of anything else. This is the same issue with square-rooting a negative number."
        return result
    else: # All other valid inputs
        result = math.log(num1)
        return result
    
def base_10_logarithmic_value(num1): # Takes the value, finds how many numbers would need to be multiplied to get that value (in base 10) and prints the result
    if num1 == 0: # Only 0 triggers this case
        result = "Undefined, as you cannot get zero by raising anything to the power of anything else."
        return result
    elif num1 < 0: # E.g. -1, -500, -0.5 triggers this case
        result = "Undefined, as you cannot get a number that is less than zero by raising anything to the power of anything else. This is the same issue with square-rooting a negative number."
        return result
    else: # All other valid inputs
        result = math.log10(num1)
        return result
    
def factorial_value(num1): # Takes the value, finds the factorial of that number (i.e. n * n-1 * n-2 ... * 3 * 2 * 1) and prints the result
    num1_converted = int(num1) # Rounds down all numbers to have zero decimals (i.e. be whole numbers)
    if num1_converted != num1: # E.g. 5 != 5.25 triggers this case
        result = "Undefined, as you cannot find the factorial value of a decimal number."
        return result
    else: # All other valid results
        result = math.factorial(num1_converted)
        return result


save_number = False # Condition to see if the num1 variable will be reused, is set to 'False' by default
num1 = None # First value, set to None by default
num2 = None # Second value, set to None by default
function = None # Determines what function will be performed on the number(s), set to None by default

print("Welcome to the Mk I Advanced Calculator:")
numbers = input("Will we be working with 1 or 2 numbers today? ") # Determines which equations will be available to the user
while numbers != '': # Loops indefinitely until an empty space is input
    if numbers == '1':
        if save_number == True: # Must have already completed an equation for this to be available
            print(f'Great! It appears that you have saved a number already: {num1}')
        else: # If this is the first equation, or the user didn't save the answer
            num1 = float(input("Great! What will the number be? "))
        if function == None:
            function = input("What function would you like to perform? Your options are square-root, sine, cosine, tangent, percent, permille, basis-point, pcm, ppm, base-10 logarithm, natural logarithm and factorial. ")
            while function: # Loops until a valid answer is given
                if function.lower() == "square-root":
                    print(f"The result of square-rooting {num1} is: {root_number(num1)}")
                    if root_number(num1) == "Undefined, due to the fact that negative numbers cannot be square-rooted, as they are represented by 'i' by most mathematicians and are too complex for the realms of this calculator.": # Prevents the user from saving a result that is undefined
                        num_not_saved_invalid()
                    else:
                        save_number = input('Would you like to save this result as a variable? (Y for yes, N for no) ') # Asks if the user would like to save this number as the num1 variable for the next equation
                        if save_number.upper() == "Y":
                            save_number = True # Overrides the default save_number to be True.
                            num1 = root_number(num1) # Activates the subprogram again to save the number to a single variable
                            function = None # Clears the variable prescribed by the user
                            numbers = input("Will we be working with 1 or 2 numbers now? ") # Loops back around to the start of the while loop
                        else:
                            num_not_saved_user()
                elif function.lower() == "sine":
                    print(f"The sine value of {num1} is: {sine_number(num1)} radians")
                    save_number = input('Would you like to save this result as a variable? (Y for yes, N for no) ')
                    if save_number.upper() == "Y":
                        save_number = True
                        num1 = sine_number(num1)
                        function = None
                        numbers = input("Will we be working with 1 or 2 numbers now? ")
                    else:
                        num_not_saved_user() 
                elif function.lower() == "cosine":
                    print(f"The cosine value of {num1} is: {cosine_number(num1)} radians")
                    save_number = input('Would you like to save this result as a variable? (Y for yes, N for no) ')
                    if save_number.upper() == "Y":
                        save_number = True
                        num1 = cosine_number(num1)
                        function = None
                        numbers = input("Will we be working with 1 or 2 numbers now? ")
                    else:
                        num_not_saved_user()
                elif function.lower() == "tangent":
                    print(f"The tangent value of {num1} is: {tangent_number(num1)} radians")
                    save_number = input('Would you like to save this result as a variable? (Y for yes, N for no) ')
                    if save_number.upper() == "Y":
                        save_number = True
                        num1 = tangent_number(num1)
                        function = None
                        numbers = input("Will we be working with 1 or 2 numbers now? ")
                    else:
                        num_not_saved_user()
                elif function.lower() == "percent":
                    print(f"The percent value of {num1} is: {percentage_value(num1)}")
                    save_number = input('Would you like to save this result as a variable? (Y for yes, N for no) ')
                    if save_number.upper() == "Y":
                        save_number = True
                        num1 = percentage_value(num1)
                        function = None
                        numbers = input("Will we be working with 1 or 2 numbers now? ")
                    else:
                        save_number = False
                        function = None
                        numbers = input("Will we be working with 1 or 2 numbers now? ")
                elif function.lower() == "permille":
                    print(f"The permille value of {num1} is: {permille_value(num1)}")
                    save_number = input('Would you like to save this result as a variable? (Y for yes, N for no) ')
                    if save_number.upper() == "Y":
                        save_number = True
                        num1 = permille_value(num1)
                        function = None
                        numbers = input("Will we be working with 1 or 2 numbers now? ")
                    else:
                        num_not_saved_user()
                elif function.lower() == "basis-point":
                    print(f"The basis-point value of {num1} is: {basis_point_value(num1)}")
                    save_number = input('Would you like to save this result as a variable? (Y for yes, N for no) ')
                    if save_number.upper() == "Y":
                        save_number = True
                        num1 = basis_point_value(num1)
                        function = None
                        numbers = input("Will we be working with 1 or 2 numbers now? ")
                    else:
                        num_not_saved_user()
                elif function.lower() == "pcm":
                    print(f"The parts-per-cent-mille value of {num1} is: {parts_per_cent_mille(num1)}")
                    save_number = input('Would you like to save this result as a variable? (Y for yes, N for no) ')
                    if save_number.upper() == "Y":
                        save_number = True
                        num1 = parts_per_cent_mille(num1)
                        function = None
                        numbers = input("Will we be working with 1 or 2 numbers now? ") 
                    else:
                        num_not_saved_user()
                elif function.lower() == "ppm":
                    print(f"The parts-per-million value of {num1} is: {parts_per_million(num1)}")
                    save_number = input('Would you like to save this result as a variable? (Y for yes, N for no) ')
                    if save_number.upper() == "Y":
                        save_number = True
                        num1 = parts_per_million(num1)
                        function = None
                        numbers = input("Will we be working with 1 or 2 numbers now? ")
                    else:
                        num_not_saved_user()
                elif function.lower() == "natural logarithm":
                    print(f'The natural logarithmic value of {num1} is: {natural_logarithmic_value(num1)}')
                    if natural_logarithmic_value(num1) == "Undefined, as you cannot get zero by raising anything to the power of anything else." or natural_logarithmic_value(num1) == "Undefined, as you cannot get a number that is less than zero by raising anything to the power of anything else. This is the same issue with square-rooting a negative number.":
                        num_not_saved_invalid()
                    else: 
                        save_number = input('Would you like to save this result as a variable? (Y for yes, N for no) ')
                        if save_number.upper() == "Y":
                            save_number = True
                            num1 = natural_logarithmic_value(num1)
                            function = None
                            numbers = input("Will we be working with 1 or 2 numbers now? ")
                        else:
                            num_not_saved_user()
                elif function.lower() == "base-10 logarithm":
                    print(f'The base-10 logarithmic value of {num1} is: {base_10_logarithmic_value(num1)}')
                    if base_10_logarithmic_value(num1) == "Undefined, as you cannot get zero by raising anything to the power of anything else." or base_10_logarithmic_value(num1) == "Undefined, as you cannot get a number that is less than zero by raising anything to the power of anything else. This is the same issue with square-rooting a negative number.":
                        num_not_saved_invalid()
                    else:
                        save_number = input('Would you like to save this result as a variable? (Y for yes, N for no) ')
                        if save_number.upper() == "Y":
                            save_number = True
                            num1 = base_10_logarithmic_value(num1)
                            function = None
                            numbers = input("Will we be working with 1 or 2 numbers now? ")
                        else:
                            num_not_saved_user()
                elif function.lower() == "factorial":
                    print(f'The factorial value of {num1} is: {factorial_value(num1)}')
                    if factorial_value(num1) == "Undefined, as you cannot find the factorial value of a decimal number.":
                        num_not_saved_invalid()
                    else:
                        save_number = input('Would you like to save this result as a variable? (Y for yes, N for no) ')
                        if save_number.upper() == "Y":
                            save_number = True
                            num1 = factorial_value(num1)
                            function = None
                            numbers = input("Will we be working with 1 or 2 numbers now? ")
                        else:
                            num_not_saved_user()
                    
                else:
                    print("Sorry, I don't recognise that operation.")
                    function = input("What function would you like to perform? ")

    elif numbers == '2':
        if save_number == True:
            print(f'Great! It appears that you have saved a number already: {num1}')
        else:
            num1 = float(input("Great! What will the first number be? "))
        num2 = float(input("Awesome! What will the second number be? ")) # Will always be a requirement, no matter if the result was saved or not.
        if function == None:
            function = input("What function would you like to perform? Your options are addition, subtraction, multiplication, division, raise, GCD and LCM. ")
            while function:
                if function.lower() == "addition":
                    print(f"The sum of {num1} and {num2} is: {add_numbers(num1, num2)}")
                    save_number = input('Would you like to save this result as a variable? (Y for yes, N for no) ')
                    if save_number.upper() == "Y":
                        save_number = True
                        num1 = add_numbers(num1, num2)
                        function = None
                        numbers = input("Will we be working with 1 or 2 numbers now? ")
                    else:
                        num_not_saved_user()
                elif function.lower() == "subtraction":
                    print(f"The subtraction of {num2} from {num1} is: {subtract_numbers(num1, num2)}")
                    save_number = input('Would you like to save this result as a variable? (Y for yes, N for no) ')
                    if save_number.upper() == "Y":
                        save_number = True
                        num1 = subtract_numbers(num1, num2)
                        function = None
                        numbers = input("Will we be working with 1 or 2 numbers now? ")
                    else:
                       num_not_saved_user() 
                elif function.lower() == "multiplication":
                    print(f"The multiplication of {num1} and {num2} is: {multiply_numbers(num1, num2)}")
                    save_number = input('Would you like to save this result as a variable? (Y for yes, N for no) ')
                    if save_number.upper() == "Y":
                        save_number = True
                        num1 = multiply_numbers(num1, num2)
                        function = None
                        numbers = (input("Will we be working with 1 or 2 numbers now? ")) 
                    else:
                        num_not_saved_user() 
                elif function.lower() == "division":
                    print(f"The division of {num1} by {num2} is: {divide_numbers(num1, num2)}")
                    if divide_numbers(num1, num2) == "Undefined, due to the fact that anything divided by 0 cannot be computed.":
                        num_not_saved_invalid()
                    else:
                        save_number = input('Would you like to save this result as a variable? (Y for yes, N for no) ')
                        if save_number.upper() == "Y":
                            save_number = True
                            num1 = divide_numbers(num1, num2)
                            function = None
                            numbers = input("Will we be working with 1 or 2 numbers now? ")
                        else:
                           num_not_saved_user()
                elif function.lower() == "raise":
                    print(f"The result of raising {num1} to the power of {num2} is: {raise_numbers(num1, num2)}")
                    save_number = input('Would you like to save this result as a variable? (Y for yes, N for no) ')
                    if save_number.upper() == "Y":
                        save_number = True
                        num1 = raise_numbers(num1, num2)
                        function = None
                        numbers = input("Will we be working with 1 or 2 numbers now? ")
                    else:
                        num_not_saved_user()
                elif function.lower() == "gcd":
                    print(f'The greatest common divisor of {num1} and {num2} is: {(greatest_common_divisor(num1, num2))}')
                    if greatest_common_divisor(num1, num2) == "Undefined, as you cannot find the greatest common divisor of a decimal.":
                        num_not_saved_invalid()
                    else:
                        save_number = input('Would you like to save this result as a variable? (Y for yes, N for no) ')
                        if save_number.upper() == "Y":
                            save_number = True
                            num1 = greatest_common_divisor(num1, num2)
                            function = None
                            numbers = input("Will we be working with 1 or 2 numbers now? ")
                        else:
                           num_not_saved_user()
                elif function.lower() == "lcm":
                    print(f"The lowest common multiple of {num1} and {num2} is: {lowest_common_multiple(num1)}")
                    save_number = input('Would you like to save this result as a variable? (Y for yes, N for no) ')
                    if lowest_common_multiple(num1, num2) == "Undefined, as you cannot find the lowest common multiple of a decimal.":
                        num_not_saved_invalid()
                    else:
                        if save_number.upper() == "Y":
                            save_number = True
                            num1 = lowest_common_multiple(num1, num2)
                            function = None
                            numbers = input("Will we be working with 1 or 2 numbers now? ") 
                        else:
                            num_not_saved_user()
                else:
                    print("Sorry, I don't recognise that operation.")
                    function = input("What function would you like to perform? ")

    else: # Any number greater than 2, less than 1, decimals or non-numerical characters trigger this case.
        print("Sorry, I can only take either 1 or 2 numbers.")
        numbers = input("Will we be working with 1 or 2 numbers today? ") # Gives the user another chance to input a valid value

print("You have chosen to deactivate the calculator. Thank you for using the Mk I Advanced Calculator") # Used to indicate that the program is closing
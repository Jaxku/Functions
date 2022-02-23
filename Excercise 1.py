def calculate_double(number1):
    double = number1 + number2
    return double

# Main routine
number1 = int(input("Whats the first number you want to add? "))
number2 = int(input("Whats the number you want to add with number 1? "))
answer = calculate_double(number1)
print(f"{number1} and {number2} together is {calculate_double(number1)}")

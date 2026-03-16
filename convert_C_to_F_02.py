# FILE NAME - convert_C_to_F_02.py

# NAME: Hoi I Tam
# DATE: March 12, 2026
# BRIEF DESCRIPTION: Converts a temperature from Celsius to Fahrenheit or vice versa based on user input. 

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''

########## ENTER YER CODE BELOW THIS LINE ##########

print("===== Temperature Converter =====\n")
print(" 1. Convert from Celsius to Fahrenheit")
print(" 2. Convert from Fahrenheit to Celsius\n")
choice = int(input("Please choose from the above menu: "))
temp = float(input("Enter a temperature to convert: "))

if choice == 1: 
    converted_temp = (temp * 9/5) + 32
    print(f"\n{temp} degrees Celsius is {converted_temp} degrees Fahrenheit.")
elif choice == 2:
    converted_temp = (temp - 32) * 5/9
    print(f"\n{temp} degrees Fahrenheit is {converted_temp} degrees Celsius.")
########### END YER CODE ABOVE THIS LINE ###########

'''

1. What is one lesson you learned in this lab?
I learned how to use elif statements to handle multiple condition to perform different calculations based on user input.




'''
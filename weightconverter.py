weight = int(input("Weight: ")) 
unit = input("Is your weight in Pounds (L) or Kgs (K): ")
if unit.upper() == "L":
  converted = weight * 0.45
  print(f"You are {converted} Kgs")
else:
  converted = weight / 0.45
  print(f"You are {converted} Pounds")

"""
76:32 https://www.youtube.com/watch?v=_uQrJ0TkZlc

Line 1 Ask user to input weight. So we use input function
    Weight colon: means user wil be prompted to enter weight.
    And the return value is stored in variable weight

Lin2 Ask user to specify whether weight is in Lbs or Kgs.
So we use input function again and store the return value in variable "unit"

Line3 If unit is L then convert weight in Kgs
But if user enters the value l (small L) then this program will not work
So we use dot operator and use UPPER method of string object.
This will convert whatever the user enters to upper case. So it will convert
small l to capital L

Lin4 if this condition is true use the formula

IMPORTANT - Weight is a string object and we cannot multiply string to floating point number
So we need to convert weight to numerical value.
So when we we call the input function, we can get the return value and pass it to the int function.
So, we call the int function and give it the return value of the input function. Now, the
in function will return an integer so we can store it in this weight

print(f"......") - This will print formatted string

"""

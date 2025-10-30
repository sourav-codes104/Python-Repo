value = float(input("Enter the value of temperature: "))
unit = input("Enter the current unit of temperature (C/K/F) : ").upper()
new_unit = input("Enter the unit in which you want to convert : ").upper()
ans = 0
if unit == "C" and new_unit == "K":
    ans = value + 273.15

elif unit == "C" and new_unit == "F":
    ans = (value*(9/5) + 32)

elif unit == "K" and new_unit == "F":
    ans = (value-273.15)*(9/5)+32

elif unit == "K" and new_unit == "C":
    ans = value-273.15

elif unit == "F" and new_unit == "K":
    ans = (value-32)*(5/9)+273.15

elif unit == "F" and new_unit == "C":
    ans = (value-32)*(5/9)


if ans is not None :
    print(f"After converting from {unit} to {new_unit} the temperature is : {ans} {new_unit}°")
else:
    print("Invalid unit conversion")
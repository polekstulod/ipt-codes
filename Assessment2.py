
# * Number 2
# length = eval(input("cm? "))
# if(length < 0):
#     print("entry is invalid!")
# else:
#     print(length / 2.54, "inches")

# * Number 3
# unit = input("Celsius or Fahrenheit? ")
# deg = eval(input("Enter the " + unit))
# if(unit == "Celsius"):
#     print((deg * 9 / 5) + 32, "fahrenheit")
# elif(unit == "Fahrenheit"):
#     print((deg - 32) * 5 / 9, "celsius")
# else:
#     print("Invalid input")

# * Number 4
# cel = eval(input("enter the temperature: "))
# if(cel < -263.15):
#     print("temperature is invalid")
# elif(cel == -263.15):
#     print("temperature is absolute zero")
# elif(cel > -263.15 and cel < 0):
#     print("temperature is below freezing")
# elif(cel > 0 and cel < 100):
#     print("temperature is normal")
# elif(cel == 100):
#     print("temperature is at boiling point")
# elif(cel > 100):
#     print("temperature is above boiling point")
# else:
#     print("temperature is at freezing point")

# * Number 5

# cred = int(input("Credits? "))
# if (cred <= 23):
#     print("You are a freshman")
# elif(cred >= 24 and cred <= 53):
#     print("You are a sophomore")
# elif(cred >= 54 and cred <= 83):
#     print("You are a junior")
# else:
#     print("You are a senior")


# * Number 6
# year = int(input("Year? "))

# if((not year % 100 == 0 or year % 400 == 0) and year % 4 == 0):
#     print(year, "is a leap year")  
# else:
#     print(year, "is not a leap year")

# * Number 7

# weight = -1
# while(weight < 0 ):
#     weight = eval(input("Weight? "))
# print(weight * 2.20462262185, "pounds")

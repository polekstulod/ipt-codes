print("Output")
# * Number 5
# ? Write a function for checking the speed of drivers. This function should have one parameter: speed.

# def speed_check(speed):
#     print("speed:", speed)
#     if speed < 70:
#         print("Ok")
#     else:
#         dem = int((speed - 70) // 5)
#         if dem <= 12:
#             print("Points:", dem)
#         else:
#             print("License Suspended!")

# speed_check(65)
# speed_check(140)
# speed_check(85)

# * Number 6
# ? Write a function called rectangle that takes two integers m and n as arguments and prints out an m × n box consisting of asterisks.

# def rectange(m, n):
#     for _ in range(m):
#         for _ in range(n):
#             print("*", end="")
#         print()
#     print()

# rectange(5,10)
# rectange(2, 5)

# * Number 7
# ? Write a function called number_of_factors that takes an integer and returns how many factors the number has

# def number_of_factors(num):
#     factors = 0
#     for i in range(1, num + 1):
#         if(num % i == 0):
#             factors += 1
#     print("Total numbers of factors of", num, end=": ")
#     return factors

# print(number_of_factors(45))
# print(number_of_factors(73))

# * Number 8
# ? Write a function called factors that takes an integer and returns a list of its factor.

# def factor_list(num):
#     factors = str(num) + " factors are: "
#     for i in range(1, num + 1):
#         if(num % i == 0):
#             factors += "(" + str(i) + ")"
#     return factors

# print(factor_list(45))
# print(factor_list(73))

# * Number 9a
# ? (a) Write a function called primes that is given a number n and returns a list of the first n primes. Let the default value of n be 100.

# def prime_num(num = 100):
#     primes = "first " + str(num) + " prime numbers are: "
#     i = 2
#     count = 0
#     while True:
#         factors = 0
#         for j in range(1, i + 1):
#             if(i % j == 0):
#                 factors += 1
#         if(factors <= 2):
#             primes += "(" + str(i) + ")"
#             count += 1
#         i += 1
#         if(count >= num):
#             break     
#     return primes
            
# print(prime_num(20))
# print(prime_num())

# * Number 9b
# ? (b) Modify the function above so that there is an optional argument called start that allows the list to start at a value other than 2. The function should return the first n primes that are greater than or equal to start. The default value of start should be 2.

# def prime_num(num = 100, start = 2):
#     primes = "first " + str(num) + " prime numbers from " + str(start) + " are: "
#     i = start
#     count = 0
#     while True:
#         factors = 0
#         for j in range(1, i + 1):
#             if(i % j == 0):
#                 factors += 1
#         if(factors <= 2):
#             primes += "(" + str(i) + ")"
#             count += 1
#         i += 1
#         if(count >= num):
#             break      
#     return primes

# print(prime_num(10, 100))
# print(prime_num())
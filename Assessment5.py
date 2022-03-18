
# * Number 1
# num = [1, 2, 3]
# num_sq = []
# for i in num:
#     num_sq.append((i, i**2))
    
# print(num_sq)


# * Number 2
# def divisible(x, y):
#     if x % y == 0:
#         return True
#     else:
#         return False
    
# size = int(input("Enter number of integers: "))
# lis = []
# for i in range(size):
#     lis.append(int(input("Enter an integer: ")))
# K = int(input("Enter the 'K' value: "))
# tup = tuple(lis)
# for i in tup:
#     if divisible(i, K):
#         print(i, end=" ")


# * Number 3
# days = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31, 'August':31,  'September':30, 'October':31, 'November':30, 'December':31}
# #a
# print(days.get(str(input("Enter a month name: "))), "days")
# #b
# for i in sorted(days.keys()):
#     print(i)
# #c
# for i, j in days.items():
#     if(j == 31):
#         print(i)
# #d
# for i in sorted(days, key=days.get):
#     print(i, days[i])


# * Number 4
# products = {}
# while True:
#     product = input("Enter the product name: ")
#     price = input("Enter product price: ")
#     products[product] = price
#     if(int(input("1 to continue, 0 to end input: ")) == 0):
#         break

# print("======================")

# while True:
#     pname = input("Enter a product name: ")
#     if(products.get(pname) == None):
#         print("The product does not exist!")
#     else:
#         print(products[pname])
#     if(int(input("1 to continue, 0 to end input: ")) == 0):
#         break


# * Number 5

# account = {"jiwon": "eu123",
#            "sihyeon": "flower05",
#            "eunji": "miaAce",
#            "serim": "0ndaaaaa",
#            "yoorim": "yoorimie",
#            "yiren": "ireon29",
#            "ldh_sky": "muhyod",
#            "doItRight": "allTheNight96",
#            "whatYouLike": "GiveItToMe",
#            "laLaLaLA": "YEaaaaahhh"}

# userName = input("Enter your username: ")
# if(account.get(userName) == None):
#     print("You are not a valid user!")
# else:
#     passWord = input("Enter your password: ")
#     if account.get(userName) == passWord:
#         print("You're now logged in to the system!")
#     else:
#         print("Incorrect password")

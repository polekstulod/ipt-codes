print("-----Output-----")

# * Number 1 answers
# a. [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# b. [1, 2, 3, 4, 5, 11, 12, 13, 14, 15]
# c. TypeError
# d. 2
# e. 1
# f. 5
# g. [1, 2, 3, 4, 5]
# h. [3, 4]
# i. [2, 4] 
# j. [1, 2]
# k. [1, 3, 5]


# * Number 2
items = []
def num2(items):
    items.append(67)
    items.append(62.9)
    items.append("hi")
    items.append(False)
    items += [8]
    items += [67]
    items += ['apple']
    items += [6.5]
    print(items)


# * Number 3
def num3(items):
    num2(items)
    items.append("banana")
    items.append(67)
    items.insert(3, "dog")
    items.insert(0, 909)
    print(items.index("hi"))
    print(items.count(67))
    items.remove(67)
    items.pop(items.index(False))
    print(items)


# * Number 4
def num4():
    items = []
    for _ in range(int(input("size of list: "))):
        items.append(int(input("enter an integer: ")))
    print(items)
    print(sum(items))
    print(items[-1])
    items.reverse()
    print(items)
    print("Yes") if 5 in items else print("No")
    count = 0
    for j in items:
        if(j < 5): count += 1
    print(count)
    del items[0:len(items):len(items)-1]
    items.sort()
    print(items)


# * Number 5
def num5():
    num = [8, 9, 10]
    num[1] = 17
    num.extend([4, 5, 6])
    num.pop(0)
    num.sort()
    num = num * 2
    num.insert(3, 25)
    print(num)


# * Number 6
def num6():
    def list_of_integers(num):
        factor_list = []
        for i in range(1, num + 1):
            if(num % i == 0): factor_list.append(i) 
        return factor_list
    
    print(list_of_integers(int(input("Enter an integer: "))))


# * Number 7
def num7():
    def remove_repeated(repeated_list):
        new_list = []
        for i in repeated_list:
            if i not in new_list:
                new_list.append(i)
        return new_list
    print(remove_repeated([1, 1, 2, 3, 4, 3, 0, 0]))
    
    
# * Testing
# num2(items)
# num3(items)
# num4()
# num5()
# num6()
# num7()

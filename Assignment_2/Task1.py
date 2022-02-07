#The algorithm takes as input a list of numbers which may contain duplicates.
# It returns true if all elements of the list occur an odd number of times.
# Otherwise it returns false
def checkduplicates():
    user_input = input("Please enter items in the list ")
    list1 = user_input.split(" ")
    even = []
    odd = []
    for element in list1:
        if int(list1.count(element)) % 2 == 0:
            even.append(element)
            if len(even) > 0:
               return False
        else:
            return True


print(checkduplicates())


#The time complexity is 0(n)




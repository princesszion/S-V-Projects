#The algorithm takes as input a list of numbers which may contain duplicates.
# It returns true if all elements of the list occur an odd number of times.
# Otherwise it returns false
def checkduplicates():
    #Getting yer input
    user_input = input("Please enter items in the list ")
    #Divide a string(user_input) into a list
    list1 = user_input.split(" ")
    even_number = []
    for element in (list1):
        if int(list1.count(element)) % 2 == 0 and element not in even_number:
            even_number.append(element)
    if len(even_number) > 0:
        # print(even_number)
        return  False
    else:
        return True
        # print("Odd numbers")




print(checkduplicates())


#The time complexity is 0(n)




#The algorithm takes as input a list of numbers which may contain duplicates.
# It returns true if all elements of the list occur an odd number of times.
# Otherwise it returns false
def check_duplicates():
    # Getting yer input
    user_input = input("Please enter items in the list ")
    # Divide a string(user_input) into a list
    list1 = user_input.split(" ")
    # Initialising a lists that will store the numbers that occurs an even number of times, if there's one.
    even_number = []
    for element in (list1):
        # Check to see if a number has occurred an even number of times.
        if int(list1.count(element)) % 2 == 0 and element not in even_number:
            even_number.append(element)
    # Check if there's an element that was store in the even number lists.
    if len(even_number) > 0:
        return False
    else:
        return True

print(check_duplicates())


# The time complexity for this algorithm is 0(n).




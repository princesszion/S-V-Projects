#Finding the maximum value of a list of numbers
def getmax(ListsNumbers):
    #ListsNumbers = [4, 56, 48, 200, 4, 2, 7, 4, 20, 34, 29]
    maxNumber = max(ListsNumbers)
    print('The maximum number in the lists is: ' + str(maxNumber))
    return maxNumber


def lowercase(string):
    # Randomly generating a string and coverting it to lowercase
    import random
    import string

    output_string = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(20))
    new_string = output_string.lower()
    print("The randomly generated string is: " + output_string)
    print("The string converted to lower case is: " + new_string)

def sort_intergers():
    # Sorting list if integers in ascending order
    ListsNumbers = [4, 56, 48, 200, 4, 2, 7, 4, 20, 34, 29]
    ListsNumbers.sort()
    print("The sorted list in ascending order is: " + str(ListsNumbers))

    # Sorting list if integers in descending order
    ListsNumbers = [4, 56, 48, 200, 4, 2, 7, 4, 20, 34, 29]
    ListsNumbers.sort(reverse=True)
    print("The sorted list in descending order is: " + str(ListsNumbers))



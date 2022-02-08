# Design and implement an algorithm that takes:
# a list containing n distinct natural numbers and a number k ≤ n
# and calculates the sum of the k largest numbers in the array.

def check_duplicates():
    user_input = input("Enter a lists of distinct natural numbers: ")
    natural_numbers = user_input.split(" ")
    #convert the user input to distinct natural numbers with no duplicates.
    distinct_numbers = list(set(natural_numbers))
    return distinct_numbers, get_k(distinct_numbers)

def get_k(distinct_numbers):
    input_k = int(input('Enter an integer k less than or equal to the length of list: '))
    # Making sure that k is less than the length of the list.
    if int(input_k) > len(distinct_numbers):
        print("k should be less than or equal to the length of list")
        return get_k(distinct_numbers)
    else:
         return input_k, distinct_numbers, sum_largest_numbers(distinct_numbers, input_k)

def sum_largest_numbers(distinct_numbers, input_k):
    distinct_numbers = [int(i) for i in distinct_numbers]
    print("The distinct lists is: " +str(distinct_numbers))
    # Sorting the lists
    distinct_numbers.sort(reverse=True)
    print("The sorted list in descending order is: " +str(distinct_numbers))
    sum_the_numbers = sum(distinct_numbers[0:input_k])
    print("The sum of the highest k numbers: " +str(sum_the_numbers))

check_duplicates()


# A Dynamic Programming based Python
# Program for 0-1 Knapsack problem
# Returns the maximum value that can
# be put in a knapsack of capacity W


# def knapSack(items, capcity):

def knapsack(weights, weightsValues, capacity):
    in_sack = len(weightsValues)  # number of gold pellets to carry
    arrayPellets = []

    # creates a 2 dimensional array initially with 0
    table = [[0 for x in range(capacity + 1)] for x in range(in_sack + 1)]

    # loops to fill the table with in_sack of all possible combination of the items with respect to maximum capacity
    for i in range(1, in_sack + 1):
        for j in range(capacity + 1):
            if weights[i - 1] <= j:
                table[i][j] = max(table[i - 1][j], weightsValues[i - 1] +
                                  table[i - 1][j - weights[i - 1]])
            else:
                table[i][j] = table[i - 1][j]

    print(f"Maximum value: ${table[in_sack][capacity]}")

    # iterates through the table decing whether to include the item or not
    while in_sack != 0:
        if table[in_sack][capacity] != table[in_sack - 1][capacity]:
            arrayPellets.append(weights[in_sack - 1])
            capacity = capacity - weights[in_sack - 1]
        in_sack -= 1

    print(f"Weights chosen: {arrayPellets}")


# Given example of Knaspack problem
val = [2500, 1700, 1200, 3000, 4100, 2000, 7000, 7500]
weights = [5, 3, 1, 6, 8, 4, 11, 12]
capacity = 20

knapsack(weights, val, capacity)



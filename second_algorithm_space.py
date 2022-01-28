from memory_profiler import memory_usage
import matplotlib.pyplot as plt

import string
import random


# def spaceplot(inputs):
#     input_size = []
#     input_space = []
#     for i in range(0, len(inputs)):
#
#         max(inputs[i])
#         space = memory_usage()
#         input_size.append(len(inputs[i]))
#         print(inputs[i])
#         input_space.append(space[0])
#
#
#     print(input_space)
#     plt.plot(input_size, input_space)
#     plt.show()
#
# spaceplot([[1, 5], [12, 65, 24, 98, 45],
#         [8,  65, 45],[12, 65, 24, 98, 45,  13, 23, 56, 78, 12, 65, 24, 98, 100, 45, 12, 65, 24,  13, 23, 56, 78, 12, 65, 24, 98, 100, 45, 12, 65, 24,  13, 23, 56, 78, 12, 65, 24, 98, 100, 45, 12, 65, 24,  13, 23, 56, 78, 12, 65, 24, 98, 100, 45, 12, 65, 24,  13, 23, 56, 78, 12, 65, 24, 98, 100, 45, 12, 65, 24]])
#

def spaceplot():
    input_space = []
    input_size = []
    i = 0
    while i < 3:

        input_strings = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(20))
        i += 1
        input_size.append(input_strings)
        # print(input_strings)
        output_strings = input_strings.lower()
        space = memory_usage()
        input_space.append(space[0])
    print(len(input_size))

    print(input_space)
    plt.plot(input_size, input_space)
    plt.show()


spaceplot()

# from memory_profiler import memory_usage
# import matplotlib.pyplot as plt
#
#
#
# def spaceplot(inputs):
#     input_size = []
#     input_space = []
#     for i in range(0, len(inputs)):
#
#         max(inputs[i])
#         space = memory_usage()
#         input_size.append(len(inputs[i]))
#         print(inputs[i])
#         input_space.append(space[0])
#
#
#     print(input_space)
#     plt.plot(input_size, input_space)
#     plt.show()
#
# spaceplot([[1, 5], [12, 65, 24, 98, 45],
#         [8,  65, 45],[12, 65, 24, 98, 45,  13, 23, 56, 78, 12, 65, 24, 98, 100, 45, 12, 65, 24,  13, 23, 56, 78, 12, 65, 24, 98, 100, 45, 12, 65, 24,  13, 23, 56, 78, 12, 65, 24, 98, 100, 45, 12, 65, 24,  13, 23, 56, 78, 12, 65, 24, 98, 100, 45, 12, 65, 24,  13, 23, 56, 78, 12, 65, 24, 98, 100, 45, 12, 65, 24]])
#

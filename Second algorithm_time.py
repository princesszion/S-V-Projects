import string
import time
import matplotlib.pyplot as plt
import random
def values():
    input_time = []
    input_size = []
    i = 0
    while i < 3:

        input_strings = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(20))
        i += 1
        Start_time = time.time()
        input_size.append(input_strings)
        # print(input_strings)
        output_strings = input_strings.lower()
        End_time = time.time()
        total_time = End_time - Start_time
        input_time.append(total_time)
        # print(output_strings)
    print(len(input_size))



    print(len(input_time))

    plt.plot(input_size,input_time)
    plt.show()

#values([[1,5],[12,65,24,98,45,24,98,45],[67,98,46,13,23,56,78,12,65,24,98,100,45,12,65,24,98,100,45]])
values()
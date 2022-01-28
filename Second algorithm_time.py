import string
import time
import matplotlib.pyplot as plt
import random
def values():
    input_time = []
    input_size = []
    i = 0
    while i < 1:
        input_string1 = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(20))
        input_string2 = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))
        input_string3 = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(100))
        i += 1
        Start_time = time.time()
        input_size.append(len(input_string1))
        input_size.append(len(input_string2))
        input_size.append(len(input_string3))
        print(input_size)
        for x in range (0,len(input_size)):

            output_string1 = input_string1.lower()
            output_string2 = input_string2.lower()
            output_string3 = input_string3.lower()
            End_time = time.time()
            total_time = End_time - Start_time
            input_time.append(total_time)
            print(total_time)

    print(len(input_time))

    plt.plot(input_time,input_size)
    plt.show()

#values([[1,5],[12,65,24,98,45,24,98,45],[67,98,46,13,23,56,78,12,65,24,98,100,45,12,65,24,98,100,45,12,65,24,98,45,24,98,45,12,65,24,98,45,24,98,45, 12,65,24,98,45,24,98,45]])
values()
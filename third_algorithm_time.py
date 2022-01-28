#plot graph showing how the time and space taken as the input size changes from length 1 to length 100.
import time
import matplotlib.pyplot as plt


def timeplot3(inputs):
    input_time = []
    input_size = []
    for i in range(0, len(inputs)):
        input_size.append(len(inputs[i]))
        Start_time = time.time()
        (inputs[i]).sort()
        (inputs[i]).sort(reverse=True)
        End_time = time.time()
        total_time = End_time - Start_time
        input_time.append(total_time)
        print('The total time: ' +str(total_time))

    plt.plot(input_time, input_size)
    plt.show()



timeplot3([[1, 5], [12, 65, 24, 98, 45, 24, 98, 45],
        [67, 98, 46, 13, 23, 56, 78, 12, 65, 24, 98, 100, 45, 12, 65, 24, 98, 100, 45]])

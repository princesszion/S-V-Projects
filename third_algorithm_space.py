from memory_profiler import memory_usage
import matplotlib.pyplot as plt


def timeplot3(inputs):
    input_space = []
    input_size = []
    for i in range(0, len(inputs)):
        (inputs[i]).sort()
        (inputs[i]).sort(reverse=True)
        space = memory_usage()
        input_size.append(len(inputs[i]))
        input_space.append(space[0])
        print(input_space)

    plt.plot(input_space, input_size)
    plt.show()



timeplot3([[1, 5], [12, 65, 24, 98, 45, 24, 98, 45],
        [67, 98, 46, 13, 23, 56, 78, 12, 65, 24, 98, 100, 45, 12, 65, 24, 98, 100, 45]])

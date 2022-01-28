#plot graph showing how the time and space taken as the input size changes from length 1 to length 100.



def spaceplot(inputs):
    input_size = []
    input_space = []
    for i in range(0, len(inputs)):

        max(inputs[i])
        space = memory_usage()
        input_size.append(len(inputs[i]))
        print(inputs[i])
        input_space.append(space[0])


    print('The memery_space is ' +str(input_space))
    plt.plot(input_size, input_space)
    plt.show()

spaceplot([[1, 5], [12, 65, 24, 98, 45],
        [8,  65, 45],[12, 65, 24, 98, 45,  13, 23, 56, 78, 12, 65, 24, 98, 100, 45, 12, 65, 24,  13, 23, 56, 78, 12, 65, 24, 98, 100, 45, 12, 65, 24,  13, 23, 56, 78, 12, 65, 24, 98, 100, 45, 12, 65, 24,  13, 23, 56, 78, 12, 65, 24, 98, 100, 45, 12, 65, 24,  13, 23, 56, 78, 12, 65, 24, 98, 100, 45, 12, 65, 24]])
from memory_profiler import memory_usage
import matplotlib.pyplot as plt




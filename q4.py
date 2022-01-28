import time
import matplotlib.pyplot as plt
def values(inputs):
    input_time = []
    input_size = []
    for i in range(0,len(inputs)):
        input_size.append(len(inputs[i]))
        Start_time = time.time()
        max(inputs[i])
        End_time = time.time()
        total_time = End_time - Start_time
        input_time.append(total_time)
        print(total_time)

    #plt.plot(input_time,input_size)
    #plt.show()

values([[1,5],[12,65,24,98,45,24,98,45],[67,98,46,13,23,56,78,12,65,24,98,100,45,12,65,24,98,100,45]])



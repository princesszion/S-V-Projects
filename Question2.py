from memory_profiler import memory_usage
from line_profiler import LineProfiler
import random


def main_func():

    arr1 = [random.randint(1,5) for i in range(100000)]
    arr2 = [random.randint(1,5) for i in range(100000)]
    arr3 = [arr1[i]+arr2[i] for i in range(100000)]
    del arr1
    del arr2
    tot = sum(arr3)
    space = memory_usage()
    del arr3
    print(tot)
    print(space)
main_func()



# if __name__ == "__main__":
#     main_func()
    
    # Run the command " python -m memory_profiler Question2.py" on the terminal
    # to see the space complexity analysis.
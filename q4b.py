from memory_profiler import memory_usage




def spaceplot(inputs):
    input_size = []
    input_space = []
    for i in range(0, len(inputs)):
        input_size.append(len(inputs[i]))
        print(inputs[i])
        max(inputs[i])
        space = memory_usage()
        input_space.append(space)

    print(input_space)

spaceplot([[1, 5], [12, 65, 24, 98, 45],
        [8,  65, 45],[12, 65, 24, 98, 45,  13, 23, 56, 78, 12, 65, 24, 98, 100, 45, 12, 65, 24,  13, 23, 56, 78, 12, 65, 24, 98, 100, 45, 12, 65, 24,  13, 23, 56, 78, 12, 65, 24, 98, 100, 45, 12, 65, 24,  13, 23, 56, 78, 12, 65, 24, 98, 100, 45, 12, 65, 24,  13, 23, 56, 78, 12, 65, 24, 98, 100, 45, 12, 65, 24]])


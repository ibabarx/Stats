def manhattan_distance(vector_1,vector_2):
    list_1 = list(vector_1)
    list_2 = list(vector_2)
    absolute_difference = [abs(list_1[index] - list_2[index]) for index in range(len(list_1))]
    manhattan_distance = sum(absolute_difference)
    print("Manhattan Distance : " + str(manhattan_distance))

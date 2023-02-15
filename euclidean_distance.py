def euclidean_distance(vector_1,vector_2):
    list_1 = list(vector_1)
    list_2 = list(vector_2)
    difference_squared = [(list_1[index] - list_2[index])**2 for index in range(len(list_1))]
    euclidean_distance = sum(difference_squared) ** 0.5
    print("Euclidean Distance : " + str(euclidean_distance))

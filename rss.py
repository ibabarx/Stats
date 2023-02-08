def rss(observed,predicted):
    dictionary = {}
    list_observed = observed.tolist()
    list_predicted = predicted.tolist()
    residue_squared = []
    for index in range(len(list_observed)):
        residue_squared.append((observed[index] - predicted[index])**2)
    dictionary['observed'] = list_observed
    dictionary['predicted'] = list_predicted
    dictionary['residue_squared'] = residue_squared
    print(pd.DataFrame(dictionary))
    print("RSS : " + str(sum(residue_squared)))

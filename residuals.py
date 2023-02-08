def residuals(observed,predicted):
    dictionary = {}
    list_observed = observed.tolist()
    list_predicted = predicted.tolist()
    residuals = []
    for index in range(len(list_observed)):
        residuals.append(observed[index] - predicted[index])
    dictionary['observed'] = list_observed
    dictionary['predicted'] = list_predicted
    dictionary['residuals'] = residuals
    print(pd.DataFrame(dictionary))

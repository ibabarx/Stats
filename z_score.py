def z_score(dataframe,features):
    
    def mean(feature_list):
        sigma = sum(feature_list)
        n = len(feature_list)
        mean = sigma / n
        return mean
    
    def standard_deviation(feature_list,mean):
        deviation = [(record - mean)**2 for record in feature_list]
        deviation = sum(deviation)
        denominator = len(feature_list) - 1
        standard_deviation = (deviation / denominator)**0.5
        return standard_deviation
    
    z_scores_dictionary = {}
    
    for feature in features:
        mean = mean(list(dataframe[feature]))
        standard_deviation = standard_deviation(list(dataframe[feature]),mean)
        z_scores = [(record - mean)/standard_deviation for record in list(dataframe[feature])]
        z_scores_dictionary[feature] = z_scores
    print(pd.DataFrame.from_dict(z_scores_dictionary))

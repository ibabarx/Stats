def pearson_correlation_coefficient(x1,x2):
    
    def mean(feature_list):
        sigma = sum(feature_list)
        n = len(feature_list)
        mean = sigma / n
        return mean
    
    def standard_deviation(feature,mean):
        deviation = [(record - mean)**2 for record in feature]
        deviation = sum(deviation)
        denominator = len(feature) - 1
        standard_deviation = (deviation / denominator)**0.5
        return standard_deviation
    
    x1_list = x1.tolist()
    x2_list = x2.tolist()
    
    x1_mean = mean(x1_list)
    x2_mean = mean(x2_list)
    
    x1_standard_deviation = standard_deviation(x1_list,x1_mean)
    x2_standard_deviation = standard_deviation(x2_list,x2_mean)
    
    numerator = sum([(x1_list[index]-x1_mean)*(x2_list[index]-x2_mean) for index in range(len(x1_list))])
    denominator = (len(x1_list) - 1) * x1_standard_deviation * x2_standard_deviation
    
    pearson_correlation_coefficient = numerator / denominator
    print("pearson's correlation coefficient : " + str(pearson_correlation_coefficient))

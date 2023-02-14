def covariance(x1,x2):
    
    def mean(feature_list):
        sigma = sum(feature_list)
        n = len(feature_list)
        mean = sigma / n
        return mean
    
    x1_list = x1.tolist()
    x2_list = x2.tolist()
    
    x1_mean = mean(x1_list)
    x2_mean = mean(x2_list)
    
    numerator = sum([(x1_list[index]-x1_mean)*(x2_list[index]-x2_mean) for index in range(len(x1_list))])
    denominator = len(x1_list) - 1
    
    covariance = numerator / denominator
    print("Covariance : " + str(covariance))

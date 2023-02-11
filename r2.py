def r_squared(observed,predicted,p=1):
    
    observed_list = observed.tolist()
    predicted_list = predicted.tolist()
    n = len(observed_list)
    mean = sum(observed_list)/n
    
    obs_pred_diff = [(observed_list[index] - predicted_list[index])**2 for index in range(n)]
    obs_mean_diff = [(observed_list[index] - mean)**2 for index in range(n)]
    
    r_squared = 1-(sum(obs_pred_diff)/sum(obs_mean_diff))
    print('R-Squared score : ' + str(r_squared))

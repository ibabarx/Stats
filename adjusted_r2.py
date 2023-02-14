# FORMULA
# 1 − (1 − R^2)( n − 1 / n − P − 1 )

def ajdusted_rSquared(observed,predicted,p=1):
    
    '''
    observed = pass the column that contains the observed output values y. Format : Dataframe[y]
    predicted = pass the column that contains the predicted output values Y. Format : Dataframe[Y]
    p = number of parameters that were used to train the model and predict the values.
        default : 1
    '''   
    
    def r_squared(observed,predicted):          # An inner function that computes and returns R-square score of the model and the number of observations.
        observed_list = observed.tolist()
        predicted_list = predicted.tolist()
        n = len(observed_list)
        mean = sum(observed_list)/n
        obs_pred_diff = [(observed_list[index] - predicted_list[index])**2 for index in range(n)]
        obs_mean_diff = [(observed_list[index] - mean)**2 for index in range(n)]
        r_squared = 1-(sum(obs_pred_diff)/sum(obs_mean_diff))
        return n,r_squared          # Returns n(number of observations) & r_squared(R-square score)
    
    n,r_squared = r_squared(observed,predicted)
    adjusted_rSquare = 1-(1-r_squared)*((n-1)/(n-p-1))          # Calculating adjusted R-square score
    
    print("R2 Score : " + str(r_squared))           # print R_square score
    print("Adjusted R2 Score : " + str(adjusted_rSquare))           # print adjusted R_square score

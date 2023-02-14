# FORMULA
# 1 − (1 − R^2)( n − 1 / n − P − 1 )

def ajdusted_rSquared(observed,predicted,p=5):
    def r_squared(observed,predicted):
        observed_list = observed.tolist()
        predicted_list = predicted.tolist()
        n = len(observed_list)
        mean = sum(observed_list)/n
        obs_pred_diff = [(observed_list[index] - predicted_list[index])**2 for index in range(n)]
        obs_mean_diff = [(observed_list[index] - mean)**2 for index in range(n)]
        r_squared = 1-(sum(obs_pred_diff)/sum(obs_mean_diff))
        return n,r_squared
    n,r_squared = r_squared(observed,predicted)
    adjusted_rSquare = 1-(1-r_squared)*((n-1)/(n-p-1))
    print("R2 Score : " + str(r_squared))
    print("Adjusted R2 Score : " + str(adjusted_rSquare))

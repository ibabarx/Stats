# FORMULA
# AIC = 2P + n log(RSS/n)

def AIC(observed,predicted,p):
    
    '''
    observed = pass the column that contains the observed output values y. Format : Dataframe[y]
    predicted = pass the column that contains the predicted output values Y. Format : Dataframe[Y]
    p = number of parameters that were used to train the model and predict the values.
        default : 1
    ''' 
    
    import math         # Import python in-built library MATH,to use log function 
    n = len(observed.tolist())          # compute number of records
    
    def rss(observed,predicted):            # Inner-Function to calculate RSS
        list_observed = observed.tolist()
        list_predicted = predicted.tolist()
        residue_squared = []
        for index in range(len(list_observed)):
            residue_squared.append((observed[index] - predicted[index])**2)
        rss = sum(residue_squared)
        return rss          # Return RSS
    
    rss = rss(observed,predicted)
    AIC = (2*p)+(n*math.log(rss/n))         # Calculating AIC
    print("AIC : " + str(AIC))

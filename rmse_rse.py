def rss(observed,predicted,p=1,metric='rmse'):
    
    residue_squared = []
    rows = observed.shape[0]
    for index in range(observed.shape[0]):
        residue_squared.append((observed[index] - predicted[index])**2)
    residue_squared_sum = sum(residue_squared)
    rmse = (residue_squared_sum / rows)**0.5
    if metric == 'rmse':
        print("RMSE : " + str(rmse))
    elif metric == 'rse':
        rse = (residue_squared_sum / (rows-p-1))**0.5
        print("RSE : " + str(rse))
    else:
        print("WRONG METRIC")

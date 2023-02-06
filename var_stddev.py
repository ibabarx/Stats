def var_std(dataframe,columns='all',decimal_points=2,var=True,stddev=False):
    
    list_of_int_columns = list(dataframe.select_dtypes(include=['int64','float64']).columns)
    
    def mean_func(column,decimal_points=2):        
        mean = sum(column) / len(column)
        return mean
    
    if columns == 'all':
        
        for column in list_of_int_columns:
            mean = mean_func(dataframe[column])
            deviation = [(example - mean)**2 for example in dataframe[column]]
            deviation = sum(deviation)
            denom = len(dataframe[column]-1)
            
            if var == True:
                print("Variance of " + column + " = " + str(deviation/denom))
            if stddev == True:
                print("Standard Deviation of " + column + " = " + str((deviation/denom)**0.5))

    else:
        
        for column in columns:
            mean = mean_func(dataframe[column])
            deviation = [(example - mean)**2 for example in dataframe[column]]
            deviation = sum(deviation)
            denom = len(dataframe[column]-1)
            
            if var == True:
                print("Variance of " + column + " = " + str(deviation/denom))
            if stddev == True:
                print("Standard Deviation of " + column + " = " + str((deviation/denom)**0.5))

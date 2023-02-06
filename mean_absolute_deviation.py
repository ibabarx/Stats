def mean_absolute_deviation(dataframe,columns='all',decimal_points=2):
    list_of_int_columns = list(dataframe.select_dtypes(include=['int64','float64']).columns)
    def mean_func(column,decimal_points=2):        
        mean = sum(column) / len(column)
        return mean
    
    if columns == 'all':
        for column in list_of_int_columns:
            mean = mean_func(dataframe[column])
            deviation = [abs(example - mean) for example in dataframe[column]]
            deviation = sum(deviation)
            print("MAD of " + column + " = " + str(deviation/len(dataframe[column])))
    else:
        for column in columns:
            mean = mean_func(dataframe[column])
            deviation = [abs(example - mean) for example in dataframe[column]]
            deviation = sum(deviation)
            print("MAD of " + column + " = " + str(deviation/len(dataframe[column])))

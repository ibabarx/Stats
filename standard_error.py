def standard_error(dataframe,columns='all'):
            
    def standard_deviation(column):
        mean = sum(column) / column.shape[0]
        deviation = [(example - mean)**2 for example in column]
        deviation = sum(deviation)
        denom = len(column)-1
        standard_deviation = (deviation/denom)**0.5
        return standard_deviation
    
    list_of_int_columns = list(dataframe.select_dtypes(include=['int64','float64']).columns)
    
    if columns=='all':
        for column in list_of_int_columns:
            n = len(dataframe[column])
            s = standard_deviation(dataframe[column])
            std_error = s/(n**0.5)
            print(std_error)
    else:
        for column in columns:
            n = len(dataframe[column])
            s = standard_deviation(dataframe[column])
            std_error = s/(n**0.5)
            print(std_error)

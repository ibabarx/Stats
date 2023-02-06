def median_absolute_deviation(dataframe,columns='all',decimal_points=2):
    list_of_int_columns = list(dataframe.select_dtypes(include=['int64','float64']).columns)
    
    def median_func(column,decimal_points=2):
        size = len(column)
        if size%2==1:
            if type(column) == 'pandas.core.series.Series':
                sol = sorted(column.tolist())[((size+1)//2)]
                return sol
            else:
                sol = sorted(column)[((size+1)//2)]
                return sol
        else:
            if type(column) == 'pandas.core.series.Series':
                sol = sorted(column.tolist())[((size+1)//2)]
                return sol
            else:
                sol = sorted(column)[((size+1)//2)]
                return sol
    
    if columns == 'all':
        for column in list_of_int_columns:
            median = median_func(dataframe[column])
            median_absolute_deviation = [abs(example - median) for example in dataframe[column]]
            mad = median_func(median_absolute_deviation)
            print("Mean Absolute Deviation of " + column + " = " + str(mad))

    else:
        for column in columns:
            median = median_func(dataframe[column])
            median_absolute_deviation = [abs(example - median) for example in dataframe[column]]
            mad = median_func(median_absolute_deviation) 
            print("Mean Absolute Deviation of " + column + " = " + str(mad))

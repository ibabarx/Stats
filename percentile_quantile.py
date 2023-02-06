def percentile(dataframe,percentiles,columns='all'):
    list_of_int_columns = list(dataframe.select_dtypes(include=['int64','float64']).columns)
    
    def sorting(column):
        if type(column) == 'pandas.core.series.Series':
            sorted_list = sorted(column.tolist())
            return sorted_list
        else:
            sorted_list = sorted(column)
            return sorted_list
        
    if columns == 'all':
        for column in list_of_int_columns:
            sorted_list = sorting(dataframe[column])
            for percentile in percentiles:
                index = round(len(sorted_list)*(percentile/100))-1
                print("The " + str(percentile) + "th Percentile of " + column + " is " + str(sorted_list[index]))
    else:
        for column in columns:
            sorted_list = sorting(dataframe[column])
            for percentile in percentiles:
                index = round(len(sorted_list)*(percentile/100))-1
                print("The " + str(percentile) + "th Percentile of " + column + " is " + str(sorted_list[index]))
                
                
def quantile(dataframe,quantiles,columns='all'):
    list_of_int_columns = list(dataframe.select_dtypes(include=['int64','float64']).columns)
    
    def sorting(column):
        if type(column) == 'pandas.core.series.Series':
            sorted_list = sorted(column.tolist())
            return sorted_list
        else:
            sorted_list = sorted(column)
            return sorted_list
        
    if columns == 'all':
        for column in list_of_int_columns:
            sorted_list = sorting(dataframe[column])
            for quantile in quantiles:
                index = round(len(sorted_list)*(quantile))-1
                print("The " + str(quantile) + "th Quantile of " + column + " is " + str(sorted_list[index]))
    else:
        for column in columns:
            sorted_list = sorting(dataframe[column])
            for quantile in quantiles:
                index = round(len(sorted_list)*(quantile))-1
                print("The " + str(quantile) + "th Quantile of " + column + " is " + str(sorted_list[index]))

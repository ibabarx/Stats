def iqr(dataframe,columns='all'):
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
            q3_index = round(len(sorted_list)*(0.75))-1
            q3 = sorted_list[q3_index]
            q1_index = round(len(sorted_list)*(0.25))-1
            q1 = sorted_list[q1_index]
            print("IQR : " + str(q3-q1))
    else:
        for column in columns:
            sorted_list = sorting(dataframe[column])
            q3_index = round(len(sorted_list)*(0.75))-1
            q3 = sorted_list[q3_index]
            q1_index = round(len(sorted_list)*(0.25))-1
            q1 = sorted_list[q1_index]
            print("IQR : " + str(q3-q1))

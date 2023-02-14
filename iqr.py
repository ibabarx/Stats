def iqr(dataframe,columns='all'):
    
    '''
    dataframe : name of the pandas dataframe in use
    columns : columns, of which the IQR is to be calculated
              default = 'all' (IQR of all columns in the dataframe is calculated)
              otherwise, pass the columns of which the IQR is desired, as a list. ex : ['column_A','column_B','column_C'] 
    '''
    
    def sorting(column):            # An inner function to sort the columns
        if type(column) == 'pandas.core.series.Series':
            sorted_list = sorted(column.tolist())
            return sorted_list
        else:
            sorted_list = sorted(column)
            return sorted_list          # Return sorted columns
        
    if columns == 'all':            # If IQR of all columns is required
        list_of_int_columns = list(dataframe.select_dtypes(include=['int64','float64']).columns)            # List of all columns with Numeric datatypes
        for column in list_of_int_columns:          # looping through all columns with numeric datatypes
            sorted_list = sorting(dataframe[column])
            q3_index = round(len(sorted_list)*(0.75))-1
            q3 = sorted_list[q3_index]
            q1_index = round(len(sorted_list)*(0.25))-1
            q1 = sorted_list[q1_index]
            IQR = q3-q1         # calculate IQR
            print("IQR : " + str(IQR))
            
    else:           # If IQR of only specific columns is required
        for column in columns:          # looping through columns passed by the user
            sorted_list = sorting(dataframe[column])
            q3_index = round(len(sorted_list)*(0.75))-1
            q3 = sorted_list[q3_index]
            q1_index = round(len(sorted_list)*(0.25))-1
            IQR = q3-q1         # calculate IQR
            print("IQR : " + str(IQR))

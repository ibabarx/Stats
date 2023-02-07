def mode(dataframe,columns='all'):
    
    def element_counts(column):
        uniques = set(column)
        counts = []
        counter = 0
        for element in uniques:
            for example in column:
                if element == example:
                    counter = counter + 1
                else:
                    pass
            counts.append(counter)
            counter = 0
        return max(counts),(list(zip(uniques,counts)))        

            
    list_of_int_columns = list(dataframe.select_dtypes(include=['int64','float64']).columns)
    if columns == 'all':
        for column in list_of_int_columns:
            max_val,elements_and_counts = element_counts(dataframe[column])
            for tpl in elements_and_counts:
                if tpl[1] == max_val:
                    print("for column " + column + " mode is : " + str(tpl[0]) + " and its count is " + str(tpl[1]))
    else:
        for column in columns:
            max_val,elements_and_counts = element_counts(dataframe[column])
            for tpl in elements_and_counts:
                if tpl[1] == max_val:
                    print("for column " + column + " mode is : " + str(tpl[0]) + " and its count is " + str(tpl[1]))

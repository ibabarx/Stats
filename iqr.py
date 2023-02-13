def IQR(dataframe,columns='all'):
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
                    return sorted_list[index]
        else:
            for column in columns:
                sorted_list = sorting(dataframe[column])
                for quantile in quantiles:
                    index = round(len(sorted_list)*(quantile))-1
                    return sorted_list[index]
    print("IQR : " + str(quantile(data,[0.75],['avg_price_per_room']) - quantile(data,[0.25],['avg_price_per_room'])))

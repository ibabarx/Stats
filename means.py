def mean(dataframe,columns='all',decimal_points=2,plot=False,width = 0.8,bottom=None,align = 'center',
         ticks_rotation=[90,0],color='green'):
    def plotter():
        plt.figure()
        plt.bar(x = data_frame[0],height=data_frame[1],width=width, bottom=bottom, align=align,color=color)
        plt.xticks(rotation=ticks_rotation[0])
        plt.yticks(rotation=ticks_rotation[1])
        
    # Empty Dictionary for use when user wants to Output Mean in form of Pandas Dictionary
    mean_dictionary = {}
        
    # List of all features with int or float data type
    list_of_int_columns = list(dataframe.select_dtypes(include=['int64','float64']).columns)
    
    # If the user wants to find the mean of all Features
    if columns == 'all':
        if plot == False:
            for column in list_of_int_columns:
                print(column + " Mean = " + str(sum(dataframe[column]) / dataframe[column].shape[0]))
        else:
            for column in list_of_int_columns:
                print(column + " Mean = " + str(sum(dataframe[column]) / dataframe[column].shape[0]))
                mean_dictionary[column] = sum(dataframe[column]) / dataframe[column].shape[0]
                data_frame = pd.DataFrame(mean_dictionary.items())
            plotter()
    # If the user wants to find the mean of specific Features        
    else:
        if plot == False:
            for column in columns:
                print(column + " Mean = " + sum(dataframe[column]) / dataframe[column].shape[0])
        else:
            for column in columns:
                print(column + " Mean = " + str(sum(dataframe[column]) / dataframe[column].shape[0]))
                mean_dictionary[column] = sum(dataframe[column]) / dataframe[column].shape[0]
                data_frame = pd.DataFrame(mean_dictionary.items())
            plotter()
            
        

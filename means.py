import matplotlib.pyplot as plt

def mean(dataframe,columns='all',decimal_points=2,plot=False,width = 0.8,align = 'center',
         ticks_rotation=[90,0],color='green',edgecolor='green',linewidth=0):
         
    '''
    dataframe : The Dataframe that we want to perform the Mean operation on
    columns   : Default = 'all' , Means of all applicable columns in calculated.
                Else define all the columns to find means of as strings, in a list.
    decimal_points : The number of integers after decimal points in the returned solution.
                     Default = 2
    plot : Draw a Barplot of the Columns and their respective means
           Default = False
           width : Width of the bars 
                   Default = 0.8
           align : alignment of bar with respect to their labels
                   Default = centre
                   others = left,right
           ticks_rotation = rotation of the x and y labels respectively , as a list
                            Default = [0,90]
           color = Color of the Bars
                   Default = Green
           edgecolor = color of Edged of the bars
                       Default = Green
           linewidth = width of the bar edges
                       Default = 0
    '''     

    # An Inner function that is used to draw bar plots    
    def plotter():
        plt.figure()
        plt.bar(x = data_frame[0],height=data_frame[1],width=width, align=align,color=color,edgecolor='green'
                ,linewidth=linewidth)
        plt.xticks(rotation=ticks_rotation[0])
        plt.yticks(rotation=ticks_rotation[1])
        
    mean_dictionary = {}   # Empty Dictionary for use , to store means of respective features, further to use for plotting.
    list_of_int_columns = list(dataframe.select_dtypes(include=['int64','float64']).columns)       # List of all features with int or float data type
    
    if columns == 'all':   # If Means of All FEatures is required        
        if plot == False:  # If Plot is Not Required
            for column in list_of_int_columns:        
                print(column + " Mean = " + str(sum(dataframe[column]) / dataframe[column].shape[0]))
        else:     # If Plot is Required
            for column in list_of_int_columns:
                print(column + " Mean = " + str(sum(dataframe[column]) / dataframe[column].shape[0]))
                mean_dictionary[column] = sum(dataframe[column]) / dataframe[column].shape[0]      
            data_frame = pd.DataFrame(mean_dictionary.items())
            plotter()
                    
    else:         # If means of specific Features is required
        if plot == False:  # If Plot is Not Required
            for column in columns: 
                print(column + " Mean = " + sum(dataframe[column]) / dataframe[column].shape[0])
        else:     # If Plot is Required
            for column in columns:
                print(column + " Mean = " + str(sum(dataframe[column]) / dataframe[column].shape[0]))
                mean_dictionary[column] = sum(dataframe[column]) / dataframe[column].shape[0]
            data_frame = pd.DataFrame(mean_dictionary.items())
            plotter()
            
#################################################################################################################################################################
                                                               
def trimmed_mean(dataframe,columns='all',trim = 0.05,decimal_points=2,plot=False,width = 0.8 ,align = 'center',
         ticks_rotation=[90,0],color='green',edgecolor='green',linewidth=0):
         
    '''
    dataframe : The Dataframe that we want to perform the Mean operation on
    columns   : Default = 'all' , Means of all applicable columns in calculated.
                Else define all the columns to find means of as strings, in a list.
    decimal_points : The number of integers after decimal points in the returned solution.
                     Default = 2
    plot : Draw a Barplot of the Columns and their respective means
           Default = False
           width : Width of the bars 
                   Default = 0.8
           align : alignment of bar with respect to their labels
                   Default = centre
                   others = left,right
           ticks_rotation = rotation of the x and y labels respectively , as a list
                            Default = [0,90]
           color = Color of the Bars
                   Default = Green
           edgecolor = color of Edged of the bars
                       Default = Green
           linewidth = width of the bar edges
                       Default = 0
    '''          
         
    # An Inner function that is used to draw bar plots    
    def plotter():
        plt.figure()
        plt.bar(x = data_frame[0],height=data_frame[1],width=width, align=align,color=color,edgecolor='green'
                ,linewidth=linewidth)
        plt.xticks(rotation=ticks_rotation[0])
        plt.yticks(rotation=ticks_rotation[1])
        
    mean_dictionary = {}   # Empty Dictionary for use later, when converted to Pandas Dataframe to Display plots
    list_of_int_columns = list(dataframe.select_dtypes(include=['int64','float64']).columns)       # List of all features with int or float data type
    
    if columns == 'all':   # If the user wants to find the mean of all Features
        if plot == False:   # if barplot is Not Required
            for column in list_of_int_columns:        
                series = dataframe[column]
                no_to_trim = round(series.shape[0] * trim)
                series = series.sort_values(ascending=True)
                series = series[no_to_trim+1 : (series.shape[0]-no_to_trim)+1]
                sol = str(sum(series) / (dataframe[column].shape[0]-(2*no_to_trim)))
                print(column + " Mean = " + sol)
        else:     # if barplot is required 
            for column in list_of_int_columns:
                series = dataframe[column]
                no_to_trim = round(series.shape[0] * trim)
                series = series.sort_values(ascending=True)
                series = series[no_to_trim+1 : (series.shape[0]-no_to_trim)+1]
                sol = str(sum(series) / (dataframe[column].shape[0]-(2*no_to_trim)))
                print(column + " Mean = " + sol)
                mean_dictionary[column] = sol
            data_frame = pd.DataFrame(mean_dictionary.items())
            plotter()
                  
    else:         # If the user wants to find the mean of specific Features        
        if plot == False:  # if barplot is Not required 
            for column in columns:
                series = dataframe[column]
                no_to_trim = round(series.shape[0] * trim)
                series = series.sort_values(ascending=True)
                series = series[no_to_trim+1 : (series.shape[0]-no_to_trim)+1]
                sol = str(sum(series) / (dataframe[column].shape[0]-(2*no_to_trim)))
                print(column + " Mean = " + sol)
        else:     # if barplot is required 
            for column in columns:
                series = dataframe[column]
                no_to_trim = round(series.shape[0] * trim)
                series = series.sort_values(ascending=True)
                series = series[no_to_trim+1 : (series.shape[0]-no_to_trim)+1]
                sol = str(sum(series) / (dataframe[column].shape[0]-(2*no_to_trim)))
                print(column + " Mean = " + sol)
                mean_dictionary[column] = sol
            data_frame = pd.DataFrame(mean_dictionary.items())
            plotter()
    
#################################################################################################################################################################

def weighted_mean(dataframe,columns,weights,decimal_points=2):
         
    '''
    dataframe : The Dataframe that we want to perform the Mean operation on
    columns   : define all the columns to find weighted means of , as strings, in a list.
    weights : List of columns that should be considered the weights
    decimal_points : The number of integers after decimal points in the returned solution.
                     Default = 2
    '''

    for i in range(len(columns)):
        weighted = sum(dataframe[columns[i]] * dataframe[weights[i]]) / sum(dataframe[weights[i]])
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Feature : " + columns[i] + "\nWeights : " + weights[i] + "\nWeighted Mean = " + str(weighted))

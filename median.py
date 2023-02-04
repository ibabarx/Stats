def median(dataframe,features='all',plot=False,ptype = 'scatter', c=None, marker=None,ticks_rotation=[90,0],s=10,width = 0.8,bottom=None,align = 'center',
            color='green',edgecolor='green',linewidth=0):
    
    def plotter():
        if ptype =='scatter':
            plt.figure()
            plt.scatter(x = dictionary.keys(),y=dictionary.values(),s=s)
            plt.xticks(rotation=ticks_rotation[0])
            plt.yticks(rotation=ticks_rotation[1])
        else:
            plt.figure()
            plt.bar(x = dictionary.keys(),height=dictionary.values(),width=width, bottom=bottom,
                align=align,color=color,edgecolor='green',linewidth=linewidth)
            plt.xticks(rotation=ticks_rotation[0])
            plt.yticks(rotation=ticks_rotation[1])
        
    if features != 'all':
        if plot==False:
            for feature in features:
                size = dataframe[feature].shape[0]
                if size%2==1:
                    sol = str(sorted(dataframe[feature].tolist())[((size+1)//2)])
                    print(feature + " Median : " + sol)
                else:
                    sol = str(sorted(dataframe[feature].tolist())[(((size)//2 - 1)+(size)//2)/2])
                    print(feature + " Median : " + sol)
        else:
            dictionary = {}
            for feature in features:
                size = dataframe[feature].shape[0]
                if size%2==1:
                    sol = sorted(dataframe[feature].tolist())[((size+1)//2)]
                    dictionary[feature] = sol
                    print(feature + " Median : " + str(sol))
                else:
                    sol = sorted(dataframe[feature].tolist())[(((size)//2 - 1)+(size)//2)/2]
                    dictionary[feature] = sol
                    print(feature + " Median : " + str(sol))
            plotter()
    else:
        features = list(dataframe.select_dtypes(include=['int64','float64']).columns)
        if plot==False:
            for feature in features:
                size = dataframe[feature].shape[0]
                if size%2==1:
                    sol = str(sorted(dataframe[feature].tolist())[((size+1)//2)])
                    print(feature + " Median : " + sol)
                else:
                    sol = str(sorted(dataframe[feature].tolist())[(((size)//2 - 1)+(size)//2)/2])
                    print(feature + " Median : " + sol)
        else:
            dictionary = {}
            for feature in features:
                size = dataframe[feature].shape[0]
                if size%2==1:
                    sol = sorted(dataframe[feature].tolist())[((size+1)//2)]
                    dictionary[feature] = sol
                    print(feature + " Median : " + str(sol))
                else:
                    sol = sorted(dataframe[feature].tolist())[(((size)//2 - 1)+(size)//2)/2]
                    dictionary[feature] = sol
                    print(feature + " Median : " + str(sol))
            plotter()

            
#################################################################################################################################################################
#################################################################################################################################################################


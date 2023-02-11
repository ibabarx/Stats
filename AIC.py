import math
def AIC(observed,predicted,p):
    n = len(observed.tolist())
    def rss(observed,predicted):
        list_observed = observed.tolist()
        list_predicted = predicted.tolist()
        residue_squared = []
        for index in range(len(list_observed)):
            residue_squared.append((observed[index] - predicted[index])**2)
        rss = sum(residue_squared)
        return rss
    rss = rss(observed,predicted)
    AIC = (2*p)+(n*math.log(rss/n))
    print("AIC : " + str(AIC))

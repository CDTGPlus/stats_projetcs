from collections import Counter
import scipy.stats as stats

def process_input(data):
    #Aggregate input into valid numerical array
    if ',' not in data:
        return 'Please enter data in valid format'
    alpha = []
    for x in  data.split(','):  
        valid = True
        negative = False
        cnt = 0
        var = ''
        
        for n in x:
            if n == '-':
                negative = True 
                continue
            if n == ' ':
                continue
            if n.isnumeric() == False and n != '.':
                valid = False
            if n == '.':
                cnt += 1
    
            var += n
            if cnt > 1:
                valid = False
                
            if valid == False:
                break

        if valid == True:
            var = float(var)
            if negative == True:
                var = -(var)
            alpha.append(var)
    return alpha
    

class probability:
    #generate z score and p values
    def __init__(self,x,mean,stdv):
        self.zscore = self.z_score(x,mean,stdv)
        self.pvals = self.p_values(self.zscore)

    def z_score(self,x,m,sd):
        return (x-m)/sd
    
    def p_values(self,zscore):
        pv_ot_negative = round(stats.norm.cdf(zscore),4)
        pv_ot_positive = round(stats.norm.cdf(-(zscore)),4)
        pv_tt = round(2 * (1 - stats.norm.cdf(abs(zscore))),4)
        p_vals = [pv_ot_negative,pv_ot_positive,pv_tt]
        return p_vals

class summary_stats:
    #Generate set of discriptive statistics from data
    def __init__(self,nums):
        self.nums = sorted(nums)
        self.mean = self.meanStat(self.nums)
        self.mode = self.modeStat(self.nums)
        self.median = self.medianStat(self.nums)
        self.variance = self.varianceStat(self.nums,self.mean)
        self.standard_dev = self.standard_devStat(self.variance)
        if len(self.nums) >= 4:
            self.quartile1, self.quartile3, self.iqrRange = self.quartileStat(self.nums)
        self.minimum, self.maximum = self.nums[0], self.nums[-1]

    def meanStat(self,n):
        return round(sum(n)/len(n),2)
    
    def modeStat(self,n):
        data = Counter(n)
        mdata = sorted(data.items(), key=lambda x:x[1], reverse=True)
        return mdata[0][0]
    
    def medianStat(self,n):
        if len(n) % 2 == 0:
            arc = int((int(len(n)/2)+(int(len(n)/2)+1))/2)
        else:
            arc = int((len(n)+1)/2)
        return n[arc-1]
    
    def varianceStat(self,n,mean):
        sigma = 0
        for x in n:
            var = (x-mean)**2
            sigma += var
        return round((sigma/(len(n)-1)),2)
    
    def standard_devStat(self,variance):
        return round(variance**0.5,2)

    def quartileStat(self,n): 
        qr1 = round((len(n))*(0.25))
        quartile1 = (n[qr1-1]+n[qr1])/2

        qr3 = round((len(n))*(0.75))
        quartile3 = (n[qr3-1]+n[qr3])/2

        interQrt_range = quartile3 - quartile1

        return quartile1,quartile3,interQrt_range



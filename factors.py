from numpy import sqrt,sort,linspace,mean,min,array,arange,e
import matplotlib.pyplot as plt

def isDivisor(n,k):
        """returns true if n is divsable by k"""
        if n%k==0:
                return(True)
        else:
                return(False)

def getFactors(n):
        factors = []
        for i in xrange(1,int(sqrt(n))+1):
                if isDivisor(n,i):
                        factors.append(i)
                        factors.append(n/i)
        return(sort(factors))

def sumFactors(n):
        return(sum(getFactors(n)))
def meanFactor(n):
        return(mean(getFactors(n)))
M = 5000
x = arange(0,M)
x1 =  linspace(0,M,10*M)
y = []
for i in x:
        y.append(meanFactor(i))

y = array(y)
rat = y/x
print min(rat)
print max(rat)
plt.plot(x,y,'b.')
plt.plot(x1,x1/2,'r')
plt.plot(x1,x1/e,'r')
plt.plot(x1,x1/3,'r')
plt.show()
# for i in range(len(y)):
#       # print(x[i])
#       if abs(y[i])<=abs(x[i]/2+.1):
#               print(x[i])



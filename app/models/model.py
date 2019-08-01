import scipy.stats as st
import math
# pip install scipy
def blackScholes(S, X, T, r, o):
    d1=(math.log(S/X)+(T*(r+(o**2)/2)))/(o*(T**(.5)))
    d2=d1-(o*(T**(.5)))
    C=(S*(st.norm.cdf(d1)))-(X*(math.exp(-r*T))*(st.norm.cdf(d2)))
    return C
    
def revBlackScholes(C,S,X,T,r):
    approx = []
    for inc in range(1,10001): #cant use 0 and divide by 0 in BSM
        testo = inc/10000
        approx.append(blackScholes(S,X,T,r,testo))
    
    diff = abs(C-approx[0])
    currIndex = 0
    for item in approx:
        newDiff = abs(C-item)
        if newDiff < diff:
            diff = newDiff
            currIndex = approx.index(item)
            
    currPercent = currIndex + 1
    currPercent = currPercent/10000
        
    return "Expected Volatility: " + str(round(currPercent,3)) + " out of 1." +"\nThe closest stock price found by the model was " + str(round(approx[currIndex],2)) + "."

print(str(revBlackScholes(3.788,52,50,.5,.05)))
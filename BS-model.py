# Black-Scholes Pricing Model

import numpy as np
from scipy.stats import norm

# define variables

r = 0.01  # interest rate
S = 30 # underlying asset value
K = 40 # strike price
T = 100/365 # time - converts days input to yrs
sigma = 0.3 # volatility

def BS(r,S,K,T,sigma,type="C"):
    "Calculate BS option price for a call/put"
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    try:
        if type ==  "C":
            price = S*norm.cdf(d1,0,1) - K*np.exp(-r*T)*norm.cdf(d2,0,1)
        elif type  == "P":
            price = K*np.exp(-r*T)*norm.cdf(-d2,0,1) - S*norm.cdf(-d1,0,1)
        return price
    except:
        print("Please confirm all option paramaters!")

print("Option Price is: ", round(BS(r,S,K,T,sigma,type='C'),2))
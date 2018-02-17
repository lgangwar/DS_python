# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 23:26:44 2018

@author: Lalit

Test Case 1:
	      balance = 320000
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 29157.09
"""

def balanceAfterYear(balance, monthly, annualIntr):
    balance = balance - monthly
    count = 1
    while count<12:
        balance = balance - monthly + (balance*annualIntr/12)
        count = count + 1
    return balance
        

def balanceCalc(balance, annualIntr):
    monthlyIntr = annualIntr/12
    upper = (balance * (1+monthlyIntr)**12)/12
    lower = balance/12
    
    while True:
        monthly = (upper + lower)/2
        residualBalance = balanceAfterYear(balance,monthly,annualIntr)
        print(str(residualBalance) + " hehe")
        if residualBalance < 0:
            upper = monthly
        else:
            lower = monthly
        if abs(residualBalance)<1:
            print('Lowest Payment: ' + str(round(monthly,2)))
            break

'''balanceCalc(320000, 0.2)'''
balanceCalc(999999, 0.18)
        
    
    
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 00:03:55 2018

@author: Lalit


Test Case 1:
	      balance = 3329
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 310
          
"""

def balanceCalc(balance, annualInterestRate):
    count = 0
    monthly = 10*((balance/12)//10)
    initbalance = balance
    while count <= 108:
        count = count + 1
        if count%12 == 1:
            balance = balance - monthly
        else:
            balance = balance - monthly + (balance * annualInterestRate / 12)
        if count % 12 == 0:
            if balance < 0:
                print('Lowest Payment: ' + str(int(monthly)))
                break
            '''print(str(balance) + ' ' + str(monthly))'''
            monthly = monthly + 10
            balance = initbalance 
        
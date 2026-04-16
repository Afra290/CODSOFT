# -*- coding: utf-8 -*-
"""
Created on Wed April 01 2026

@author: Afra
"""
def your_calculator():
    print("\n---Simple Calculator---")
    while True: 
         try:
            n1=float(input("Enter 1st number:"))
            op=input("Enter operator(+,-,*,\):")
            n2=float(input("Enter 2nd number:"))
        
            if op=='+': 
               print(f"Result:{n1+n2}")
            elif op== '-':
               print (f"Result:{n1-n2}")
            elif op== '*': 
               print (f"Result:{n1*n2}")
            elif op== '/': 
               print (f"Result:{n1/n2}" if n2!=0 else"Errror:  Div by 0")
            else: print("Invalid Operator")
         except ValueError :
               print("Error: please enter numbers only")

your_calculator()

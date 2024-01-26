# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 11:31:12 2024

@author: cmj17
"""
import random


fortunes= [
    "Yes",
    "No",
    "Maybe",
    "Not Likely",
    "Likely",
    "I dont know",
    "Sure",
    "Absolutely"]

numFortunes=len(fortunes)
userInput=input("""
                WELCOME TO MAGIC 8 BALL
                    
                1. Print all respones
                2. Find a specific fortune
                3. Ask question
                Pick a number(1-3): """)

if userInput=="1":
    for i in range(numFortunes):
        print(f"{i+1}: {fortunes[i]} ")

if userInput=="2": 
    twoInput=input("Choose a number 1-8: ")
    if twoInput>"0"and twoInput<"9":
        twoInput=int(twoInput)
        print(fortunes[twoInput-1])
    else:
        print("Please pick a number within the range next time.")

elif userInput=="3":
    threeInput=input("Ask me a question: ")
    print(random.choice(fortunes))

elif userInput<"1":
    print("That number is too low!")

elif userInput>"3":
    print("That number is too high!")
        
        
        
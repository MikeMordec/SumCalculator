'''
Created on May 8, 2022

@author: michaelmordec

Lab 11
- Please input a whole number greater than 1.
- The output will be the sum of the numbers from 1 to the number.

'''
# takes N as a parameter and returns the sum of 1 to N
def sumOfOneToN(n):
    total = 0
    for num in range(n+1):
        total = total + num
    return total       

#main program
def main():
    n = int(input("Enter a number greater than 1: "))
    print("Answer: ",sumOfOneToN(n))
    
main()
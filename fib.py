#Author:Zuriahn Yun
#Date:2/12/2023
#Description:Finds the golden number and the number in the the fibonacci sequence

#Import sys to use Program arguments
import sys
#Number given is the number of the sequence the user wants
num = int(sys.argv[1])
start = 0
f = 0
n = 1

#Creating a while loop
while start < num:
    fib = f + n
    #Updating the variables so that the sequence continues and the same numbers arent printed
    f = n
    n = fib
    #Adding to start so that the sequence continues to the right point
    start+=1
#For infinity and so that golden can be figured out
if num == 1:
    golden ="infinity"
else:
    #Calculating golden ratio
    golden = fib/f
#Printing number and golden ratio
print("Fib:", f, "Golden:", golden, end="")
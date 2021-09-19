# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 21:29:38 2021

@author: cprusty58@gmail.com
@topic: Generators

Explanations:
    > Generators are objects that are lazy operators.
    > Mostly used to create infinite sequence of numbers or read large pieces of data.
    > There are two kinds of Generators - Expression - Function.
    > Yields are kind of Return statements.
    > Advantages: - Avoid memory errors.
"""
#Expression
g_exp = [num for num in range(0,5)]
print(g_exp) #[0,1,2,3,4]
print(type(g_exp)) #List

arr="1234"
g_exp2 = [arr[i] for i in range(len(arr))]
print(g_exp2) #['1','2','3','4']
print(type(g_exp2)) #List


#Function
def g_func(num):
    for i in range(num):
        yield i
        
Generator = g_func(5)
print(next(Generator))   #0

print(next(Generator))   #1

for i in Generator:
    print(i,end=" ")     #2,3,4

print("")

#Read CSV Example
"""
def read_csv(<filename>):
    for row in open(<filename>,"r"):
        yield row

gen = read_csv(<filename>)
for i in gen:
    print(i)

"""

###Infinite Sequence Example

def inf_seq():
    num = 0
    while True:
        yield num
        num+=1

gen = inf_seq()
print(next(gen))    #0

print(next(gen))    #1

for i in range(3):
    print(next(gen),end = " ")   #2,3,4
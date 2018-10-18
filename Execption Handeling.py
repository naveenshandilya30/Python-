#Question 1
a=3
try:
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError as b:
        print(b)


#Question 2

l = [1,2,3]
try:
    print(l[3])
except IndexError as g:
    print(g)


#Question 3

try:
    raise NameError("Hi there")  # Raise Error
except NameError as j:
    print("An exception is ")
       

def AbyB(a , b):
        try:
            c = ((a+b) / (a-b))
        except ZeroDivisionError:
            print("a/b result in 0")
        else:
            print(c)
    
    # Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

#Question 5
import abc
try:
    from abc import datetime
except ImportError as n:
    print(n)


try:
    x = int(input("Enter the number: "))
    print(x)
except ValueError as m:
    print(m)

l = [1,2,3]
print(type(l))
try:
    
    print(l[3])
except Exception as h:
    print(h)

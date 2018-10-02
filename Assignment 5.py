#DECISION AND FLOW CONTROL

#Question_1

year=int(input("Enter year : "))
if year%4==0:
    print("The year is a leap year")
else:
    print("The year is not a leap year")



#Question_2


length= int(input("Enter length:"))
breadth= int(input("Enter breadth:"))
if length==breadth:
    print("dimensions are square")
else:
    print("dimensions are rectangle")




#Question_3

a=int(input("Enter age of  person a:"))
b=int(input("Enter age of person b:"))
c=int(input("Enter age of person c:"))
if (a>b and a>c):
    print ("a is older")
elif (c>b and c>a):
    print("c is older")
elif(b>a and b>c):
    print("b is older")
if(a<b and a<c):
    print("a is younger")
elif(b<a and b<c):
    print("b is younger")
elif(c<a and c<b):
    print("c is younger")




#Question_4

print ("Enter age : ")
age = int(input())
print ("Enter SEX..? (M or F)")
sex = input()
print ("MARRIED..? (Y or N)")
marry = input()
if sex == "F" and age>=20 and age<=60:
  print ("Urban areas only")
elif sex == "M" and age>=20 and age<=40:
  print ("You can work anywhere")
elif sex == "M" and age>40 and age<=60:
  print ("Urban areas only")
else:
  print ("ERROR")


#Question_5

a=int(input("enter the amount:"))
print(a)
if (a<=1000):
    print("Sorry, no discount")
elif (a*100 > 1000):
  print ("Cost is",((a*100)-(.1*a*100)))
else:
  print ("Cost is",a*100)



#Loops.................................


#Question 1


l=[]
for a in range(10):
    integer= int(input("enter nos.: "))
    l.append(integer)
print(l)
for b in l:
    print(b)


#Question 2

while True:
 print("Error 404")


#Question 3


m=[]
elements = int(input("enter total no elements of list: "))
for c in range(elements):
    element=int(input("enter elements: "))
    m.append(element)
print(m)
n=[]
for d in m:
    e=d**2
    n.append(e)
print(n)



#Question 4

integers=[]
decimals = []
strings = []
lists = ["Naveen", "2", "4", "5.5", "Shandilya", "9.8"]
for f in lists:
    if f.isalpha():
        strings.append(f)
    elif f.isdigit():
        integers.append(int(f))
    else:
        decimals.append(float(f))
print(decimals)
print(integers)
print(strings)


#Question 5

even =[]
odd = []
for g in range(1,101):
    if g%2==0:
        even.append(g)
    else:
        odd.append(g)
print(even)
print(odd)


#Question 6


for h in range(1,5):
    print("*"*h)

#Question 7

l=  []
a = int(input("enter total no of elements: "))
for b in range(a):
    elements = input("enter element: ")
    l.append(elements)
c = input("enter elements to be search: ")
for d in l:
    if c==d:
        l.remove(c)
print(l)


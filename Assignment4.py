# Question 1

list= [0,1,2,3,4,5]
list.reverse()
print(list)


#Qustion 2

lst= 'I Love You '
for i in lst:
    if i==i.upper():
        print(i,end="")
print()

#Question 3

a=input("Enter the numbers:")
print(a.split())

#Question 4

str=input("Enter the String: ")
if (str==str[::-1]):
    print(str,'is a pallindrome')
else:
     print(str,'is not a pallindrome')

#Question 5

#shallowcopy
a=['python',20,'c++','ruby']
b=a
print("original list a:",a,"id=",id(a))
print("shallow copy list b:",b,"id=",id(b))

print("original list a:",a)
print("shallow copy list b:",b)

#deepcopy

a=['python',20,'c++','ruby']
c=a.copy()
print("original list:",a,"id=",id(a))
print("deep copy list:",c,"id=",id(c))

print("original copy a:",a)
print("deep copy list c:",c)
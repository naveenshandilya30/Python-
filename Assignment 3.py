#LIST............

#Question_1

a=[1,2,3,4,5]
print(a)

#Question 2

a=['google’,’apple’,’facebook’,’microsoft’,’tesla']
a.append([1, 2, 3, 4, 5])
print(a)


#Question 3

a=["google","apple","tesla","google","microsoft","google"]
print(a.count("google"))


#Question 4

a=[2,4,5,3,6,1]
a.sort()
print('Numbers after sorting in ascending order',a)

#Question 5

A=[11,12,13,14,15,16,17,18,19,20]
B=[1,2,3,4,5,6,7,8,9,10]
C=A+B
C.sort()
print(C)


#Question 6

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count_odd = 0
count_even = 0
for x in a:
        if not x % 2:
            count_even+=1
        else:
            count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)


#TUPLES..............

#Question 1


a = [1,2,3,4,5,6,7,8,9]
print (a[::-1])
#OR
y = reversed(a)
print(tuple(y))


#Question 2

t1=(20,34,45,10,67,84)
print('Largest element is: ',max(t1))
print('Smallest element is:',min(t1))


#Strings...........

#Question 1

str="hello iam naveen"
print(str.upper())

#Question 2

str="150008"
print(str.isnumeric())


#Question 3

str="Hello World"
print(str.replace('World','Naveen'))

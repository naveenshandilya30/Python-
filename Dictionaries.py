#Question No.1

n1=int(input("enter total number of keys: "))
d1={}
for i in range(1,n1+1):
    v=input("enter value of key: ")
    d1[i]=v
l=[]
for j in d1:
    l.append(j)
print("keys of dictionary is: ",l)

#Question No.2

d={"a":{"Maths":45,"Science":56,"Hindi":67,"English":89},"b":{"Maths":34,"English":67,"Hindi":45,"Science":76},"c":{"Science":35,"Maths":65,"English":23,"Hindi":78}}
n=input("Enter name of student (a,b,c) to print marks: ")
for i in d:
    if n.lower()==i:
        print(d[n.lower()])

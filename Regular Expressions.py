import re

#Q.No.1

str1=input("enter a string containig valid email: ")
pattern=r'[\w\.-]+@[\w\.-]+'
x=re.findall(pattern,str1)
print(x)

#Q.No.2

str2=input("enter a string with indian phone number: ")
pat=r"[6-9][0-9]{9}"
num=re.findall(pat,str2)
print(num)


#q-1)
n=int(input("enter number of elements in list"))
list=[]
for i in range (0,n):
    a=int(input("enter elements"))
    list.append(a)
print(list[::-1])    
#q-2)
string=input("enter word")
for i in string:
    if(i>='A' and i<='Z'):
        print(i)

#q-3)
n1=input("enter number using commas").split(",")
list1=[]
for i in n1:
    b=int(i)
    list1.append(b)
print(list1)
#q-4)
str1=input("enter string")
str2=str1[::-1]
if(str2==str1):
    print("palindrome")
else:
    print("not palindrome")
#q-5)

import copy as c
print("---deep copy---")
a=[1,2,3,[4,5],6,7]
b=c.deepcopy(a)
print("list 1",a)
print("lis 2",b)
b[3][0]=9
print("after changing list 2")
print("list 1",a)
print("list 2",b)

print("---shallow copy---")
a=[1,2,3,[4,5],6,7]
b=c.copy(a)
print("list 1",a)
print("lis 2",b)
b[3][0]=9
print("after changing list 2")
print("list 1",a)
print("list 2",b)

#DIFFERENCE
'''
1.changes made in deep copy of list are never reflected in original list
where as changes made in shallow copy are always reflected in original list
2.in deep copy of object is copied to other object whereas in shallow copy
reference of object is copied in other object
'''


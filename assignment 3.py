#question 1 Create a list with user defined inputs.
print("<----solution 1-------->")

list= []
e1=input("enter element ");
list.append(e1)
e2=input("enter element ");
list.append(e2)
e3=input("enter element ");
list.append(e3)
e4=input("enter element ");
list.append(e4)
e5=input("enter element ");
list.append(e5)
print(list)

#question 2 Add the following list to above created list:  [‘google’,’apple’,’facebook’,’microsoft’,’tesla’]
print("<----solution 2-------->")

list1=["google","apple","facebook","microsoft","tesla"]
list.extend(list1)
print(list)

#question 3  Count the number of time an object occurs in a list.
print("<----solution 3-------->")

list2=["google","facebook","instagram","google"]
print("count is ",list.count('google'))

#question 4 create a list with numbers and sort it in ascending order.
print("<----solution 4-------->")

list3=[]
n=int(input("enter the no. of elements in a list"))
for i in range (n):
    x=int(input("enter value"))
    list3.append(x)
print("before sorting : ",list3)
list3.sort()
print("after sorting : ",list3)


#question 5 Given are two one-dimensional arrays A and B which are sorted in ascending order. Write a program to merge them into a single sorted array C that contains every item from arrays A and B, in ascending order. [List] 
print("<----solution 5-------->")

A=[1,5,7,8,2]
B=[4,9,6,3,8]
C=[]
A.sort()
B.sort()
C.extend(A)
C.extend(B)

print(C)


#question 6 Count even and odd numbers in that list.
print("<----solution 6-------->")

list4=[1,5,7,8,9,6,4,3,2]
even=odd=0
for i in list4:
    if(i%2==0):
        even=even+1
    else:
        odd=odd+1
print("no. of even elements : ",even)
print("no. of odd elements : ",odd)

#question 7 Print a tuple in reverse order. 

#this part is not taught in the class

#question 8 Find largest and smallest elements of a tuples. 

#this part is not taught in the class


#question 9 Convert a string to uppercase. 
print("<----solution 9-------->")

string="my name is raghav jain"
print(string.upper())

#question 10  Print true if the string contains all numeric characters. 
print("<----solution 10-------->")

string1=input("enter the string")
length=len(string)
count=0;
for i in range(length):
    if string1.isdigit():
        count=0;
    else:
        count=1;
if count==0:
    print("True")
else:
    print("False")


#question 11 Replace the word "World" with your name in the string "Hello World". 

string2="Hello World"
print("before replacing : ",string2)
print("after replacing : ",string2.replace("World","raghav"))

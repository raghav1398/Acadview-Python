#Q.1)Write a python code to find a valid email address from a text.
import re
a=input('Type your text:')
count=0
matcher=re.finditer('[a-zA-z][a-zA-Z0-9_.]*[@](gmail.com|yahoo.com|hotmail.com|outlook.com)',a)
for i in matcher:
    count+=1
    print('{} is a valid id'.format(i.group()))
if(count==0):
    print('Not a valid id.')

#Q.2)Write a python program to find a valid Indian phone number from a text.
# (Valid Indian numbers will start with "+91-" and after that [6-9] followed by 9 digits. )
b=(input('Enter the no.:'))
count=0
matcher=re.finditer('[6-9][0-9]{9}',b)
for i in matcher:
    count+=1
    print('{} is a valid number.'.format(i.group()))
if(count==0):
    print('Not a valid number.')

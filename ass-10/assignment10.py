#Q.1)Write a Python program to read n lines of a file
n = int(input("Enter number: "))
f = open('line.txt','r')
for i in range(0,n):
    data = f.readline()
    print(data)
f.close()
#Q.2)Write a Python program to count the frequency of words in a file.
f = open('line.txt','r')
a = f.read()
n = input("Enter the value to be counted: ")
b = a.count(n)
print("{} occurs {} times ".format(n,b))
#Q.3)Write a Python program to copy the contents of a file to another file
f1 = open('line.txt')
f2 = open('line1.txt','a')
b = f1.read()
f2.writelines(b)
f2.close()
f1.close()
#Q.4)Write a Python program to combine each line from first file with the corresponding line in second file.
x = open('line.txt','r')
y = open('line1.txt','r')
z = open('line2.txt','w+')
a = x.readlines()
b = y.readlines()
for i,j in zip(a,b):
    z.write(i)
    z.write(j)
l = z.read()
print(l)
z.close()
y.close()
x.close()

#Q.5)Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.
list = []
for i in range(1,11):
    num = int(input("Enter value: "))
    list.append(num)
f1 = open('number.txt','a')
f2 = open('number1.txt','w+')
f1.write(str(list))
print(list)
list.sort()
f2.write(str(list))
f2.close()
f2=open('number1.txt','r')
n = f2.read()
print(n)
f1.close()
f2.close()

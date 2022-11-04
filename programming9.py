#Sum of even numbers
#2 + 4 + 6 +...... + n
n= int(input("Enter the last intiger number\n"))
sum=0
for x in range(2,n+1,2):#initialaization,endind,increament or dicreament
    sum=sum+x
print(sum)
print("The sum of series is:\n")

#Sum of odd numbers
# 1 + 2 + 3 +.... + n
n= int(input("Enter the last intiger number\n"))
sum=0
for x in range(1,n+1,1): #initialaization,endind,increament or dicreament
    sum=sum+x
print(sum)
print("The sum of series is:\n")

#1*1 + 2*2 + 3*3 +......+ n*n
n= int(input("Enter the last intiger number\n"))
sum=0
for x in range(1,n+1,1): #initialaization,endind,increament or dicreament
    sum=sum+x*x
print(sum)
print("The sum of series is:\n")

# 1 + 1/2 + 1/3 +....1/n
n= int(input("Enter the last intiger number\n"))
sum=0
for x in range(1,n+1): #initialaization,endind,increament or dicreament
    sum=sum+(1/x)
print(sum)
print("The sum of series is:\n",round(sum,2))

# 1 * 2 * 3 * .....* n
n= int(input("Enter the last intiger number\n"))
sum=1
for x in range(1,n+1,1): #initialaization,endind,increament or dicreament
    sum= sum * x
print(sum)
print("The sum of multyplying series is:\n",round(sum,2))

#Factorial
n=int(input("Enter an intiger number:\n"))
fact =1
for x in range(1,n+1,1): #initialaization,endind,increament or dicreament
    fact = fact * x
print(fact)
print("The factorial is:\n")

#HCF of Two numbers
num1=int(input("Enter the 1st number:"))
num2=int(input("Enter the 2nd number:"))
n1=num1
n2=num2
HCF=1
for x in range

"""n= int(input("Enter the last intiger number\n"))
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+1
print(sum)"""
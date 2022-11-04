
    # Find the largest number among the three numbers
num1=input("Please enter your 1st intiger number\n" )
num2= input("Please enter your 2nd intiger number\n")
num3=input("Please enter your 3rd intiger number\n")

if (num1>=num2) and (num1>=num3):
    print("1st intiger number is greater: Thank you")
elif(num2>=num1) and (num2>=num3):
    print("2nd intiger number is greater: Thank you :")
elif (num3>=num1) and (num3>=num2):
    print("3rd intiger number is greater: Thank you :")
else:
     print("You enter the wrong numbers:Thank you :")

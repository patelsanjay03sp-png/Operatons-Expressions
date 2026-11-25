age = int(input("Enter your age : "))
marks = int(input("Enter your marks : "))
if (age>=18 and marks>=40):
    print("You are Eligible for the Exam")
elif (age>=18 or marks>=40):
    print("You Meet one of the criteria for the Exam")
else:
    print("You are Not Eligible for the Exam")
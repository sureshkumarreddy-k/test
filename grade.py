marks=int(input("Enter marks:"))
if(marks<100 and marks>=90):
    print("grade :A")
elif(marks>=80 and marks<90):
    print("Grade: B")
elif(marks>=70 and marks<80):
    print("Grade: C")
elif(marks>=60 and marks<70):
    print("Grade: D")
elif(marks>=50 and marks<60):
    print("Grade: E")
elif(marks>=40 and marks<50):
    print("Grade: B")
else:
    print("Fail")

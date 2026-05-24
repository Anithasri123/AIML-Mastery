student={}
n=int(input("Enter number of subjects:"))
total=0
for i in range(n):
    subject=input("Enter subject:")
    marks=int(input(f"Enter for marks for {subject}:"))
    student[subject]=marks 
    total+=marks 
avg=total//n 
if avg>=90:
    grade='A'
elif avg>=70:
    grade='B'
elif avg>=50:
    grade='C'
else:
    grade='Fail'
print("\nStudent Marks:")
print(student)
print("Total Marks:",total) 
print("Average Mark:",avg)
print("Grade:",grade)
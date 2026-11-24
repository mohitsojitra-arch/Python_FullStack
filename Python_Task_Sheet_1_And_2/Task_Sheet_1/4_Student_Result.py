stu_name=input("Enter Student Name : ")
marks=[]
for i in range(0,5,1):
  marks.append(int(input(f"Enter Subject {i+1} Marks : ")))

for i in marks:
    if i < 23:
       print("Fail : ")
       break
else:
  percentage=(sum(marks)/(len(marks)*70))*100 
  print(f"Percentage : {round(percentage,2)}%") 
    
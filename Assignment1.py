n = int(input("Enter number of students: "))  
max_marks = float('-inf')  
min_marks = float('inf')  
sum_of_marks = 0           
absent_count = 0
present_count = 0
for i in range(0, n ):
     mark = int(input("Enter marks obtained by student :"))  
     if mark > max_marks:
         max_marks = mark
     if mark < min_marks:
        min_marks = mark

     sum_of_marks += mark
     if mark < 25:
        absent_count += 1
     else:
        present_count += 1
average = (sum_of_marks)/n
percentage_pass = (present_count/n)*100
print("Maximum marks obtained: ",max_marks)
print("Minimum marks obtained: ",min_marks)
print("Average of marks obtained by students:",average)
print("Percentage of student passed:",percentage_pass)
print("Number of student present:",absent_count)
print("Number of student absent:",present_count)




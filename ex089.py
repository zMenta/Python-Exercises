#Create a school report card. That can register various students and 2 grades for each student.Show the students average grade and if you want to check a specific student grade at the end of the algorithm. Using only 1 list to store all the data.

report = [["Carlos", 10, 8 ,9.85], ["Rodrigo", 4, 5, 6.345], ["Gustavo", 3, 8, 7.781]]  #TEST
#report = []
student = []

# Report contains students
# Each student list has, index [0] = Name | [1] = 1th grade | [2] = 2th grade | [3] =  grade average

# while True: #Register students for the report list.
#     print("="*50)
#     student.append(str(input("Please type the name of the student: ")).strip())
#     for c in range(1,3):
#         student.append(float(input(f"Please type {student[0]}'s {c}th grade: ")))
#     student.append((student[1]+student[2])/2) #add the grade average of this student 
#     report.append(student[:])
#     student.clear()

#     while True: # Checks if the user wants to register more students
#         print("-"*50)
#         choice = str(input("Do you want to register another student? (Y/N)").upper())
        
#         if choice != "Y" and choice != "N": #Checks if the answer is valid 
#             print("Invalid answer, please try again.")
#         else:
#             break
    
#     if choice == "N": #Stops asking for new students.
#         break

print("="*50)
print("|{:^6}|{:^19}|{:^21}|".format("Num.","NAME","Final Grade"))
print("|{:6}|{:19}|{:21}|".format("-"*6, "-"*19, "-"*21 ))
for i in range(len(report)):
    print(f"|{i:^6}|{report[i][0]:^19}|{report[i][3]:^21.1f}|")
print("="*50)
print(report)

while True: #Asks if the user want to check for specific students grades.
    while True:
        choice = str(input("Do you want to check for a student specific grades? (Y/N)").upper())

        if choice != "Y" and choice != "N":
            print("Invalid answer, please try again.")
        else:
            break
    
    if choice == "N": #Don't ask for a specific student grade if choice is "N"
        break
    else:
        study_name = str(input("Please type the name of the student: ")).strip()



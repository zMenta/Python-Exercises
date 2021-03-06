#Create a school report card. That can register various students and 2 grades for each student.Show the students average grade and if you want to check a specific student grade at the end of the algorithm. Using only 1 list to store all the data.

report = []
student = []

# Report contains students
# Each student list has, index [0] = Name | [1] = 1th grade | [2] = 2th grade | [3] =  grade average

while True: #Register students for the report list.
    print("="*50)
    student.append(str(input("Please type the name of the student: ")).strip())
    for c in range(1,3):
        student.append(float(input(f"Please type {student[0]}'s {c}th grade: ")))
    student.append((student[1]+student[2])/2) #add the grade average of this student 
    report.append(student[:])
    student.clear()

    while True: # Checks if the user wants to register more students
        print("-"*50)
        choice = str(input("Do you want to register another student? (Y/N)").upper())
        
        if choice != "Y" and choice != "N": #Checks if the answer is valid 
            print("Invalid answer, please try again.")
        else:
            break
    
    if choice == "N": #Stops asking for new students.
        break

print("="*50)
print("|{:^6}|{:^19}|{:^21}|".format("Num.","NAME","Final Grade"))
print("|{:6}|{:19}|{:21}|".format("-"*6, "-"*19, "-"*21 ))
for i in range(len(report)):  #Shows the students final grades and names in a chart.
    print(f"|{i:^6}|{report[i][0]:^19}|{report[i][3]:^21.1f}|")
print("="*50)

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
        print("-"*50)
        study_name = str(input("Please type the name of the student: ")).strip()
        for i in range(len(report)):
            name_found = False
            if report[i][0] == study_name:
                print("="*50)
                print("|{:^6}|{:^19}|{:^10}|{:^10}|".format("Num.","NAME", "Grade 1", "Grade 2" ))
                print("|{:^6}|{:^19}|{:10}|{:10}|".format("-"*6, "-"*19, "-"*10, "-"*10))
                print("|{:^6}|{:^19}|{:^10}|{:^10}|".format(i, report[i][0], report[i][1], report[i][2]))
                print("="*50)
                name_found = True
                break
        if name_found is not True:
            print("-"*50)
            print("Student not found.")
            print("-"*50)

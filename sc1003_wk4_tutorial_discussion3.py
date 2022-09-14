# for example:
# group names: A, B, C
# lab IDs: 01, 02, 03, 04


grades_db = { 'A': { '01': '', '02': '', '03': '', '04': '' }, 
              'B': { '01': '', '02': '', '03': '', '04': '' },
              'C': { '01': '', '02': '', '03': '', '04': '' }}


while True:

    group = input("Enter student's group letter: ")

    if group in grades_db.keys():

        student_id = input("Enter student's ID: ")

        if student_id in grades_db[group].keys():

            student_score = input("Please enter student score: ")

            if 0 <= int(student_score) <= 100:
                grades_db[group][student_id] = student_score
                quit()
                
            else:
                print("Score has to be between 0 and 100. Please try again.")
        
        else:
            print("Invalid student ID. Please try again.")
    
    else:
        print("Invalid group number. Please try again")


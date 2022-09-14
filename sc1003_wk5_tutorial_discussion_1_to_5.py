grades_db = {}


def input_record(database, group, id, score):
    """assign score to id in group in database"""

    database.setdefault(group, {})
    database[group][id] = score


def query(database, group, id):
    """return score of id in group in database"""

    return database[group][id]


def list_grades(database, group):
    """return group in database"""

    return database[group]


def max_grade(database, group):
    """return max value in group in database"""

    return max(database[group].values())


def main():

    while True:
        
        print("Welcome to the grading system! Please enter your option: \
            \n 1: input record \
            \n 2: query a student \
            \n 3: list grades in a group \
            \n 4: get max in a group \
            \n 5: list all group names \
            \n 6: exit \
            \n")

        user_input = input("option: ")
        
        if user_input == "1":
            group = input("Please input group name: ")
            id = int(input("Please input the student id: "))
            score = float(input("Please input the score: "))
            input_record(grades_db, group, id, score)
        
        elif user_input == '2':
            group = input("Please input group name: ")
            id = int(input("Please input the student id: "))
            print(query(grades_db, group, id) + '\n')
            
        elif user_input == '3':
            group = input("Please input group name: ")
            print(list_grades(grades_db, group) + '\n')
            
        elif user_input == '4':
            group = input("Please input group name: ")
            print(max_grade(grades_db, group) + '\n')
            
        elif user_input == '5':
            print(grades_db.keys() + '\n')
        
        elif user_input == '6':
            quit()
            
        else:
            print("Invalid option. Please try again" + '\n')


if __name__ == "__main__":
    main()

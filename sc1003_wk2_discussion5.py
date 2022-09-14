no_of_girls = int(input("Enter the number of girls: "))
no_of_guys = int(input("Enter the number of guys: "))
sum_of_students_in_class = no_of_girls + no_of_guys
print("Girls percentage: {:.0%}".format(no_of_girls / sum_of_students_in_class))
print("Boys percentage: {:.0%}".format(no_of_guys / sum_of_students_in_class))
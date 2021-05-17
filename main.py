project_title = "Welcome to Student Management System"
width = len(project_title)*2
print("-"*width)
print(project_title.center(width,'-'))
print("-"*width)
list_of_students = []
print("Enter 1: To show the Students List")
print("Enter 2: To Remove the student")
print("Enter 3: To Search the specific student")
print("Enter 4: To add the student")
done = False
while not done:
    user = int(input("Enter a code to start operations: "))
    if user == 1:
        if len(list_of_students) == 0:
            print("You cant fetch the list of students since, there are no students")
        else:
            print("you have choosen to view the entire list of students")
            for student in list_of_students:
                print("---> ", student)

    elif user == 2:
        if len(list_of_students) == 0:
            print("You cant remove the students since, there are no students")
        else:
            print("you have to choosen to remove the specified student")
            student_remove = input("Enter the name of student you want to remove from the list: ")
            try:
                list_of_students.remove(student_remove)
            except:
                print("Sorry! we cant Remove him")

    elif user == 3:
        if len(list_of_students) == 0:
            print("You cant search the students since, there are no students")
        else:
            print("you have to choosen to search for the specified student")
            student_search = input("Enter the name of student you want to search from the list: ")
            if student_search in list_of_students:
                print("He is present in the list")
            else:
                print(
                    "Sorry! He isn't there in the list. The reasons for not removing him may be he is not present in the list or the name you entered has spelling mistakes")

    elif user == 4:
        print("You can add the students")
        student_add = input("Enter the name of student you want to add in the list: ")
        list_of_students.append(student_add)

    user_exit_process = input("Are you done or not? ")#Type done or not
    if user_exit_process == 'done':
        done = True
    else:
        done = False
print("user exited successfully")


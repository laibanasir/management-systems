print('Welcome to student management')
menu()
students = []
student = {}
def menu():
    print('Enter an option of your choice')
    print('1 Add students\n2 Delete students \n3 Find student \n4 Exit')
    option = input('= ')
    if option == '1':
        add()
    elif option == '2':
        delstu()
    elif option == '3':
        findstu()
    elif option == '4':
        print('Good bye')
    else:
        while option != '1' or option != '2' or option != '3':
            print('Invalid entry, enter again')
            option = input('= ')
def add():
    num = int(input('how many students do you want to enroll?'))
    for i in range (num):
        student = {}
        student['Name'] = input('Enter student Name: ' )
        student['number'] = input('Enter roll number: ') 
        student['quarter'] = input('Enter quarter: ')
        students.append(student)
    print('Number of students enrolled: ',len(students))
    print('press any key to go back to menu')
    goto_menu = input()
    menu()
def delstu():
    delname = input('Enter the name of the student whose data you want to delete')
    for student in students :
        if student['Name'] == delname:
            del student['Name']
            del student['number']
            del student['quarter']
    goto_menu = input('Enter any key to go back')
    manu()
def findstu():
    findname = input('Enter student name to get his data: ')
    for student in students:
        if student[Name] == findname:
            print(student)
    goto_menu = input('Enter any key to go back')
    manu()
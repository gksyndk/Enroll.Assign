#2 users
#-Student
#-Admin
def login_admin_student(singin):
    if signin == 1:
        student = str(input("Enter student ID :"))
        # Student Valid ID
        if student in studentID:
            print("Welcome", student)
            return student
        else:
            print("Invalid student ID")
    elif signin == 2:
        admin = input("Enter admin ID :")
        if admin in adminID:
            print("Welcome", admin)
            return admin
        else:
            print("Invalid admin ID")
    else:
        print("Invalid Option")

studentID=["A24AI0033","A24AI0044"]
adminID = "Admin123"

#Choose Student or Admin
print("Menu\n1.Student\n2.Admin")
signin = int(input("Select Option :"))
#Verification#Current ID to hold ID key for add,remove,view.
currentID=login_admin_student(signin)
#Without function
"""if login == 1:
    student = str(input("Enter student ID :"))
    #Student Valid ID
    if student in studentID:
        print("Welcome", student)
    else:
        print("Invalid student ID")
elif login == 2:
    admin = input("Enter admin ID :")
    if admin in adminID:
        print("Welcome", admin)
    else:
        print("Invalid admin ID")
else:
    print("Invalid Option")"""

#Start Menu for Student
#Student
#-Add course
#-Remove course
#-View
def start_menu():
    if currentID in studentID:
        menu = int(input('Menu\n1.Register Course\n2.Drop Courses\n3.Enrollment Status'))
        if menu == 1:
            subjects = [
                {'code': 'ML119', 'name': 'Machine Learning', 'credits': 4},
                {'code': 'CS102', 'name': 'Python Programming', 'credits': 4},
                {'code': 'DM111', 'name': 'Discrete Math', 'credits': 3},
                {'code': 'DAT101', 'name': 'Data Management', 'credits': 3},
                {'code': 'IA101', 'name': 'Introduction to AI', 'credits': 2},
            ]
            print('Available Subjects:')
            for subjects in subjects:
                print(f'{subjects["code"]}: {subjects["name"]} ({subjects["credits"]} credits)')
            
            print('\nEnroll in subjects by entering their codes (type "done" when finished):')
            enrolled_subjects =[]
            while True:
                code = input("Enter Subject Code :").upper()
                if code in subjects:
                    enrolled_subjects.append(code)
                elif code == 'done':
                    break
                else:
                    print('Invalid code. Please try again')

#Admin
#-Handle course
#-View report

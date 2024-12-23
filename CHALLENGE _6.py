#2 users
#-Student
#-Admin
def start_menu():
    while True:
        enrolled_subjects = []
        subjects = [
            {'code': 'ML119', 'name': 'Machine Learning', 'credits': 4},
            {'code': 'CS102', 'name': 'Python Programming', 'credits': 4},
            {'code': 'DM111', 'name': 'Discrete Math', 'credits': 3},
            {'code': 'DAT101', 'name': 'Data Management', 'credits': 3},
            {'code': 'IA101', 'name': 'Introduction to AI', 'credits': 2},
        ]
        if currentID in studentID:
            menu = int(input('Menu\n1.Register Course\n2.Drop Courses\n3.Enrollment Status\n4.Exit\nSelect Option :'))
            if menu == 1:
                #show the available subject
                print('Available Subjects:')
                for subject in subjects:
                    print(f'{subject["code"]}: {subject["name"]} ({subject["credits"]} credits)')

                #insert registration for the subject
                print('\nEnroll in subjects by entering their codes (type "done" when finished):')

                while True:
                    code = input('Enter Subject code: ').upper()
                    if code == 'DONE':
                        print("The subjects code has been registered. You can view the data via menu option.")
                        break

                  #sub = next((s for s in subjects if s['code']==code), None)
                    #next is use to iterate the next element after going through the list
                    # if we dont use next
                    sub = None
                    for s in subjects:
                        if s['code'] == code:
                            sub = s
                            break
                    if sub not in enrolled_subjects:
                        enrolled_subjects.append(sub)
                        print (f'Enrolled in {sub['name']}')
                    elif sub in enrolled_subjects:
                        print('You are already enrolled in this subject.')
                    else:
                        print('Invalid code. Try again.')

            elif menu == 2:
                #removing subject
                while True:
                    code = input('Enter Subject code you wish to drop (type "done" when finished): ').upper()
                    if code == 'DONE':
                        print("The subjects code has been registered. You can view the data via menu option.")
                        break
                    sub = next((s for s in subjects if s['code'] == code), None)
                    if sub in enrolled_subjects:
                        enrolled_subjects.remove(sub)
                        print(f'Subject {sub['name']} removed.')
                    elif sub not in enrolled_subjects:
                        print('The subject is not in your registered course.')
                    else:
                        print('Invalid code. Try again.')

            elif menu == 3:
                print("\nYou are enrolled in the following subjects:")
                #supposedly count the total credits too
                total_credits = 0
                for subject in enrolled_subjects:
                    print(f"{subject['code']}: {subject['name']} ({subject['credits']} credits)")
                    total_credits += subject["credits"]
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
    while True:
        enrolled_subjects = []
        subjects = [
            {'code': 'ML119', 'name': 'Machine Learning', 'credits': 4},
            {'code': 'CS102', 'name': 'Python Programming', 'credits': 4},
            {'code': 'DM111', 'name': 'Discrete Math', 'credits': 3},
            {'code': 'DAT101', 'name': 'Data Management', 'credits': 3},
            {'code': 'IA101', 'name': 'Introduction to AI', 'credits': 2},
        ]
        if currentID in studentID:
            menu = int(input('Menu\n1.Register Course\n2.Drop Courses\n3.Enrollment Status\n4.Exit\nSelect Option :'))
            if menu == 1:
                #show the available subject
                print('Available Subjects:')
                for subject in subjects:
                    print(f'{subject["code"]}: {subject["name"]} ({subject["credits"]} credits)')

                #insert registration for the subject
                print('\nEnroll in subjects by entering their codes (type "done" when finished):')

                while True:
                    code = input('Enter Subject code: ').upper()
                    if code == 'DONE':
                        print("The subjects code has been registered. You can view the data via menu option.")
                        break

                  #sub = next((s for s in subjects if s['code']==code), None)
                    #next is use to iterate the next element after going through the list
                    # if we dont use next
                    sub = None
                    for s in subjects:
                        if s['code'] == code:
                            sub = s
                            break
                    if sub not in enrolled_subjects:
                        enrolled_subjects.append(sub)
                        print (f'Enrolled in {sub['name']}')
                    elif sub in enrolled_subjects:
                        print('You are already enrolled in this subject.')
                    else:
                        print('Invalid code. Try again.')

            elif menu == 2:
                #removing subject
                while True:
                    code = input('Enter Subject code you wish to drop (type "done" when finished): ').upper()
                    if code == 'DONE':
                        print("The subjects code has been registered. You can view the data via menu option.")
                        break
                    sub = next((s for s in subjects if s['code'] == code), None)
                    if sub in enrolled_subjects:
                        enrolled_subjects.remove(sub)
                        print(f'Subject {sub['name']} removed.')
                    elif sub not in enrolled_subjects:
                        print('The subject is not in your registered course.')
                    else:
                        print('Invalid code. Try again.')

            elif menu == 3:
                print("\nYou are enrolled in the following subjects:")
                #supposedly count the total credits too
                total_credits = 0
                for subject in enrolled_subjects:
                    print(f"{subject['code']}: {subject['name']} ({subject['credits']} credits)")
                    total_credits += subject["credits"]

start_menu()
#Admin
#-Handle course
#-View report

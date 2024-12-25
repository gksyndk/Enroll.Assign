#DB
studentID=["A24AI0033","A24AI0044"]
adminID = "Admin123"
student_data = {}
enrolled_subjects = []
subjects = [
            {'code': 'ML119', 'name': 'Machine Learning', 'credits': 4},
            {'code': 'CS102', 'name': 'Python Programming', 'credits': 4},
            {'code': 'DM111', 'name': 'Discrete Math', 'credits': 3},
            {'code': 'DAT101', 'name': 'Data Management', 'credits': 3},
            {'code': 'IA101', 'name': 'Introduction to AI', 'credits': 2},
        ]
#Login Student or Admin
def login_admin_student():
    while True:#Loop for invalid menu and ID
        #Login Menu
        print("Menu\n1.Student\n2.Admin")
        signin = int(input("Select Option :"))
        if signin == 1:  # Student login
            student = input("Enter student ID: ").strip().upper()
            currentID = student
            if student in studentID:
                print("Welcome, Student:", student)
                student_menu(currentID)
            else:
                print("Invalid student ID. Please try again.")

        elif signin == 2:  # Admin login
            admin = input("Enter admin ID: ").strip()
            if admin == adminID:
                print("Welcome, Admin:", admin)
                admin_menu()
            else:
                print("Invalid admin ID. Please try again.")
        else:
            print("Invalid option. Please select 1 for Student or 2 for Admin.")

#Student Menu
def student_menu(currentID):
    total_credits = sum(sub["credits"] for sub in enrolled_subjects)
    max_credits = 12
    min_credits = 6
    while True:
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
                    #next is used to iterate the next element after going through the list
                    # if we dont use next
                    sub = None
                    for s in subjects:
                        if s['code'] == code:
                            sub = s
                            break

                    if sub not in enrolled_subjects:
                        enrolled_subjects.append(sub)
                        print (f"Enrolled in {sub['name']}")
                        total_credits += sub["credits"]
                        if total_credits > max_credits:
                            print(f"\nYou have exceeded the maximum credit limit ({max_credits}). Please remove some subjects.")
                        elif total_credits < min_credits:
                            print(f"\nYou need to enroll in at least {min_credits} credits. Please add more subjects.")

                    elif sub in enrolled_subjects:
                        print('You are already enrolled in this subject.')

                    else:
                        print('Invalid code. Try again.')

            elif menu == 2:
                #removing subject
                while True:
                    # show the current subject
                    print('Current Subjects:')
                    for subject in enrolled_subjects:
                        print(f'{subject["code"]}: {subject["name"]} ({subject["credits"]} credits)')
                    code = input('Enter Subject code you wish to drop (type "done" when finished): ').upper()
                    if code == 'DONE':
                        print("The subjects code has been registered. You can view the data via menu option.")
                        break
                    sub = next((s for s in subjects if s['code'] == code), None)
                    if sub in enrolled_subjects:
                        enrolled_subjects.remove(sub)
                        print(f"Subject {sub['name']} removed.")
                    elif sub not in enrolled_subjects:
                        print('The subject is not in your registered course.')
                    else:
                        print('Invalid code. Try again.')

            elif menu == 3:
                while True:
                    print("\nYou are enrolled in the following subjects:")

                    for subject in enrolled_subjects:
                        print(f"{subject['code']}: {subject['name']} ({subject['credits']} credits)")
                    print(f'Total Credits: {total_credits}')

                    exit_menu=int(input("Select 1 To Exit :"))
                    if exit_menu == 1:
                        break
            else:
                student_data[currentID] = {
                    "enrolled_subjects": enrolled_subjects,
                    "total_credits": total_credits,
                }
                print(f"Data saved for {currentID}. Exiting...")
                break

#Admin Menu
def admin_menu():
    while True:
        menu = int(input('Menu\n1.Manage Course\n2.View Students Enrollment\n3.Exit\nSelect Option :'))
        if menu == 1:
            print('The subjects available for this courses are:')
            for subject in subjects:
                print(f'{subject["code"]}: {subject["name"]} ({subject["credits"]} credits)')
            while True:
                action = input('1.Add Course\n2.Drop Course\n3.Exit\nSelect Option : ')
                if action == 1:
                    sub_to_add = input('Enter subject name: ')
                    code_to_add = input('Enter subject code: ')
                    credit_to_add = int(input('Enter subject credits: '))

                    if any(s['code'] == code_to_add for s in subjects):
                        print(f"Subject with code {code_to_add} already exists.")
                    else:
                        new_subject = {"code": code_to_add, "name": sub_to_add, "credits": credit_to_add}
                        subjects.append(new_subject)
                        print(f"Subject {sub_to_add} added successfully!")

                elif action == 2:
                    code_to_remove = input('Enter subject code: ')
                    sub_to_remove = None
                    for s in subjects:
                        if s['code'] == code_to_remove:
                            sub_to_remove = s
                            break
                    if sub_to_remove:
                        subjects.remove(sub_to_remove)
                    else:
                        print(f"Subject with code {code_to_remove} does not exist in the system.")

                elif action == 3:
                    break
                else:
                    print('Invalid option.')

            '''elif menu == 2:
                print("Student Enrollment Data:")
                for student_id, data in student_data.items():
                    print(f"Student ID: {student_id}\nEnrolled Subjects: ")
                    for course in data:
                          print(f"{course}")'''
        elif menu == 2:
            print("Student Enrollment Data:")
            for student_id, data in student_data.items():
                print(f"Student ID: \n{student_id}")
                print(f"{'Code':<8}{'Name':<20}{'Credit':<6}")  #
                print("-" * 35)
                for subject in data['enrolled_subjects']:
                    print(f"{subject['code']:<8}{subject['name']:<20}{subject['credits']:<6}")

        else:
            print('No such ID exists.')

login_admin_student()

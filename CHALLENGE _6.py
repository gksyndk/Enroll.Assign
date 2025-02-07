#DB
studentID = ["A24AI0033", "A24AI0044"]
adminID = "Admin123"
student_data = {}  # For ID,courseid,coursename,credit
subjects = [
    {'code': 'ML119', 'name': 'Machine Learning', 'credits': 4},
    {'code': 'CS102', 'name': 'Python Programming', 'credits': 4},
    {'code': 'DM111', 'name': 'Discrete Math', 'credits': 3},
    {'code': 'DAT101', 'name': 'Data Management', 'credits': 3},
    {'code': 'IA101', 'name': 'Introduction to AI', 'credits': 2},
]

# login student or admin
def login_admin_student():
    while True:
        # Login Menu
        print("Menu\n1.Student\n2.Admin")
        signin = int(input("Select Option :"))
        if signin == 1:  # student login
            student = input("Enter student ID: ").strip().upper()
            if student in studentID:
                print("Welcome, Student:", student)
                student_menu(student)
            else:
                print("Invalid student ID. Please try again.")

        elif signin == 2:  # admin login
            admin = input("Enter admin ID: ").strip()
            if admin == adminID:
                print("Welcome, Admin:", admin)
                admin_menu()
            else:
                print("Invalid admin ID. Please try again.")
        else:
            print("Invalid option. Please select 1 for Student or 2 for Admin.")

# student Menu
def student_menu(currentID):
    total_credits = 0  # track credit
    max_credits = 12
    min_credits = 6
    student_data[currentID] = {"enrolled_subjects": [], "total_credits": total_credits}

    while True:
        menu = int(input('Menu\n1.Register Course\n2.Drop Courses\n3.View Enrollment\n4.View Status\n5.Exit\nSelect Option :'))
        if menu == 1:
            # show the available subjects
            print('Available Subjects:')
            for subject in subjects:
                print(f'{subject["code"]}: {subject["name"]} ({subject["credits"]} credits)')

            # enroll subject
            print('\nEnroll in subjects by entering their codes (type "done" when finished):')

            while True:
                code = input('Enter Subject code: ').upper()
                if code == 'DONE':
                    print("The subjects code has been registered.")
                    break

                # find sub based on code
                sub = None
                for s in subjects:
                    if s['code'] == code:
                        sub = s
                        break

                if sub and sub not in student_data[currentID]["enrolled_subjects"]:
                    student_data[currentID]["enrolled_subjects"].append(sub)
                    student_data[currentID]["total_credits"] += sub["credits"]
                    print(f"Enrolled in {sub['name']}")

                    # check credit limits
                    if student_data[currentID]["total_credits"] > max_credits:
                        print(
                            f"\nYou have exceeded the maximum credit limit ({max_credits}). Please remove some subjects.")
                    elif student_data[currentID]["total_credits"] < min_credits:
                        print(f"\nYou need to enroll in at least {min_credits} credits. Please add more subjects.")
                elif sub in student_data[currentID]["enrolled_subjects"]:
                    print('You are already enrolled in this subject.')
                elif not sub:
                    print('Invalid code. Try again.')

        elif menu == 2:
            # remove subject
            while True:
                print('Current Subjects:')
                for subject in student_data[currentID]["enrolled_subjects"]:
                    print(f'{subject["code"]}: {subject["name"]} ({subject["credits"]} credits)')
                code = input('Enter Subject code you wish to drop (type "done" when finished): ').upper()
                if code == 'DONE':
                    print("The subjects code has been registered.")
                    break

                # find sub based on code
                sub = None
                for s in student_data[currentID]["enrolled_subjects"]:
                    if s['code'] == code:
                        sub = s
                        break
                if sub:
                    student_data[currentID]["enrolled_subjects"].remove(sub)
                    student_data[currentID]["total_credits"] -= sub["credits"]
                    print(f"Subject {sub['name']} removed.")
                else:
                    print('The subject is not in your registered courses.')

        elif menu == 3:
            # display status
            print("\nYou are enrolled in the following subjects:")
            for subject in student_data[currentID]["enrolled_subjects"]:
                print(f"{subject['code']}: {subject['name']} ({subject['credits']} credits)")
            print(f'Total Credits: {student_data[currentID]["total_credits"]}')

            exit_menu = int(input("Select 1 To Exit :"))
            if exit_menu == 1:
                pass

        elif menu == 4:
            # show status
            print("\nApproval Status of Registered Subjects:")
            for subject in student_data[currentID]["enrolled_subjects"]:
                print(f"{subject['code']}: {subject['name']} ({subject['credits']} credits)")

            total_credits = student_data[currentID]["total_credits"]
            if total_credits < 12:
                print(f"\nTotal Credits: {total_credits} - Status: APPROVED\n")
            else:
                print(f"\nTotal Credits: {total_credits} - Status: NOT APPROVED (Minimum 12 credits required)\n")

        elif menu == 5:
            break

        else:
            print("Invalid option.")

# admin Menu
def admin_menu():
    while True:
        menu = int(input('Menu\n1.Manage Course\n2.View Students Enrollment\n3.Report\n4.Logout\nSelect Option :'))
        if menu == 1:
            # manage courses (add/drop)
            print('The subjects available for this courses are:')
            for subject in subjects:
                print(f'{subject["code"]}: {subject["name"]} ({subject["credits"]} credits)')

            while True:
                action = input('1.Add Course\n2.Drop Course\n3.Exit\nSelect Option : ')
                if action == '1':
                    sub_to_add = input('Enter subject name: ')
                    code_to_add = input('Enter subject code: ')
                    credit_to_add = int(input('Enter subject credits: '))

                    if any(s['code'] == code_to_add for s in subjects):
                        print(f"Subject with code {code_to_add} already exists.")
                    else:
                        new_subject = {"code": code_to_add, "name": sub_to_add, "credits": credit_to_add}
                        subjects.append(new_subject)
                        print(f"Subject {sub_to_add} added successfully!")

                elif action == '2':
                    code_to_remove = input('Enter subject code: ')
                    sub_to_remove = None
                    for s in subjects:
                        if s['code'] == code_to_remove:
                            sub_to_remove = s
                            break
                    if sub_to_remove:
                        subjects.remove(sub_to_remove)
                        print(f"Subject {sub_to_remove['name']} removed.")
                    else:
                        print(f"Subject with code {code_to_remove} does not exist.")
                elif action == '3':
                    break
                else:
                    print('Invalid option.')

        elif menu == 2:
            # view all enrollments for each student
            print("\nStudent Enrollment Data:")

            # check if any student is enrolled in courses
            check_students = False

            # print each student's enrolled courses
            for student_id, data in student_data.items():
                if data['enrolled_subjects']:
                    check_students = True
                    print(f"\nStudent ID: {student_id}")
                    print(f"{'Code':<8}{'Name':<20}{'Credit':<6}")
                    print("-" * 35)
                    for subject in data['enrolled_subjects']:
                        print(f"{subject['code']:<8}{subject['name']:<20}{subject['credits']:<6}")
                    print("")

            if not check_students:
                print("No students have enrolled in any courses.")

        elif menu == 3:
            # num of student eah course
            print("\nReport on the number of students registered based on course\n")
            course_registration = {}

            # count num
            for student_id, data in student_data.items():
                for subject in data['enrolled_subjects']:
                    if subject['code'] not in course_registration:
                        course_registration[subject['code']] = 0
                    course_registration[subject['code']] += 1

            print(f"{'Code':<8}{'Name':<20}{'Registered Students':<20}")
            print("-" * 50)
            for subject in subjects:
                code = subject['code']
                name = subject['name']
                count = course_registration.get(code, 0)
                print(f"{code:<8}{name:<20}{count:<20}")

        elif menu == 4:
            break

        else:
            print("-Invalid Option-")

# run function
login_admin_student()

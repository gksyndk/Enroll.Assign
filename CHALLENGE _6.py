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

#Admin
#-Handle course
#-View report

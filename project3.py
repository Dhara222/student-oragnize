students = []
student_data = {}
subject_set= set()

print("Welcome to the student data Organizer!")

while True:
    print("\nSelect an option: ")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = int(input("\n Enter your choice: "))

    if choice==1:
        print("\n***add student***\n")
        print("\nEnter student details: ")
        student = int(input("student id: "))

        if student in student_data:
            print("student already exits")
        else:
            Name=input("Name: ")
            Age=int(input("Age: "))
            Grade=input("Grade: ")
            Date=input("Date of Birth (YYYY-MM-DD): ")
            Subjects=input("Subjects (comma-separated): ")

            Subjects= Subjects.split(" , ")
            Subjects=[Subject.strip() for Subject in Subjects]
            subject_set.update(Subjects)
            

            student_info = (student,Date)
            
            student_data={
            student :{
                    "info": student_info,
                     "name": Name,
                     "Age": Age,
                     "Grade": Grade,
                     "Date" : Date,
                     "Subjects": Subjects}}

            students.append(student_data)

            print("\n Student added Successfully \n")

            
    elif choice == 2:
         print("\n***Display All Students***\n")
         for student in students:
             for student_id, details in student.items():
                print(f"Student ID: {student_id} | Name: {details['name']} | Age: {details['Age']} | Grade: {details['Grade']} | Date: {details['Date']} | Subjects: {','.join(details['Subjects'])}")


    elif choice == 3:
         print("\n***Update student information***\n")
         student_id_input = int(input("Enter student ID: "))

         for student in students:
             for student_id, details in student.items():
                 if student_id == student_id_input:
                     new_name = input("Enter your New Name: ")
                     new_age = int(input("Enter your New Age: "))
                     new_grade = input("Enter your New Grade: ")
                     new_subjects= [Subject.strip()for Subject in input("Enter your New Subjects: ").split(" , ")]

                     details["name"] = new_name
                     details["Age"] = new_age
                     details["Grade"] = new_grade
                     details["Subjects"] = new_subjects
                     subject_set.update(new_subjects)
                    
                     print(f"\nStudent ID: {student_id}")
                     print(f"Name: {details['name']}")
                     print(f"Age: {details['Age']}")
                     print(f"Grade: {details['Grade']}")
                     print(f"Date: {details['Date']}")
                     print(f"Subjects: {details['Subjects']}")
                     print("\nYour information updated successfully")
         
    elif choice == 4:
        
        print("\n***Delete Student***\n")

        student_id_input = int(input("Enter student ID: "))

        for i in range(len(students)):
            for student_id in students[i]:
                if student_id == student_id_input:
                    del students[i]
                    print("\nStudent deleted successfully")
                    break
                
                    
    elif choice == 5:
        print("\n***Subjects Offered***\n")
        for subject in subject_set:
            print(subject)

    elif choice == 6:
        print("\nThank you! Program exited.")
        break
              
            

            
            
                         
           
            
            











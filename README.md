🎓 Student Data Organizer
A clean, efficient, and beginner-friendly Python application to manage student records with full CRUD functionality.

📸 Screenshots • 🎥 Video Demo • 🐛 Report Bug • ✨ Request Feature


📋 Table of Contents

Section	Section	Section
About	Features	Installation
Usage	Flowchart	Screenshots
Video	Tech Stack	Roadmap
Contributing	License	Author

🚀 About the Project
Student Data Organizer is a professional command-line application built with Python that provides a complete solution for managing student information. It offers a seamless experience for adding, viewing, updating, and deleting student records, while intelligently tracking all unique subjects offered across the institution.

This project is designed to demonstrate core Python programming concepts including data structures, control flow, and CRUD operations in a practical, real-world scenario.

✨ Features

🎯 Feature	📝 Description
➕ Add Student	Register new students with ID, Name, Age, Grade, DOB & Subjects

📋 Display Students	View comprehensive details of all registered students
✏️ Update Records	Modify student information with ease
🗑️ Delete Student	Remove records using unique student ID
📚 Subjects Tracker	Automatically track all unique subjects offered
🚪 Safe Exit	Gracefully terminate the program

🧠 Python Concepts Demonstrated


📋  List

A **list** is used to store student records.

Lists are **mutable**, which means their contents can be changed.

Example:
students = []
The project uses operations such as:
students.append(student_data)

and:
del students[i]
to add and remove student records.


📖  Dictionary

A dictionary stores information using key-value pairs.
The Student ID is used as the main key, while the student's information is stored inside the dictionary.
Example:
student_data = {
    102: {
        "name": "Dhara",
        "Age": 19,
        "Grade": "A",
        "Date": "2007-06-02",
        "Subjects": ["maths", "sci", "python"]
         }
       }
Dictionaries make it easy to access and update individual student information.


🔒  Tuple

A tuple is used to store the Student ID and Date of Birth together.
student_info = (student, Date)
Tuples are immutable, meaning their values cannot be changed after creation.

This demonstrates the difference between mutable and immutable data structures.



📚  Set

A set is used to maintain a collection of unique subjects.
subject_set = set()
Subjects are added using:
subject_set.update(Subjects)
A set automatically prevents duplicate subjects.


🔄  CRUD Operations

The application demonstrates the four basic CRUD operations:
CRUD
Application Feature
Create
Add Student
Read
Display All Students
Update
Update Student Information
Delete
Delete Student


🔢  Type Casting

Since input() returns data as a string, type casting is used when numerical values are required.
Example:
student = int(input("Student ID: "))
Age = int(input("Age: "))
Here, int() converts the user's input into an integer.


✂️  String Manipulation

The project processes comma-separated subjects using split() and strip().
Subjects = Subjects.split(",")
Subjects = [Subject.strip() for Subject in Subjects]
For example:
maths, sci, python
is converted into:
["maths", "sci", "python"]


🔁 Control Flow

The project uses several Python control-flow concepts:

~ while loop →   keeps the main menu running
~ for loop →   searches and displays student records
~ if / elif →   handles different menu choices
~ break →   exits the program

📁 Project Structure

📦 Student-Data-Organizer
 ┣ 📜 main.py                # Main program file
 ┣ 📜 README.md              # Project documentation
 ┣ 📂 screenshots/           # Application screenshots
 ┗ 📂 assets/                # Flowchart and other assets


🎮 Usage
Upon launching the application, you'll be presented with an interactive menu:


╔══════════════════════════════════════╗
║   WELCOME TO STUDENT DATA ORGANIZER  ║
╠══════════════════════════════════════╣
║  1. Add Student                      ║
║  2. Display All Students             ║
║  3. Update Student Information       ║
║  4. Delete Student                   ║
║  5. Display Subjects Offered         ║
║  6. Exit                             ║
╚══════════════════════════════════════╝
Simply enter the corresponding number to perform your desired action.

📊 Program Flowchart

(<img width="6979" height="3081" alt="picture" src="https://github.com/user-attachments/assets/a4262b71-6ee8-4610-9ea0-785efdbc34ea" />)


📸 Screenshots

🔗 Click Here to View All Screenshots

🎬 Video Demonstration

🔗 Click Here to Watch Full Demo Video


🧰 Tech Stack

Technology	        Purpose

🐍 Python       Programming language
💻 CLI          User interface
📋 List         Store student records
📖 Dictionary   Store student information
🔒 Tuple        Store ID and DOB
📚 Set          Track unique subjects

🗺️ Roadmap

☑ ✅ Add student records
☑ ✅ Display all students
☑ ✅ Update student information
☑ ✅ Delete student records
☑ ✅ Track unique subjects
☑ ✅ Implement menu-driven interface
☑ ✅ Add program flowchart 
☑ ✅ Create project documentation

🤝 Contributing
Contributions make the open-source community an amazing place to learn and grow. Any contributions you make are greatly appreciated.

👨‍💻 Author
Dhara

Made with ❤️ using Python

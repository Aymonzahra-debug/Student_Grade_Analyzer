import os
import numpy as np
import re  # For input validation


USER_DATA_FILE = "users.txt"
STUDENT_DATA_FILE = "students.npy"  # Student data saved in numpy file

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_users():
    users = {}
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    username, password = line.split(",")
                    users[username] = password
    return users

def save_user(username, password):
    with open(USER_DATA_FILE, "a") as f:
        f.write(f"{username},{password}\n")

def signup(users):
    clear_screen()
    print("\n=== Signup ===")
    username = input("Choose a username: ").strip()
    if username in users:
        print("Username already exists! Try logging in.\n")
        return None
    password = input("Choose a password: ").strip()
    users[username] = password
    save_user(username, password)
    print("Signup successful! You can now login.\n")
    return username

def login(users):
    clear_screen()
    print("\n=== Login ===")
    username = input("Enter username: ").strip()
    if username not in users:
        print("User not found! Please signup first.\n")
        return None
    password = input("Enter password: ").strip()
    if users[username] == password:
        print(f"Login successful! Welcome {username}.\n")
        return username
    else:
        print("Incorrect password! Try again.\n")
        return None

def calculate_grade_gpa(marks):
    if 85 <= marks <= 100:
        return 'A', 4.0
    elif 80 <= marks <= 84:
        return 'A-', 3.7
    elif 75 <= marks <= 79:
        return 'B+', 3.3
    elif 71 <= marks <= 74:
        return 'B', 3.0
    elif 68 <= marks <= 70:
        return 'B-', 2.7
    elif 64 <= marks <= 67:
        return 'C+', 2.3
    elif 61 <= marks <= 63:
        return 'C', 2.0
    elif 58 <= marks <= 60:
        return 'C-', 1.7
    elif 54 <= marks <= 57:
        return 'D+', 1.3
    elif 50 <= marks <= 53:
        return 'D', 1.0
    else:
        return 'F', 0.0

def load_students():
    if os.path.exists(STUDENT_DATA_FILE):
        try:
            data = np.load(STUDENT_DATA_FILE, allow_pickle=True).item()
            if isinstance(data, dict):
                return data
            else:
                print("Error: Data in students.npy is not a dictionary.")
                return {}
        except Exception as e:
            print(f"Error loading students file: {e}")
            return {}
    return {}

def save_students(students):
    try:
        np.save(STUDENT_DATA_FILE, students)
    except Exception as e:
        print(f"Error saving students file: {e}")

students = load_students()

def validate_roll(roll):
    return re.fullmatch(r'\d+', roll) is not None

def add_student():
    clear_screen()
    print("=== Add Student ===")
    roll = input("Enter student roll number (digits only): ").strip()
    if not validate_roll(roll):
        print("Invalid roll number! Use digits only.\n")
        input("Press Enter to continue...")
        return
    if roll in students:
        print("Student already exists!\n")
        input("Press Enter to continue...")
        return
    name = input("Enter student name: ").strip()
    try:
        marks = float(input("Enter student marks (0-100): "))
        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.\n")
            input("Press Enter to continue...")
            return
    except ValueError:
        print("Invalid marks input.\n")
        input("Press Enter to continue...")
        return
    grade, gpa = calculate_grade_gpa(marks)
    students[roll] = {"name": name, "marks": marks, "grade": grade, "gpa": gpa}
    save_students(students)
    print(f"Student {name} added successfully with grade {grade} and GPA {gpa}.\n")
    input("Press Enter to continue...")

def edit_student():
    clear_screen()
    print("=== Edit Student Info ===")
    roll = input("Enter student roll number to edit: ").strip()
    if roll not in students:
        print("Student not found.\n")
        input("Press Enter to continue...")
        return
    student = students[roll]
    print(f"Current Name: {student['name']}")
    new_name = input("Enter new name (press Enter to keep current): ").strip()
    if new_name:
        student['name'] = new_name
    print(f"Current Marks: {student['marks']}")
    try:
        new_marks_input = input("Enter new marks (0-100) (press Enter to keep current): ").strip()
        if new_marks_input:
            new_marks = float(new_marks_input)
            if new_marks < 0 or new_marks > 100:
                print("Marks must be between 0 and 100.\n")
                input("Press Enter to continue...")
                return
            student['marks'] = new_marks
            student['grade'], student['gpa'] = calculate_grade_gpa(new_marks)
    except ValueError:
        print("Invalid marks input.\n")
        input("Press Enter to continue...")
        return
    students[roll] = student
    save_students(students)
    print("Student info updated successfully.\n")
    input("Press Enter to continue...")

def delete_student():
    clear_screen()
    print("=== Delete Student ===")
    roll = input("Enter student roll number to delete: ").strip()
    if roll in students:
        del students[roll]
        save_students(students)
        print("Student deleted successfully.\n")
    else:
        print("Student not found.\n")
    input("Press Enter to continue...")

def search_student():
    clear_screen()
    print("=== Search Student ===")
    roll = input("Enter student roll number to search: ").strip()
    if roll in students:
        s = students[roll]
        print(f"Roll: {roll}, Name: {s['name']}, Marks: {s['marks']}, Grade: {s['grade']}, GPA: {s['gpa']}\n")
    else:
        print("Student not found.\n")
    input("Press Enter to continue...")

def view_report():
    clear_screen()
    if not students:
        print("No students to show.\n")
        input("Press Enter to continue...")
        return
    print("\n=== Student Report ===")
    print(f"{'Roll':<10}{'Name':<20}{'Marks':<10}{'Grade':<8}{'GPA':<5}")
    print("-" * 55)
    for roll, s in students.items():
        print(f"{roll:<10}{s['name']:<20}{s['marks']:<10}{s['grade']:<8}{s['gpa']:<5}")
    print()
    input("Press Enter to continue...")

def main_menu():
    while True:
        clear_screen()
        print("Main Menu:")
        print("1. Add Student")
        print("2. Edit Student Info")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. View Report")
        print("6. Logout")
        choice = input("Enter choice (1-6): ").strip()

        if choice == '1':
            add_student()
        elif choice == '2':
            edit_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            search_student()
        elif choice == '5':
            view_report()
        elif choice == '6':
            print("Logging out...\n")
            break
        else:
            print("Invalid choice. Please try again.\n")
            input("Press Enter to continue...")

def start_program():
    users = load_users()
    while True:
        clear_screen()
        print("Welcome! Please select:")
        print("1. Login")
        print("2. Signup")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ").strip()

        if choice == "1":
            user = login(users)
            if user:
                main_menu()
        elif choice == "2":
            signup(users)
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")
            input("Press Enter to continue...")

if __name__ == "__main__":
    start_program()
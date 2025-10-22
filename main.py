import os
import hashlib
import json
from datetime import datetime

DATA_DIR = "data"
STUDENTS_FILE = os.path.join(DATA_DIR, "students.txt")
COURSES_FILE = os.path.join(DATA_DIR, "courses.txt")
ENROLLMENTS_FILE = os.path.join(DATA_DIR, "enrollments.txt")

def ensure_data_directory():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_students():
    if not os.path.exists(STUDENTS_FILE):
        return {}
    students = {}
    with open(STUDENTS_FILE, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                data = json.loads(line)
                students[data['student_number']] = data
    return students

def save_students(students):
    with open(STUDENTS_FILE, 'w') as f:
        for student in students.values():
            f.write(json.dumps(student) + '\n')

def load_courses():
    if not os.path.exists(COURSES_FILE):
        return {}
    courses = {}
    with open(COURSES_FILE, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                data = json.loads(line)
                courses[data['course_code']] = data
    return courses

def save_courses(courses):
    with open(COURSES_FILE, 'w') as f:
        for course in courses.values():
            f.write(json.dumps(course) + '\n')

def load_enrollments():
    if not os.path.exists(ENROLLMENTS_FILE):
        return {}
    enrollments = {}
    with open(ENROLLMENTS_FILE, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                data = json.loads(line)
                student_num = data['student_number']
                if student_num not in enrollments:
                    enrollments[student_num] = []
                enrollments[student_num].append(data)
    return enrollments

def save_enrollments(enrollments):
    with open(ENROLLMENTS_FILE, 'w') as f:
        for student_enrollments in enrollments.values():
            for enrollment in student_enrollments:
                f.write(json.dumps(enrollment) + '\n')

def authenticate_student(student_number, email, password):
    students = load_students()
    if student_number in students:
        student = students[student_number]
        if student['email'] == email and student['password'] == hash_password(password):
            return student
    return None

def validate_email(email, student_number):
    expected_email = f"{student_number}@mocku.edu.ph"
    return email == expected_email

def add_course():
    print("\n=== ADD NEW COURSE ===")
    courses = load_courses()
    
    course_code = input("Enter Course Code: ").strip().upper()
    if course_code in courses:
        print(f"Error: Course {course_code} already exists!")
        return
    
    department = input("Enter Department: ").strip()
    try:
        units = int(input("Enter Units: ").strip())
    except ValueError:
        print("Error: Units must be a number!")
        return
    
    course_name = input("Enter Course Name: ").strip()
    
    courses[course_code] = {
        'course_code': course_code,
        'department': department,
        'units': units,
        'course_name': course_name
    }
    
    save_courses(courses)
    print(f"\nCourse {course_code} added successfully!")

def update_course():
    print("\n=== UPDATE COURSE ===")
    courses = load_courses()
    
    if not courses:
        print("No courses available to update.")
        return
    
    print("\nAvailable Courses:")
    for code, course in courses.items():
        print(f"{code}: {course['course_name']} - {course['department']} ({course['units']} units)")
    
    course_code = input("\nEnter Course Code to update: ").strip().upper()
    if course_code not in courses:
        print(f"Error: Course {course_code} not found!")
        return
    
    print(f"\nCurrent details for {course_code}:")
    course = courses[course_code]
    print(f"Course Name: {course['course_name']}")
    print(f"Department: {course['department']}")
    print(f"Units: {course['units']}")
    
    print("\nEnter new values (press Enter to keep current value):")
    
    new_name = input(f"Course Name [{course['course_name']}]: ").strip()
    new_dept = input(f"Department [{course['department']}]: ").strip()
    new_units = input(f"Units [{course['units']}]: ").strip()
    
    if new_name:
        course['course_name'] = new_name
    if new_dept:
        course['department'] = new_dept
    if new_units:
        try:
            course['units'] = int(new_units)
        except ValueError:
            print("Invalid units value, keeping current value.")
    
    save_courses(courses)
    print(f"\nCourse {course_code} updated successfully!")

def delete_course():
    print("\n=== DELETE COURSE ===")
    courses = load_courses()
    
    if not courses:
        print("No courses available to delete.")
        return
    
    print("\nAvailable Courses:")
    for code, course in courses.items():
        print(f"{code}: {course['course_name']} - {course['department']} ({course['units']} units)")
    
    course_code = input("\nEnter Course Code to delete: ").strip().upper()
    if course_code not in courses:
        print(f"Error: Course {course_code} not found!")
        return
    
    confirm = input(f"Are you sure you want to delete {course_code}? (yes/no): ").strip().lower()
    if confirm == 'yes':
        del courses[course_code]
        save_courses(courses)
        print(f"\nCourse {course_code} deleted successfully!")
    else:
        print("Deletion cancelled.")

def view_available_courses():
    print("\n=== AVAILABLE COURSES ===")
    courses = load_courses()
    
    if not courses:
        print("No courses available.")
        return
    
    print(f"\n{'Code':<10} {'Course Name':<30} {'Department':<20} {'Units':<6}")
    print("-" * 70)
    for code, course in sorted(courses.items()):
        print(f"{code:<10} {course['course_name']:<30} {course['department']:<20} {course['units']:<6}")

def enroll_in_course(student):
    print("\n=== ENROLL IN COURSE ===")
    courses = load_courses()
    enrollments = load_enrollments()
    
    if not courses:
        print("No courses available for enrollment.")
        return
    
    student_num = student['student_number']
    enrolled_courses = [e['course_code'] for e in enrollments.get(student_num, [])]
    
    print("\nAvailable Courses:")
    available = False
    for code, course in sorted(courses.items()):
        if code not in enrolled_courses:
            print(f"{code}: {course['course_name']} - {course['department']} ({course['units']} units)")
            available = True
    
    if not available:
        print("You are already enrolled in all available courses.")
        return
    
    course_code = input("\nEnter Course Code to enroll: ").strip().upper()
    
    if course_code not in courses:
        print(f"Error: Course {course_code} not found!")
        return
    
    if course_code in enrolled_courses:
        print(f"Error: You are already enrolled in {course_code}!")
        return
    
    if student_num not in enrollments:
        enrollments[student_num] = []
    
    enrollments[student_num].append({
        'student_number': student_num,
        'course_code': course_code,
        'enrollment_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    
    save_enrollments(enrollments)
    print(f"\nSuccessfully enrolled in {course_code}!")

def view_my_courses(student):
    print("\n=== MY ENROLLED COURSES ===")
    courses = load_courses()
    enrollments = load_enrollments()
    
    student_num = student['student_number']
    student_enrollments = enrollments.get(student_num, [])
    
    if not student_enrollments:
        print("You are not enrolled in any courses yet.")
        return
    
    print(f"\n{'Code':<10} {'Course Name':<30} {'Department':<20} {'Units':<6} {'Enrolled On':<20}")
    print("-" * 90)
    
    total_units = 0
    for enrollment in student_enrollments:
        course_code = enrollment['course_code']
        if course_code in courses:
            course = courses[course_code]
            print(f"{course_code:<10} {course['course_name']:<30} {course['department']:<20} {course['units']:<6} {enrollment['enrollment_date']:<20}")
            total_units += course['units']
    
    print("-" * 90)
    print(f"Total Units: {total_units}")

def student_menu(student):
    while True:
        print(f"\n{'='*50}")
        print(f"STUDENT ENROLLMENT SYSTEM")
        print(f"{'='*50}")
        print(f"Logged in as: {student['name']} ({student['student_number']})")
        print(f"Year: {student['year']} | Degree: {student['degree']}")
        print(f"{'='*50}")
        print("\n1. View Available Courses")
        print("2. Enroll in Course")
        print("3. View My Enrolled Courses")
        print("4. Logout")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            view_available_courses()
        elif choice == '2':
            enroll_in_course(student)
        elif choice == '3':
            view_my_courses(student)
        elif choice == '4':
            print("\nLogging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def course_management_menu():
    while True:
        print(f"\n{'='*50}")
        print("COURSE MANAGEMENT")
        print(f"{'='*50}")
        print("\n1. View All Courses")
        print("2. Add Course")
        print("3. Update Course")
        print("4. Delete Course")
        print("5. Back to Main Menu")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            view_available_courses()
        elif choice == '2':
            add_course()
        elif choice == '3':
            update_course()
        elif choice == '4':
            delete_course()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    ensure_data_directory()
    
    while True:
        print(f"\n{'='*50}")
        print("STUDENT ENROLLMENT SYSTEM")
        print(f"{'='*50}")
        print("\n1. Student Login")
        print("2. Course Management")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            print("\n=== STUDENT LOGIN ===")
            student_number = input("Enter Student Number: ").strip()
            email = input("Enter Email (format: [student_number]@mocku.edu.ph): ").strip()
            password = input("Enter Password: ").strip()
            
            if not validate_email(email, student_number):
                print("\nError: Email must be in format [student_number]@mocku.edu.ph")
                print(f"Expected: {student_number}@mocku.edu.ph")
                continue
            
            student = authenticate_student(student_number, email, password)
            if student:
                print(f"\nWelcome, {student['name']}!")
                student_menu(student)
            else:
                print("\nInvalid credentials. Please try again.")
        
        elif choice == '2':
            course_management_menu()
        
        elif choice == '3':
            print("\nThank you for using the Student Enrollment System!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

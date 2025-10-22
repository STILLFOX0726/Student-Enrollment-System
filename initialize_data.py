import os
import json
import hashlib

DATA_DIR = "data"
STUDENTS_FILE = os.path.join(DATA_DIR, "students.txt")
COURSES_FILE = os.path.join(DATA_DIR, "courses.txt")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def initialize_students():
    students = [
        {
            'student_number': '2021001',
            'name': 'Juan dela Cruz',
            'year': '3rd Year',
            'degree': 'BS Computer Science',
            'email': '2021001@mocku.edu.ph',
            'password': hash_password('password123')
        },
        {
            'student_number': '2021002',
            'name': 'Maria Santos',
            'year': '2nd Year',
            'degree': 'BS Information Technology',
            'email': '2021002@mocku.edu.ph',
            'password': hash_password('password123')
        },
        {
            'student_number': '2021003',
            'name': 'Pedro Reyes',
            'year': '4th Year',
            'degree': 'BS Computer Engineering',
            'email': '2021003@mocku.edu.ph',
            'password': hash_password('password123')
        },
        {
            'student_number': '2022001',
            'name': 'Ana Garcia',
            'year': '2nd Year',
            'degree': 'BS Computer Science',
            'email': '2022001@mocku.edu.ph',
            'password': hash_password('password123')
        },
        {
            'student_number': '2022002',
            'name': 'Carlos Mendoza',
            'year': '1st Year',
            'degree': 'BS Information Technology',
            'email': '2022002@mocku.edu.ph',
            'password': hash_password('password123')
        }
    ]
    
    with open(STUDENTS_FILE, 'w') as f:
        for student in students:
            f.write(json.dumps(student) + '\n')
    
    print(f"Created {len(students)} student records")

def initialize_courses():
    courses = [
        {
            'course_code': 'CS101',
            'course_name': 'Introduction to Programming',
            'department': 'Computer Science',
            'units': 3
        },
        {
            'course_code': 'CS201',
            'course_name': 'Data Structures and Algorithms',
            'department': 'Computer Science',
            'units': 3
        },
        {
            'course_code': 'CS301',
            'course_name': 'Database Management Systems',
            'department': 'Computer Science',
            'units': 3
        },
        {
            'course_code': 'IT101',
            'course_name': 'Web Development Fundamentals',
            'department': 'Information Technology',
            'units': 3
        },
        {
            'course_code': 'IT201',
            'course_name': 'Network Administration',
            'department': 'Information Technology',
            'units': 3
        },
        {
            'course_code': 'CE101',
            'course_name': 'Digital Logic Design',
            'department': 'Computer Engineering',
            'units': 4
        },
        {
            'course_code': 'MATH101',
            'course_name': 'Calculus I',
            'department': 'Mathematics',
            'units': 3
        },
        {
            'course_code': 'ENG101',
            'course_name': 'Technical Writing',
            'department': 'English',
            'units': 2
        }
    ]
    
    with open(COURSES_FILE, 'w') as f:
        for course in courses:
            f.write(json.dumps(course) + '\n')
    
    print(f"Created {len(courses)} course records")

def main():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    
    print("Initializing Student Enrollment System Database...")
    print("-" * 50)
    
    initialize_students()
    initialize_courses()
    
    print("-" * 50)
    print("\nDatabase initialized successfully!")
    print("\nSample Student Credentials:")
    print("  Student Number: 2021001, Password: password123")
    print("  Student Number: 2021002, Password: password123")
    print("  Student Number: 2021003, Password: password123")
    print("  Student Number: 2022001, Password: password123")
    print("  Student Number: 2022002, Password: password123")
    print("\nEmail format: [student_number]@mocku.edu.ph")

if __name__ == "__main__":
    main()

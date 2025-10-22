# Student Enrollment System

A Python 3.x command-line application for managing student enrollments with text file-based data storage.

## Features

### Student Login
- Secure authentication using Student Number and Password
- Email format: `[student_number]@mocku.edu.ph`
- Password hashing with SHA-256

### Student Information
- Student Number
- Name
- Year Level
- Undergraduate Degree

### Course Management
- **Add Course**: Create new courses with course code, department, units, and name
- **Update Course**: Modify existing course information
- **Delete Course**: Remove courses from the system
- **View Courses**: Display all available courses

### Course Information
- Course Code
- Course Name
- Department
- Units

### Student Enrollment
- View available courses
- Enroll in courses
- View enrolled courses with total units

## Setup and Installation

### Prerequisites
- Python 3.x

### Initial Setup

1. Initialize the database with sample data:
```bash
python initialize_data.py
```

This creates:
- 5 sample student records
- 8 sample courses

2. Run the application:
```bash
python main.py
```

## Usage

### Student Login Credentials

| Student Number | Password | Name | Year | Degree |
|---|---|---|---|---|
| 2021001 | password123 | Juan dela Cruz | 3rd Year | BS Computer Science |
| 2021002 | password123 | Maria Santos | 2nd Year | BS Information Technology |
| 2021003 | password123 | Pedro Reyes | 4th Year | BS Computer Engineering |
| 2022001 | password123 | Ana Garcia | 2nd Year | BS Computer Science |
| 2022002 | password123 | Carlos Mendoza | 1st Year | BS Information Technology |

### Main Menu Options

1. **Student Login**: Access student enrollment interface
2. **Course Management**: Add, update, or delete courses
3. **Exit**: Close the application

### Student Menu

After logging in, students can:
1. View Available Courses
2. Enroll in Course
3. View My Enrolled Courses
4. Logout

### Course Management Menu

1. View All Courses
2. Add Course
3. Update Course
4. Delete Course
5. Back to Main Menu

## Data Storage

All data is stored in text files using JSON format:

- `data/students.txt`: Student records
- `data/courses.txt`: Course catalog
- `data/enrollments.txt`: Student enrollments

## Project Structure

```
.
├── main.py                 # Main application
├── initialize_data.py      # Database initialization script
├── README.md              # This file
└── data/                  # Data directory (created automatically)
    ├── students.txt       # Student records
    ├── courses.txt        # Course catalog
    └── enrollments.txt    # Enrollment records
```

## Sample Courses

- **CS101**: Introduction to Programming (CS, 3 units)
- **CS201**: Data Structures and Algorithms (CS, 3 units)
- **CS301**: Database Management Systems (CS, 3 units)
- **IT101**: Web Development Fundamentals (IT, 3 units)
- **IT201**: Network Administration (IT, 3 units)
- **CE101**: Digital Logic Design (CE, 4 units)
- **MATH101**: Calculus I (Math, 3 units)
- **ENG101**: Technical Writing (English, 2 units)

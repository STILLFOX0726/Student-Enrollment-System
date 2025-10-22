# Student Enrollment System

## Overview

A command-line student enrollment management system built with Python 3.x. The application enables students to authenticate, view available courses, enroll in courses, and manage their academic information. The system uses a file-based data storage approach with JSON-formatted text files for persistence, making it lightweight and easy to deploy without database dependencies.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Data Storage Architecture

**File-Based JSON Storage**: The application uses plain text files with JSON line format (one JSON object per line) for data persistence.

- **Problem**: Need for simple, portable data storage without external database dependencies
- **Solution**: Three separate text files in a `data/` directory:
  - `students.txt` - Student records with credentials
  - `courses.txt` - Course catalog
  - `enrollments.txt` - Student-course enrollment relationships
- **Rationale**: Eliminates setup complexity, enables version control of data, and ensures portability across systems
- **Trade-offs**: 
  - Pros: Zero configuration, human-readable, easy backup
  - Cons: No ACID guarantees, poor scalability, manual file locking needed for concurrent access

### Authentication System

**SHA-256 Password Hashing**: Student passwords are hashed using SHA-256 before storage.

- **Problem**: Secure credential storage and authentication
- **Solution**: Hash passwords with SHA-256 before storing in student records
- **Security Model**: 
  - Email format enforced as `[student_number]@mocku.edu.ph`
  - Authentication requires matching student number, email, and password hash
- **Trade-offs**:
  - Pros: Better than plaintext, built into Python standard library
  - Cons: SHA-256 alone is not ideal for passwords (no salt, fast computation enables brute force)

### Data Model

**Student Entity**:
- `student_number` (unique identifier)
- `name`
- `year` (e.g., "3rd Year")
- `degree` (e.g., "BS Computer Science")
- `email` (derived from student number)
- `password` (SHA-256 hash)

**Course Entity**:
- `course_code` (unique identifier, e.g., "CS101")
- `course_name`
- `department`
- `units` (credit hours)

**Enrollment Entity**:
- `student_number` (foreign key to student)
- `course_code` (foreign key to course)
- `enrollment_date` (timestamp)

### Application Structure

**Modular Function Design**: Core functionality separated into distinct functions for data loading, saving, and business logic.

- **Problem**: Organize code for a CLI application with multiple operations
- **Solution**: 
  - `main.py` - Core application logic and data operations
  - `initialize_data.py` - Database seeding with sample data
  - `test_system.py` - Test suite for authentication and data loading
- **Pattern**: Functional programming approach with stateless utility functions
- **Data Flow**: Load from files → Process in memory → Save back to files

### Initialization System

**Sample Data Seeding**: Provides pre-populated data for testing and demonstration.

- **Included Data**:
  - 5 sample students across different years and programs
  - 8 sample courses covering CS, IT, CE, Math, and English departments
- **Default Credentials**: All sample students use password `password123`

## External Dependencies

### Standard Library Only

The application uses only Python 3.x standard library modules:

- **os**: File system operations and path management
- **json**: JSON serialization/deserialization for data storage
- **hashlib**: SHA-256 password hashing
- **datetime**: Timestamp generation for enrollment records

**Design Decision**: No external dependencies ensures maximum portability and minimal setup requirements. The application can run on any system with Python 3.x installed without pip or package management.

### File System Requirements

- Write access to create `data/` directory
- Read/write permissions for `.txt` files in data directory
- No database server or network services required
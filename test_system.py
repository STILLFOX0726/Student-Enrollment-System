import os
import json
from main import (
    load_students, load_courses, load_enrollments,
    authenticate_student, hash_password,
    save_courses, save_enrollments
)

def test_student_authentication():
    print("\n=== Testing Student Authentication ===")
    
    student = authenticate_student('2021001', '2021001@mocku.edu.ph', 'password123')
    if student:
        print(f"✓ Authentication successful for {student['name']}")
        print(f"  Email: {student['email']}")
        print(f"  Year: {student['year']}")
        print(f"  Degree: {student['degree']}")
    else:
        print("✗ Authentication failed")
        return False
    
    invalid = authenticate_student('2021001', '2021001@mocku.edu.ph', 'wrongpassword')
    if not invalid:
        print("✓ Invalid password correctly rejected")
    else:
        print("✗ Invalid password incorrectly accepted")
        return False
    
    wrong_email = authenticate_student('2021001', 'wrong@mocku.edu.ph', 'password123')
    if not wrong_email:
        print("✓ Invalid email correctly rejected")
    else:
        print("✗ Invalid email incorrectly accepted")
        return False
    
    return True

def test_course_loading():
    print("\n=== Testing Course Loading ===")
    
    courses = load_courses()
    print(f"✓ Loaded {len(courses)} courses")
    
    if len(courses) > 0:
        sample = list(courses.values())[0]
        print(f"  Sample: {sample['course_code']} - {sample['course_name']}")
        print(f"  Department: {sample['department']}, Units: {sample['units']}")
    
    return len(courses) > 0

def test_student_loading():
    print("\n=== Testing Student Loading ===")
    
    students = load_students()
    print(f"✓ Loaded {len(students)} students")
    
    if len(students) > 0:
        sample = list(students.values())[0]
        print(f"  Sample: {sample['student_number']} - {sample['name']}")
        print(f"  Email format: {sample['email']}")
    
    expected_email_format = "@mocku.edu.ph"
    all_valid = all(expected_email_format in s['email'] for s in students.values())
    
    if all_valid:
        print(f"✓ All student emails use {expected_email_format} format")
    else:
        print(f"✗ Some student emails don't use {expected_email_format} format")
        return False
    
    return len(students) > 0

def test_course_crud():
    print("\n=== Testing Course CRUD Operations ===")
    
    courses = load_courses()
    original_count = len(courses)
    
    test_course = {
        'course_code': 'TEST101',
        'course_name': 'Test Course',
        'department': 'Testing',
        'units': 3
    }
    
    courses['TEST101'] = test_course
    save_courses(courses)
    print("✓ Course added")
    
    courses = load_courses()
    if 'TEST101' in courses:
        print("✓ Course persisted to file")
    else:
        print("✗ Course not found after reload")
        return False
    
    courses['TEST101']['course_name'] = 'Updated Test Course'
    save_courses(courses)
    print("✓ Course updated")
    
    courses = load_courses()
    if courses['TEST101']['course_name'] == 'Updated Test Course':
        print("✓ Update persisted to file")
    else:
        print("✗ Update not saved correctly")
        return False
    
    del courses['TEST101']
    save_courses(courses)
    print("✓ Course deleted")
    
    courses = load_courses()
    if 'TEST101' not in courses:
        print("✓ Deletion persisted to file")
    else:
        print("✗ Course still exists after deletion")
        return False
    
    if len(courses) == original_count:
        print(f"✓ Course count restored to {original_count}")
    
    return True

def test_enrollment():
    print("\n=== Testing Enrollment Functionality ===")
    
    enrollments = load_enrollments()
    
    test_enrollment = {
        'student_number': '2021001',
        'course_code': 'CS101',
        'enrollment_date': '2025-10-22 00:00:00'
    }
    
    if '2021001' not in enrollments:
        enrollments['2021001'] = []
    
    original_count = len(enrollments.get('2021001', []))
    
    enrollments['2021001'].append(test_enrollment)
    save_enrollments(enrollments)
    print("✓ Enrollment added")
    
    enrollments = load_enrollments()
    if '2021001' in enrollments and len(enrollments['2021001']) > original_count:
        print("✓ Enrollment persisted to file")
        
        enrolled_courses = [e['course_code'] for e in enrollments['2021001']]
        if 'CS101' in enrolled_courses:
            print("✓ Correct course enrolled")
        else:
            print("✗ Course not found in enrollments")
            return False
    else:
        print("✗ Enrollment not saved correctly")
        return False
    
    return True

def test_data_file_format():
    print("\n=== Testing Data File Format ===")
    
    files = ['data/students.txt', 'data/courses.txt']
    
    for file_path in files:
        if os.path.exists(file_path):
            print(f"✓ {file_path} exists")
            
            with open(file_path, 'r') as f:
                lines = f.readlines()
                if len(lines) > 0:
                    try:
                        data = json.loads(lines[0].strip())
                        print(f"  ✓ Valid JSON format")
                    except json.JSONDecodeError:
                        print(f"  ✗ Invalid JSON format")
                        return False
        else:
            print(f"✗ {file_path} does not exist")
            return False
    
    return True

def main():
    print("="*60)
    print("STUDENT ENROLLMENT SYSTEM - AUTOMATED TESTS")
    print("="*60)
    
    tests = [
        ("Data File Format", test_data_file_format),
        ("Student Loading", test_student_loading),
        ("Course Loading", test_course_loading),
        ("Student Authentication", test_student_authentication),
        ("Course CRUD Operations", test_course_crud),
        ("Enrollment Functionality", test_enrollment)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n✗ {test_name} failed with error: {e}")
            results.append((test_name, False))
    
    print("\n" + "="*60)
    print("TEST RESULTS SUMMARY")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status}: {test_name}")
    
    print("-"*60)
    print(f"Total: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed successfully!")
    else:
        print(f"\n⚠ {total - passed} test(s) failed")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)

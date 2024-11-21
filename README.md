Student Management System API
This is a Student Management System built using Django and Django Rest Framework (DRF). It includes various modules such as User Management, Student Profiles, Course Management, Grades, Attendance, and Notifications. The system supports role-based access for different types of users (Admin, Teacher, Student).

Features
User Management: Registration, login, and role-based access control (Admin, Teacher, Student).
Student Profile: Manage student profiles including personal information.
Course Management: Create courses, assign instructors, and enroll students.
Grade Management: Assign grades to students and view their performance.
Attendance Management: Mark student attendance and view attendance records.
Notifications: Send and manage notifications to users about important events.
Installation & Setup
Prerequisites
Python 3.8+
Django 3.2+
Django Rest Framework
PostgreSQL/MySQL (or SQLite for development)
Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/student-management-system.git
cd student-management-system
Install Dependencies
bash
Copy code
pip install -r requirements.txt
Configure Database
Make sure to configure your database settings in settings.py. If you are using SQLite for development, the default configuration should work.

Run Migrations
bash
Copy code
python manage.py migrate
Create a Superuser (Admin)
bash
Copy code
python manage.py createsuperuser
Run the Development Server
bash
Copy code
python manage.py runserver
API Endpoints
Authentication & User Management
POST /api/users/register/
Description: Register a new user (Student, Teacher, or Admin).
Request Body:
json
Copy code
{
    "username": "user123",
    "password": "password123",
    "email": "user@example.com",
    "role": "student"  // roles: "student", "teacher", "admin"
}
POST /api/users/login/
Description: Login and get a JWT token.
Request Body:
json
Copy code
{
    "username": "user123",
    "password": "password123"
}
GET /api/users/me/
Description: View the logged-in user's profile.
Response:
json
Copy code
{
    "id": 1,
    "username": "user123",
    "email": "user@example.com",
    "role": "student"
}
PUT /api/users/me/
Description: Update the logged-in user's profile (e.g., change name, email, etc.).
Request Body:
json
Copy code
{
    "first_name": "New Name"
}
Student Profile Management
GET /api/students/profile/
Description: View the student's profile (only accessible by the logged-in student or an admin).
Response:
json
Copy code
{
    "user": {
        "id": 1,
        "username": "student1",
        "email": "student@example.com",
        "role": "student"
    },
    "dob": "2000-01-01",
    "registration_date": "2020-05-01"
}
POST /api/students/profile/
Description: Create or update the student's profile.
Request Body:
json
Copy code
{
    "dob": "1999-12-31"
}
Course Management
GET /api/courses/
Description: View all courses (Teachers can see their own, Admins can see all courses).
Response:
json
Copy code
[
    {
        "id": 1,
        "name": "Math 101",
        "description": "Basic Math Course",
        "instructor": {
            "id": 1,
            "username": "teacher1",
            "role": "teacher"
        }
    }
]
POST /api/courses/
Description: Create a new course (only accessible by Admins or Teachers).
Request Body:
json
Copy code
{
    "name": "Math 101",
    "description": "Basic Math Course",
    "instructor": 1  // Instructor's user ID
}
POST /api/courses/enrollments/
Description: Enroll a student in a course (only accessible by Teachers or Admins).
Request Body:
json
Copy code
{
    "student": 1,  // Student's user ID
    "course": 1    // Course ID
}
GET /api/courses/enrollments/
Description: View all enrollments for a course (Teachers can see enrollments for their courses).
Response:
json
Copy code
[
    {
        "student": {
            "id": 1,
            "username": "student1"
        },
        "course": {
            "id": 1,
            "name": "Math 101"
        },
        "enrollment_date": "2020-01-01"
    }
]
Grade Management
POST /api/grades/
Description: Assign a grade to a student for a course (only accessible by Teachers or Admins).
Request Body:
json
Copy code
{
    "student": 1,
    "course": 1,
    "grade": "A"
}
GET /api/grades/
Description: View grades for courses (Teachers see their students' grades, Admins see all grades).
Response:
json
Copy code
[
    {
        "student": {
            "id": 1,
            "username": "student1"
        },
        "course": {
            "id": 1,
            "name": "Math 101"
        },
        "grade": "A",
        "date": "2020-01-01"
    }
]
GET /api/grades/student/
Description: View the logged-in student's grades.
Response:
json
Copy code
[
    {
        "course": {
            "id": 1,
            "name": "Math 101"
        },
        "grade": "A",
        "date": "2020-01-01"
    }
]
Attendance Management
POST /api/attendance/records/
Description: Mark attendance for students (only accessible by Teachers or Admins).
Request Body:
json
Copy code
{
    "student": 1,
    "course": 1,
    "date": "2020-01-01",
    "status": "present"
}
GET /api/attendance/records/
Description: View attendance records (Teachers see their courses' attendance, Admins see all records).
Response:
json
Copy code
[
    {
        "student": {
            "id": 1,
            "username": "student1"
        },
        "course": {
            "id": 1,
            "name": "Math 101"
        },
        "date": "2020-01-01",
        "status": "present"
    }
]
GET /api/attendance/student/
Description: View the logged-in student's attendance.
Response:
json
Copy code
[
    {
        "course": {
            "id": 1,
            "name": "Math 101"
        },
        "date": "2020-01-01",
        "status": "present"
    }
]
Notification Management
GET /api/notifications/
Description: View all notifications for the logged-in user.
Response:
json
Copy code
[
    {
        "id": 1,
        "recipient": "student1",
        "title": "New Grade Available",
        "message": "You have received a grade for Math 101.",
        "is_read": false,
        "created_at": "2024-01-01T12:00:00Z"
    }
]
POST /api/notifications/create/
Description: Send a new notification (only accessible by Admins or Teachers).
Request Body:
json
Copy code
{
    "recipient": 1,  // Recipient's user ID
    "title": "New Assignment",
    "message": "There is a new assignment for you in Math 101."
}
POST /api/notifications/<id>/mark-read/
Description: Mark a notification as read.
Response:
json
Copy code
{
    "message": "Notification marked as read"
}
Conclusion
This API allows managing a full-fledged Student Management System, from user registration to course enrollment, attendance tracking, grades, and notifications. Each module is designed with role-based access to ensure proper data management.

Let me know if you have any questions or need further clarification on any of the endpoints!

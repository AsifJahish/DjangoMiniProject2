# Student Management System API

This is a **Student Management System** built using **Django** and **Django Rest Framework (DRF)**. It includes various modules such as **User Management**, **Student Profiles**, **Course Management**, **Grades**, **Attendance**, and **Notifications**. The system supports role-based access for different types of users (Admin, Teacher, Student).

## Features

- **User Management**: Registration, login, and role-based access control (Admin, Teacher, Student).
- **Student Profile**: Manage student profiles including personal information.
- **Course Management**: Create courses, assign instructors, and enroll students.
- **Grade Management**: Assign grades to students and view their performance.
- **Attendance Management**: Mark student attendance and view attendance records.
- **Notifications**: Send and manage notifications to users about important events.

## Installation & Setup

### Prerequisites
- Python 3.8+
- Django 3.2+
- Django Rest Framework
- PostgreSQL/MySQL (or SQLite for development)







# Student Management System API

## API Endpoints

### User Management
- **POST `/api/users/register/`** - Register a user.
- **POST `/api/users/login/`** - Login and get JWT token.
- **GET `/api/users/me/`** - View logged-in user profile.
- **PUT `/api/users/me/`** - Update logged-in user profile.

### Student Profile
- **GET `/api/students/profile/`** - View student profile.
- **POST `/api/students/profile/`** - Create or update student profile.

### Course Management
- **GET `/api/courses/`** - View courses (Teachers/Admin).
- **POST `/api/courses/`** - Create a new course (Teachers/Admin).
- **POST `/api/courses/enrollments/`** - Enroll a student in a course.
- **GET `/api/courses/enrollments/`** - View course enrollments (Teachers/Admin).

### Grade Management
- **POST `/api/grades/`** - Assign a grade to a student.
- **GET `/api/grades/`** - View grades (Teachers/Admin).
- **GET `/api/grades/student/`** - View logged-in student's grades.

### Attendance Management
- **POST `/api/attendance/records/`** - Mark attendance for a student.
- **GET `/api/attendance/records/`** - View attendance records (Teachers/Admin).
- **GET `/api/attendance/student/`** - View logged-in student's attendance.

### Notification Management
- **GET `/api/notifications/`** - View notifications for the logged-in user.
- **POST `/api/notifications/create/`** - Create a new notification (Teachers/Admin).
- **POST `/api/notifications/<id>/mark-read/`** - Mark a notification as read.

---

## Conclusion

This **Student Management System API** covers user registration, course management, grades, attendance, and notifications, with role-based access to ensure proper data handling. Each module is integrated and secured for admin, teacher, and student use.

For more details or assistance, feel free to contact me!








### Clone the Repository

```bash
git clone https://github.com/yourusername/student-management-system.git
cd student-management-system





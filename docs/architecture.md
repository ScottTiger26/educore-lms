# EduCore-LMS Wireframe Overview

> This document provides text-based wireframes for the EduCore-LMS platform. These can be refined into real UI mockups using tools like Figma or Excalidraw.

## 1. Auth & Landing

### Landing Page

- **Navbar**
  - EduCore Logo
  - Login button
  - Register button
- **Hero Section**
  - Tagline: "Learn. Teach. Grow."
  - CTA: "Explore Courses"
- **Footer**
  - Links
  - Contact information

### Login Form

- Email input field
- Password input field
- Login button
- "Forgot Password?" link
- "Sign up" link

### Register Form

- Name input field
- Email input field
- Password input field
- Role selection (Student / Instructor)
- Sign up button

---

## 2. Student Dashboard

### Sidebar Navigation

- Dashboard
- My Courses
- Explore Courses
- Notifications
- Profile

### Main Dashboard

- **Welcome Message**: "Welcome, [Student Name] 👋"
- **Progress Bar**: Shows progress for enrolled courses
- **Recommended Courses**: ML-driven course recommendations
- **Recent Notifications**: Latest updates and alerts

---

## 3. Instructor Dashboard

### Sidebar Navigation

- Dashboard
- My Courses
- Create Course
- Manage Students
- Payments
- Notifications
- Profile

### Main Dashboard

- **Statistics**
  - Number of Students
  - Revenue
  - Active Courses
- **Quick Action**: "Create New Course" button
- **Student Feedback & Ratings**: Recent reviews and ratings

---

## 4. Course Page

### Course Header

- Course Title
- Instructor Name

### Tabs

- **Overview**: Course description, learning outcomes
- **Lessons**: List of course modules and lessons
- **Discussions**: Forum for student discussions
- **Resources**: Downloadable materials and links

### Action Buttons

- Enroll button (for new students)
- Continue button (for enrolled students)

### Sidebar

- Lessons Progress tracker

---

## 5. Payment Page

### Checkout Form

- **Course Information**
  - Course Name
  - Price
- **Payment Methods**
  - Stripe integration
  - Razorpay integration
- **Billing Information Form**
  - Name
  - Address
  - Card details
- **Pay Now Button**

---

## 6. Admin / Tenant Dashboard

> For organizations managing multiple users and courses

### Sidebar Navigation

- Dashboard
- Users
- Courses
- Payments
- Settings

### Main Dashboard

- **Manage Tenants**: Organization management
- **Add Instructors / Students**: User management
- **Org-wide Analytics**: Platform-wide statistics and insights

---

## 7. Notification System

### Notifications Panel

Examples of notification types:

- "Your payment was successful"
- "New lesson added: Module 3"
- "Assignment deadline tomorrow"

---

## 🌐 Wireframe to Folder Structure Mapping

This section maps the wireframes above to the backend folder structure:

| Wireframe Section | Backend Folder | Description |
|-------------------|----------------|-------------|
| Auth & Landing | `users/` | Login, Register, Profile, Roles (student, instructor, admin) |
| Student/Instructor Dashboard | `courses/` | Course CRUD, lessons, resources, progress tracking |
| Payment Page | `payments/` | Payment flow (checkout, success, refunds) |
| Notification System | `notifications/` | Notification panel (email, in-app, SMS) |
| Admin/Tenant Dashboard | `tenants/` | Admin dashboard for multi-org setup |
| Recommended Courses | `ml/` | ML-driven course recommendations on dashboard |

---

## Next Steps

1. Convert these wireframes to high-fidelity mockups
2. Implement frontend components based on these designs
3. Ensure responsive design for mobile and tablet devices
4. Conduct user testing and iterate on the designs
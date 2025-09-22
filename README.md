# EduCore LMS

EduCore LMS is a full-stack Learning Management System built with **Django (DRF)** and **React**.  
It will support authentication, authorization, RBAC, payments, notifications, Redis, Celery, and more.  
Eventually, we’ll evolve it into a **microservices architecture** with Docker & Kubernetes.

---

## 📌 Milestones

### Milestone 1 (Current)
- Setup project structure (backend + frontend).
- Create initial Django + React apps.
- Initialize Git and documentation.

### Milestone 2
- Implement Authentication (JWT, Login, Register, Password Reset).
- RBAC (roles & permissions).
- Postgres DB setup with ORM.

### Milestone 3
- Course Management (CRUD).
- API integration with React frontend.
- File uploads (media, PDFs, images).

### Milestone 4
- Redis + Celery (notifications, async tasks).
- Payment/Subscription system.
- Dockerize services.

### Milestone 5
- Move towards microservices.
- API Gateway, SSO/OAuth, Multi-tenant support.

### Milestone 6
- Deployment (Docker, Kubernetes, CI/CD).
- Autoscaling + monitoring.

---

## ⚡ Tech Stack

- **Backend**: Django, Django REST Framework  
- **Frontend**: React (Vite migration later)  
- **Database**: PostgreSQL  
- **Cache/Queue**: Redis + Celery  
- **Deployment**: Docker, Kubernetes  

---

## 🚀 Quickstart

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver

# Expense Tracker — Django Web App

A simple expense tracking web application built with Django.

## Features
- Custom user authentication (register, login, logout)
- Full CRUD for expenses (create, view, edit, delete)
- Users can only see/edit their own expenses
- Filter expenses by category
- Monthly expense total displayed on dashboard
- Flash messages for all actions

## Setup Instructions

### 1. Clone the repository
git clone <your-github-url>
cd expense_tracker

### 2. Install dependencies
pip install django

### 3. Run migrations
python manage.py makemigrations
python manage.py migrate

### 4. Create superuser (optional)
python manage.py createsuperuser

### 5. Start the server
python manage.py runserver

### 6. Open in browser
http://127.0.0.1:8000/

## Testing the Application
1. Go to /register/ and create an account
2. Login at /login/
3. Add an expense at /expenses/create/
4. Edit it using the Edit button
5. Delete it using the Delete button
6. Filter by category using the dropdown

## Approach
- Django class-based views for clean, organized code
- Custom User Model (AbstractUser) for extensibility
- ModelForm with custom validation for title and amount
- LoginRequiredMixin protects all expense views
- ForeignKey ensures users only access their own data
- Django messages framework for user feedback

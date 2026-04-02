# 💸 Expense Tracker — Django Web App

A personal finance web application built with Django. Authenticated users can track their expenses and income, filter by category, and monitor monthly savings.

## Features

- Custom user authentication (register, login, logout)
- Full CRUD for expenses (create, view, edit, delete)
- Income tracking with monthly and all-time summaries
- Savings calculation (income − expenses)
- Filter expenses by category
- Monthly expense total on the dashboard
- Flash messages for all user actions
- Responsive UI built with Bootstrap 5

## Tech Stack

- **Backend:** Django 6, Python 3.13
- **Database:** SQLite
- **Frontend:** Bootstrap 5, Bootstrap Icons

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/bikrant0/expense_tracker.git
cd expense_tracker
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create a superuser (optional)
```bash
python manage.py createsuperuser
```

### 5. Start the server
```bash
python manage.py runserver
```

### 6. Open in browser
```
http://127.0.0.1:8000/
```

## Testing the Application

1. Go to `/register/` and create a new account
2. You will be automatically logged in and redirected to `/expenses/`
3. Add an expense at `/expenses/create/`
4. Edit an expense using the ✏️ button in the table
5. Delete an expense using the 🗑️ button (with confirmation)
6. Filter expenses by category using the dropdown
7. Visit `/income/` to add income and view savings summary
8. Logout via the navbar button

## Project Structure
```
expense_tracker/
├── expense_tracker/       # Project settings and URLs
│   ├── settings.py
│   └── urls.py
├── expenses/              # Main app
│   ├── models.py          # CustomUser, Expense, Income models
│   ├── views.py           # Class-based views
│   ├── forms.py           # ModelForms with validation
│   ├── urls.py            # App-level URL patterns
│   └── templates/
│       ├── base.html      # Shared navbar and layout
│       ├── registration/  # Login and register pages
│       └── expenses/      # Expense and income templates
├── requirements.txt
└── README.md
```

## Approach

- **Class-based views** for clean, organized, reusable code
- **Custom User Model** (`AbstractUser` with UUID primary key) for security and extensibility
- **ModelForms** with custom validation — title cannot be empty, amount must be > 0
- **`LoginRequiredMixin`** protects all expense and income views
- **ForeignKey** on Expense and Income ensures users can only access their own data
- **Django messages framework** provides feedback on every create, update, and delete action
- **Bootstrap 5** for a consistent, responsive UI across all pages

## Bonus Features Implemented

- ✅ Filter expenses by category (`/expenses/?category=Food`)
- ✅ Registration page for new users
- ✅ Monthly expense total on the dashboard
- ✅ Income tracking and savings calculation (monthly + all-time)
# NoteVault – Backend

Django + Django REST Framework + PostgreSQL backend for the Notes Management App.

## Tech Stack
- **Python** 3.10+
- **Django** 5.0
- **Django REST Framework** 3.15
- **djangorestframework-simplejwt** – JWT authentication
- **django-cors-headers**
- **django-environ** 
- **django-filter**

## Setup (Local)

```bash
# 1. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment (edit .env if needed)
# Default uses SQLite – ready to run without PostgreSQL

# 4. Run migrations
python manage.py makemigrations notes
python manage.py migrate

# 5. (Optional) Create superuser for admin panel
python manage.py createsuperuser

# 6. Start server
python manage.py runserver
```

## PostgreSQL Setup (Production)

Update `.env`:
```env
DATABASE_URL=postgres://notes_user:yourpassword@localhost:5432/notes_db
```

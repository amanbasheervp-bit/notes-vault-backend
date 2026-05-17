# NoteVault – Backend

Django + Django REST Framework + PostgreSQL backend for the Notes Management App.

## Tech Stack
- **Python** 3.10+
- **Django** 5.0
- **Django REST Framework** 3.15
- **djangorestframework-simplejwt** – JWT authentication
- **django-cors-headers** – CORS support
- **django-environ** – Environment variable management
- **django-filter** – Advanced filtering

## API Endpoints

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/api/auth/register/` | ❌ | Register new user |
| POST | `/api/auth/login/` | ❌ | Obtain JWT tokens |
| POST | `/api/auth/token/refresh/` | ❌ | Refresh access token |
| GET | `/api/auth/me/` | ✅ | Get current user info |
| GET | `/api/notes/` | ✅ | List notes (supports `?search=`, `?category=`) |
| POST | `/api/notes/` | ✅ | Create note |
| GET | `/api/notes/<id>/` | ✅ | Get note detail |
| PUT | `/api/notes/<id>/` | ✅ | Update note |
| PATCH | `/api/notes/<id>/` | ✅ | Partial update |
| DELETE | `/api/notes/<id>/` | ✅ | Delete note |

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

Backend runs at: **http://127.0.0.1:8000**

## PostgreSQL Setup (Production)

Update `.env`:
```env
DATABASE_URL=postgres://notes_user:yourpassword@localhost:5432/notes_db
```

# rest_server

This folder contains a minimal Django project (`server`) and an app (`apiapp`) demonstrating Django REST Framework with validators, caching, filtering, and pagination.

Quick setup (Windows PowerShell):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt; cd rest_server; python manage.py migrate; python manage.py runserver
```

The API is available at http://127.0.0.1:8000/api/items/

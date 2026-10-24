# REST-CRUD-API-Dynamic Formatting

A tiny RESTful API built with Python and Flask. It serves a hard-coded list of books with full CRUD support and includes an HTML view that highlights top-rated books.

## Files

- `app.py`: the Flask application
- `reflection.md`: my written reflection on the assignment

## Run it

```bash
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install Flask
python3 app.py
```

The app runs at `http://127.0.0.1:5000`.

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/goodbooks` | List all books (JSON) |
| GET | `/goodbooks/<id>` | Get one book |
| POST | `/goodbooks` | Add a book |
| PUT | `/goodbooks/<id>` | Update a book |
| DELETE | `/goodbooks/<id>` | Delete a book |
| GET | `/goodbooks/html` | Table view with loading and error handling; ratings of 4.8 or higher are highlighted green |

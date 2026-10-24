from flask import Flask, jsonify, request, abort, Response

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Data model: hard-coded, in-memory (resets whenever the server restarts)
# ---------------------------------------------------------------------------
books = [
    {"id": 1, "title": "1984", "author": "George Orwell", "rating": 4.9},
    {"id": 2, "title": "Brave New World", "author": "Aldous Huxley", "rating": 4.3},
    {"id": 3, "title": "Fahrenheit 451", "author": "Ray Bradbury", "rating": 4.7},
    {"id": 4, "title": "True Grit", "author": "Charles Portis", "rating": 4.2},
]

HIGHLIGHT_THRESHOLD = 4.8  # rows at or above this rating are shaded green


def find_book(book_id):
    return next((b for b in books if b["id"] == book_id), None)


@app.route("/")
def welcome():
    return jsonify(message="Welcome to Tiny REST App!"), 200


# ---------------------------------------------------------------------------
# CRUD endpoints (renamed from /books to /goodbooks)
# ---------------------------------------------------------------------------
@app.route("/goodbooks", methods=["GET"])
def get_books():
    return jsonify(books), 200


@app.route("/goodbooks/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = find_book(book_id)
    if not book:
        abort(404, description="Book not found")
    return jsonify(book), 200


@app.route("/goodbooks", methods=["POST"])
def add_book():
    data = request.get_json(silent=True)
    if not data or "title" not in data or "author" not in data:
        abort(400, description="Missing required fields")
    new_id = max(b["id"] for b in books) + 1 if books else 1
    book = {
        "id": new_id,
        "title": data["title"],
        "author": data["author"],
        "rating": data.get("rating", 0),
    }
    books.append(book)
    return jsonify(book), 201


@app.route("/goodbooks/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.get_json(silent=True) or {}
    book = find_book(book_id)
    if not book:
        abort(404, description="Book not found")
    book.update({k: v for k, v in data.items() if k in ["title", "author", "rating"]})
    return jsonify(book), 200


@app.route("/goodbooks/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    global books
    if not find_book(book_id):
        abort(404, description="Book not found")
    books = [b for b in books if b["id"] != book_id]
    return "", 204


# ---------------------------------------------------------------------------
# HTML view: /goodbooks/html
# The page fetches /goodbooks (the JSON API), shows a loading message,
# handles errors, and renders a table with conditional row styling.
# ---------------------------------------------------------------------------
PAGE = """<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Good Books</title>
  <style>
    body { font-family: sans-serif; margin: 2rem; }
    table { border-collapse: collapse; }
    th, td { border: 1px solid #333; padding: 6px 12px; text-align: left; }
    .good { background-color: lightgreen; }
    #status { margin: 1rem 0; }
    .error { color: #b00020; font-weight: bold; }
  </style>
</head>
<body>
  <h1>Good Books</h1>
  <p id="status">Loading books...</p>
  <table id="books" hidden>
    <thead><tr><th>ID</th><th>Title</th><th>Author</th><th>Rating</th></tr></thead>
    <tbody></tbody>
  </table>

  <script>
    const THRESHOLD = __THRESHOLD__;
    const status = document.getElementById("status");
    const table = document.getElementById("books");

    fetch("/goodbooks")
      .then(res => {
        if (!res.ok) throw new Error("Server returned " + res.status);
        return res.json();
      })
      .then(data => {
        const tbody = table.querySelector("tbody");
        data.forEach(book => {
          const tr = document.createElement("tr");
          if (book.rating >= THRESHOLD) tr.className = "good";
          [book.id, book.title, book.author, book.rating].forEach(value => {
            const td = document.createElement("td");
            td.textContent = value;   // textContent avoids HTML injection
            tr.appendChild(td);
          });
          tbody.appendChild(tr);
        });
        status.textContent = data.length ? "" : "No books found.";
        table.hidden = data.length === 0;
      })
      .catch(err => {
        status.textContent = "Could not load books: " + err.message;
        status.className = "error";
      });
  </script>
</body>
</html>
"""


@app.route("/goodbooks/html")
def books_html():
    html = PAGE.replace("__THRESHOLD__", str(HIGHLIGHT_THRESHOLD))
    return Response(html, mimetype="text/html")


if __name__ == "__main__":
    app.run(debug=True)

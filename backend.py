from flask import Flask, jsonify


app = Flask(__name__)


books = [
    {"id": 0, "title": "Harry Potter", "author": "J.K. Rowling", "year": 1997},
    {"id": 1, "title": "The Hobbit",  "author": "J.R.R. Tolkien", "year": 1937},
    {"id": 2, "title": "1984",        "author": "George Orwell",  "year": 1949},
]


@app.get("/books/<int:index>")
def get_book(index):
    if 0 <= index < len(books):
        return jsonify(books[index])

    return jsonify({"error": "not found"}), 404


def start_backend():
    app.run(host="0.0.0.0", port=5000)

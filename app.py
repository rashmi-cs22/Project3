from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
DATA_FILE = 'data/books.json'

if not os.path.exists('data'):
    os.makedirs('data')

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

def load_books():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_books(books):
    with open(DATA_FILE, 'w') as f:
        json.dump(books, f, indent=4)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        books = load_books()
        new_book = {
            'title': request.form['title'],
            'author': request.form['author'],
            'year': request.form['year']
        }
        books.append(new_book)
        save_books(books)
        return redirect(url_for('view_books'))
    return render_template('add_book.html')

@app.route('/view')
def view_books():
    books = load_books()
    return render_template('view_books.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)

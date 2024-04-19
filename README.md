# Dutch Flashcards

This project is a flashcard application that helps users learn Dutch vocabulary by providing flashcards from the Nederlands in actie book.

## Features
- Basic flashcard feature
- User performance graph for words

## Usage
- From python console:
```
from app import app, db, Flashcard, UserPerformance

with app.app_context():
    db.create_all()
```
- From shell: 
```
python3 populate_db.py
```
- From sqlite3 console in the db: (to set all values to 0 if they are null)
```
UPDATE flashcards SET correct_count = COALESCE(correct_count, 0), incorrect_count = COALESCE(incorrect_count, 0);
```

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Flashcard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dutch_word = db.Column(db.String(80), unique=True, nullable=False)
    english_translation = db.Column(db.String(120), unique=False, nullable=False)
    correct_count = db.Column(db.Integer, default=0)
    incorrect_count = db.Column(db.Integer, default=0)


@app.route('/')
def index():
    # Get the first flashcard
    flashcard = Flashcard.query.first()

   # Get the correct and incorrect counts for this flashcard
    correct_count = flashcard.correct_count
    incorrect_count = flashcard.incorrect_count

    # Render the template with the flashcard and stats
    return render_template('index.html', flashcard=flashcard, stats={'correct_count': correct_count, 'incorrect_count': incorrect_count})

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    flashcard_id = data['flashcard_id']
    correct = data['correct']

    # Get the flashcard
    flashcard = Flashcard.query.get(flashcard_id)

    # Update the correct or incorrect count
    if correct:
        flashcard.correct_count += 1
    else:
        flashcard.incorrect_count += 1

    # Commit the changes to the database
    db.session.commit()

    # Get the next flashcard
    next_flashcard = Flashcard.query.order_by(func.random()).first()

    # Serialize the flashcard data to JSON
    next_flashcard_data = {
        'id': next_flashcard.id,
        'dutch_word': next_flashcard.dutch_word,
        'english_translation': next_flashcard.english_translation
    }

    return jsonify(flashcard=next_flashcard_data)

if __name__ == '__main__':
    app.run(debug=True)
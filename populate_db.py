import pandas as pd
from sqlalchemy import create_engine
from app import app

# Create SQLAlchemy engine
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

# Read CSV file into DataFrame
df = pd.read_csv('Nederlands in actie/Hoofdstuk 1/woorden.csv', names=['dutch_word', 'english_translation'])

# Write DataFrame to SQLite database
df.to_sql('flashcard', engine, if_exists='append', index=False)

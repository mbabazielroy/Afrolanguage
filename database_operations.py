import sqlite3
# Function to create the database and tables if they don't exist
def create_database():
    conn = sqlite3.connect('language_learner.db')
    cursor = conn.cursor()

    # Create a table for language progress
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            language TEXT NOT NULL,
            category TEXT NOT NULL,
            flashcard_count INTEGER DEFAULT 0,
            quiz_score INTEGER DEFAULT 0
        )
    ''')

    conn.commit()
    conn.close()

# Function to insert or update user progress
def save_progress(language, category, flashcard_count, quiz_score):
    conn = sqlite3.connect('language_learner.db')
    cursor = conn.cursor()

    # Check if a record for this language and category already exists
    cursor.execute('''
        SELECT * FROM progress WHERE language=? AND category=?
    ''', (language, category))

    existing_record = cursor.fetchone()

    if existing_record:
        # Update the existing record
        cursor.execute('''
            UPDATE progress SET flashcard_count=?, quiz_score=? WHERE id=?
        ''', (flashcard_count, quiz_score, existing_record[0]))
    else:
        # Insert a new record
        cursor.execute('''
            INSERT INTO progress (language, category, flashcard_count, quiz_score) VALUES (?, ?, ?, ?)
        ''', (language, category, flashcard_count, quiz_score))

    conn.commit()
    conn.close()

# Function to retrieve user progress for a specific language and category
def get_progress(language, category):
    conn = sqlite3.connect('language_learner.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT flashcard_count, quiz_score FROM progress WHERE language=? AND category=?
    ''', (language, category))

    progress = cursor.fetchone()

    conn.close()

    return progress

# Example usage
if __name__ == '__main__':
    create_database()

    # Simulate user progress
    language = 'Spanish'
    category = 'Animals'
    flashcard_count = 15
    quiz_score = 80

    save_progress(language, category, flashcard_count, quiz_score)

    # Retrieve user progress
    user_progress = get_progress(language, category)
    if user_progress:
        print(f"Flashcard Count: {user_progress[0]}, Quiz Score: {user_progress[1]}")
    else:
        print("No progress found for the selected language and category.")

# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

# Import the functions from database_operations.py
from database_operations import create_database, save_progress, get_progress

# Connect to the database and create tables
create_database()

# Simulate user progress
language = 'Spanish'
category = 'Animals'
flashcard_count = 15
quiz_score = 80

save_progress(language, category, flashcard_count, quiz_score)

# Retrieve user progress
user_progress = get_progress(language, category)
if user_progress is not None:
    flashcard_count, quiz_score = user_progress
    print(f"Flashcard Count: {flashcard_count}, Quiz Score: {quiz_score}")
else:
    print("No progress found for the selected language and category.")

# Dummy data for language selection and flashcards
supported_languages = [ "English","Luganda", "Runyankole", "Swahili"]
vocabulary_categories = {
    "English": ["Animals", "Food", "Colors"],
    "Luganda": ["E'bsolo", "E'mele", "kalamu"],
    "Runyankole": ["Animaux", "Nourriture", "Couleurs"],
    "Swahili":["Mamba ni Mbuzi", "Chapati ya N"]
}

class AfroLanguageLearnerApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Initialize the flashcard layout here
        self.flashcard_layout = GridLayout(cols=2, spacing=10)
    def build(self):
        # Create the main layout
        layout = BoxLayout(orientation="vertical")

        # Language selection screen
        language_selection_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        language_selection_layout.bind(minimum_height=language_selection_layout.setter("height"))

        # Create buttons for each supported language
        for language in supported_languages:
            language_btn = Button(text=language, size_hint_y=None, height=40)
            language_btn.bind(on_press=self.on_language_selected)
            language_selection_layout.add_widget(language_btn)

        # Add the language selection screen to the main layout
        layout.add_widget(language_selection_layout)

        # Add the flashcard view to the main layout
        layout.add_widget(self.flashcard_layout)

        # Bind the main layout to be displayed
        return layout


    def on_language_selected(self, instance):
        # Function to handle language selection
        selected_language = instance.text
        # Replace this with logic to load flashcards and display them based on the selected language
        self.show_flashcards(selected_language)

    def show_flashcards(self, language):
        # Function to load and display flashcards for the selected language
        self.flashcard_layout.clear_widgets()
        flashcards = self.get_flashcards(language)
        for word, image_path in flashcards:
            self.flashcard_layout.add_widget(Label(text=word))
            self.flashcard_layout.add_widget(Label(text=image_path))

    def get_flashcards(self, language):
        # Function to fetch flashcard data from the database for the selected language
        # Replace this with actual database retrieval logic
        # In a real app, you'd have tables for languages, categories, words, and images in the SQLite database
        # Here, we use dummy data
        return [
            ("Cat", "images/cat.png"),
            ("Apple", "images/apple.png"),
            ("Red", "images/red.png"),
        ]
if __name__ == "__main__":
    AfroLanguageLearnerApp().run()

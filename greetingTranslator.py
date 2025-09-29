import tkinter as tk
from tkinter import ttk

# --- 1. Define the Action Function ---
def show_greeting(language_key):
    """
    Updates the output label with a greeting based on the selected language key.
    We use the English name (the key) to look up the greeting.
    """
    greetings = {
        "English": "Hello!",
        "Spanish": "¡Hola!",
        "French": "Bonjour!",
        "German": "Hallo!"
    }
    
    # Get the greeting for the selected language key
    greeting_message = greetings.get(language_key, "Greeting not found.")
    
    # Update the text of the output_label
    output_label.config(text=f"The greeting is: {greeting_message}")

# --- 2. Set Up the Main Window ---
root = tk.Tk()
root.title("Language Greeter (Authentic Labels)")
root.geometry("350x300") 

# --- 3. Create Widgets ---

# A. Welcome Message (Label)
welcome_label = ttk.Label(root, text="Welcome! Select a language for a greeting:", font=('Arial', 12, 'bold'))
welcome_label.pack(pady=15)

# C. Language Buttons
# Now, the list contains tuples: (Button Label, Function Argument/Key)
languages_to_display = [
    ("English", "English"),
    ("Español", "Spanish"),
    ("Français", "French"),
    ("Deutsch", "German")
] 

for button_label, language_key in languages_to_display:
    # Use 'button_label' for the button's text
    # Pass 'language_key' to the show_greeting function
    button = ttk.Button(
        root, 
        text=button_label, 
        command=lambda lk=language_key: show_greeting(lk)
    )
    # Arrange in a column, all the same width
    button.pack(pady=5, padx=50, fill=tk.X) 

# D. Output Display (Label)
output_label = ttk.Label(root, text="Click a button to see a greeting.", font=('Arial', 11, 'italic'))
output_label.pack(pady=20) 

# --- 4. Start the Main Loop ---
root.mainloop()
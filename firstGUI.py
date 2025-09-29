import tkinter as tk
from tkinter import ttk

# --- 1. Define the Action Function ---
def process_input():
    # Get the text from the Entry widget
    input_text = entry.get()

    # Simple logic: Convert the text to uppercase
    output_text = f"Processed: {input_text.upper()}"

    # Update the text in the output Label widget
    output_label.config(text=output_text)

# --- 2. Set Up the Main Window ---
# Create the main window object
root = tk.Tk()
root.title("Tkinter Basic GUI")
root.geometry("400x200")  # Set a default size for the window

# --- 3. Create Widgets ---

# A. Input Text Box (Entry Widget)
# We use a StringVar to easily manage the text content
input_var = tk.StringVar(root, value="Type something here...")
entry = ttk.Entry(root, textvariable=input_var, width=15)
entry.pack(pady=10) # 'pack' is a simple way to place the widget

# B. Action Button (Button Widget)
# We link the 'command' argument to the function defined above
action_button = ttk.Button(root, text="Click Me", command=process_input)
action_button.pack(pady=10)

# C. Output Display (Label Widget)
# This label will initially be empty or display instructions
output_label = ttk.Label(root, text="Output will appear here.", font=('Arial', 10, 'italic'))
output_label.pack(pady=10)

# --- 4. Start the Main Loop ---
# This line is essential. It tells Tkinter to start running the event loop,
# listening for mouse clicks, key presses, and window events.
root.mainloop()
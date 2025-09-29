import tkinter as tk
from tkinter import ttk

# --- 1. Define the Action Function ---
def submit_feedback():
    """
    Retrieves the input from all form fields and prints it to the console.
    """
    # 1. Retrieve data from the Entry widgets (Name and Email)
    name = name_entry.get()
    email = email_entry.get()

    # 2. Retrieve data from the Text widget (Feedback)
    # "1.0" means line 1, character 0 (the beginning)
    # tk.END means the end of the text, minus a newline character
    feedback = feedback_text.get("1.0", tk.END).strip()

    # 3. Print the collected data to the console
    print("--- NEW FEEDBACK SUBMISSION ---")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Feedback Content:\n{feedback}")
    print("---------------------------------")
    
    # Optionally, clear the form after submission
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    feedback_text.delete("1.0", tk.END)
    
    # Update a message in the GUI to confirm submission
    confirmation_label.config(text="Thank you! Your feedback has been submitted (see console).")


# --- 2. Set Up the Main Window ---
root = tk.Tk()
root.title("Customer Feedback Form")
root.geometry("500x450") # Set a slightly larger size for the form
root.columnconfigure(0, weight=1) # Make column 0 expandable (for centering)
root.columnconfigure(1, weight=3) # Make column 1 even more expandable for the inputs

# --- 3. Create Widgets and Layout using Grid ---

# A. Main Title/Prompt
title_label = ttk.Label(
    root, 
    text="Please provide feedback on your experience:", 
    font=('Arial', 14, 'bold')
)
# sticky='w' makes it align to the West (left)
title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10), padx=20, sticky='w')

# B. Name Field
name_label = ttk.Label(root, text="Your Name:")
name_label.grid(row=1, column=0, padx=(20, 5), pady=5, sticky='w') # Label on the left
name_entry = ttk.Entry(root, width=50)
name_entry.grid(row=1, column=1, padx=(5, 20), pady=5, sticky='ew') # Input field on the right

# C. Email Field
email_label = ttk.Label(root, text="Your Email:")
email_label.grid(row=2, column=0, padx=(20, 5), pady=5, sticky='w')
email_entry = ttk.Entry(root, width=50)
email_entry.grid(row=2, column=1, padx=(5, 20), pady=5, sticky='ew')

# D. Feedback Area
feedback_label = ttk.Label(root, text="Feedback:")
feedback_label.grid(row=3, column=0, padx=(20, 5), pady=5, sticky='nw') # Align label top-left
feedback_text = tk.Text(root, height=10, width=40, font=('Arial', 10))
feedback_text.grid(row=3, column=1, padx=(5, 20), pady=5, sticky='nsew') # Allow text area to expand

# E. Submission Confirmation Label (initially empty)
confirmation_label = ttk.Label(root, text="", foreground='green')
confirmation_label.grid(row=4, column=0, columnspan=2, pady=10)

# F. Submit Button
submit_button = ttk.Button(root, text="Submit Feedback", command=submit_feedback)
submit_button.grid(row=5, column=0, columnspan=2, pady=15)

# --- 4. Start the Main Loop ---
# This is required to keep the window open and responsive
root.mainloop()
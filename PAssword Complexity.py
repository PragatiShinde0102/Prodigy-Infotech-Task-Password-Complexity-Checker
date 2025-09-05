import tkinter as tk
import re

# Function to check password strength
def check_password_strength(event=None):
    password = entry.get()
    
    # Criteria checks
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None
    
    # Score system
    score = 5 - sum([length_error, digit_error, uppercase_error, lowercase_error, symbol_error])
    
    # Feedback messages
    feedback = []
    if length_error:
        feedback.append("❌ At least 8 characters required")
    if digit_error:
        feedback.append("❌ Add at least one number")
    if uppercase_error:
        feedback.append("❌ Add at least one uppercase letter")
    if lowercase_error:
        feedback.append("❌ Add at least one lowercase letter")
    if symbol_error:
        feedback.append("❌ Add at least one special character")
    
    # Strength evaluation
    if score == 5:
        result = "✅ Strong Password"
        color = "green"
    elif score >= 3:
        result = "⚠️ Medium Password"
        color = "orange"
    else:
        result = "❌ Weak Password"
        color = "red"
    
    # Update UI
    result_label.config(text=result, fg=color)
    feedback_text.delete("1.0", tk.END)
    if feedback:
        feedback_text.insert(tk.END, "\n".join(feedback))
    else:
        feedback_text.insert(tk.END, "👍 Your password looks great!")

# GUI setup
root = tk.Tk()
root.title("🔐 Password Complexity Checker")
root.geometry("500x400")
root.config(bg="#2E3B55")

title = tk.Label(root, text="Password Complexity Checker", font=("Arial", 16, "bold"), bg="#2E3B55", fg="white")
title.pack(pady=10)

instruction = tk.Label(root, text="Enter your password below:", font=("Arial", 12), bg="#2E3B55", fg="white")
instruction.pack(pady=5)

entry = tk.Entry(root, show="*", font=("Arial", 14), width=30, justify="center")
entry.pack(pady=10)

# Bind event for live checking
entry.bind("<KeyRelease>", check_password_strength)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#2E3B55")
result_label.pack(pady=10)

feedback_text = tk.Text(root, height=6, width=50, wrap="word", font=("Arial", 11))
feedback_text.pack(pady=10)

root.mainloop()

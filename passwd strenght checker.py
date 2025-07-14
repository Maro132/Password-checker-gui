import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    score = 0
    feedback = []
    # check for password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password must be at least 8 characters long.")

    #check for password uppercase character
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Password must contain at least one uppercase letter (A-Z).")

    #check for password lowercase character
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Password must contain at least one lowercase letter (a-z).")

    #check for password digit character
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Password must contain at least one digit (1,2,3).")

    #check for password special character
    special_characters = "!@#$%^&*-_=+"
    if any(char in special_characters for char in password):
        score += 1
    else:
        feedback.append(f"Password must contain at least one special character such as {special_characters}.")

    #check password score
    strength_level = ""
    if score == 5:
        strength_level = "Strong"
    elif score == 4:
        strength_level = "Medium"
    elif score == 3:
        strength_level = "Weak"
    elif score == 2:
        strength_level = "Very Weak"
    elif score == 1:
        strength_level = "Poor"
    else:
        strength_level = "Very Poor"

    return score, strength_level, feedback

# ---

def analyze_password():
    password = password_entry.get()

    if not password:
        messagebox.showwarning("Input Error", "Please enter a password to check.")
        return

    score, strength_level, feedback_list = check_password_strength(password)

    strength_label.config(text=f"Password Strength: {strength_level}")
    score_label.config(text=f"Score: {score}/5")

    feedback_text.config(state=tk.NORMAL)
    feedback_text.delete(1.0, tk.END)

    if feedback_list:
        feedback_text.insert(tk.END, "Feedback to improve your password:\n")
        for item in feedback_list:
            feedback_text.insert(tk.END, f"- {item}\n")
    else:
        feedback_text.insert(tk.END, "Excellent! Your password meets all criteria.")

    feedback_text.config(state=tk.DISABLED)

# ---

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x450")
root.resizable(False, False)

main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(expand=True, fill=tk.BOTH)

title_label = tk.Label(main_frame, text="Password Strength Checker",
                       font=("Arial", 20, "bold"),
                       fg="#333")
title_label.pack(pady=10)

password_label = tk.Label(main_frame, text="Enter your password:", font=("Arial", 12))
password_label.pack(pady=5)

# تم إزالة show="*" لجعل الأحرف تظهر بدلاً من النجوم
password_entry = tk.Entry(main_frame, width=40, font=("Arial", 12))
password_entry.pack(pady=5)

analyze_button = tk.Button(main_frame, text="Analyze Password", command=analyze_password,
                           font=("Arial", 14, "bold"), bg="#4CAF50", fg="white",
                           activebackground="#45a049", padx=10, pady=5, relief=tk.RAISED, bd=3)
analyze_button.pack(pady=15)

strength_label = tk.Label(main_frame, text="Password Strength: ---",
                           font=("Arial", 16, "bold"), fg="#0056b3")
strength_label.pack(pady=5)

score_label = tk.Label(main_frame, text="Score: --/5", font=("Arial", 14), fg="#555")
score_label.pack(pady=5)

feedback_title_label = tk.Label(main_frame, text="Feedback:", font=("Arial", 12, "underline"))
feedback_title_label.pack(pady=10)

feedback_text = tk.Text(main_frame, height=8, width=50, wrap=tk.WORD, font=("Arial", 10),
                        bg="#f0f0f0", fg="#333", relief=tk.SUNKEN, bd=2)
feedback_text.pack(pady=5)
feedback_text.config(state=tk.DISABLED)

root.mainloop()
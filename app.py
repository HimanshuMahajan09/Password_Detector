import tkinter as tk
from tkinter import messagebox
from src.breach_detector import build_filter

# Build Bloom Filter from data file
bloom = build_filter("data/breached_passwords.txt")

def check_password():
    password = entry.get().strip()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password to check.")
        return
    if bloom.check(password):
        result_label.config(text="⚠️ This password MAY have been breached!", fg="red")
    else:
        result_label.config(text="✅ This password is safe!", fg="green")

# GUI setup
window = tk.Tk()
window.title("🔐 Password Breach Detector (Bloom Filter)")
window.geometry("450x300")
window.config(bg="#f5f5f5")

title = tk.Label(window, text="Password Breach Detector", font=("Arial", 16, "bold"), bg="#f5f5f5")
title.pack(pady=20)

entry_label = tk.Label(window, text="Enter a password to check:", bg="#f5f5f5", font=("Arial", 12))
entry_label.pack()

entry = tk.Entry(window, show="*", width=30, font=("Arial", 12))
entry.pack(pady=10)

check_btn = tk.Button(window, text="Check Password", command=check_password, bg="#0078d7", fg="white", font=("Arial", 12, "bold"))
check_btn.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 13, "bold"), bg="#f5f5f5")
result_label.pack(pady=15)

window.mainloop()

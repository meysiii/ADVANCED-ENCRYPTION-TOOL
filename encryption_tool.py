import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import os

# Encryption key (keep it safe!)
KEY = b'1YqzKIsBg6ab3CABeel6go1b0NRpmvDCq4klorlWO3M='
fernet = Fernet(KEY)

# Encrypt a file
def encrypt_file():
    filepath = filedialog.askopenfilename()
    if not filepath:
        return
    with open(filepath, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(filepath + '.enc', 'wb') as enc_file:
        enc_file.write(encrypted)
    messagebox.showinfo("Success", f"File encrypted: {filepath}.enc")

# Decrypt a file
def decrypt_file():
    filepath = filedialog.askopenfilename(filetypes=[("Encrypted files", "*.enc")])
    if not filepath:
        return
    with open(filepath, 'rb') as enc_file:
        encrypted = enc_file.read()
    try:
        decrypted = fernet.decrypt(encrypted)
        output_path = filedialog.asksaveasfilename(defaultextension=".txt")
        with open(output_path, 'wb') as dec_file:
            dec_file.write(decrypted)
        messagebox.showinfo("Success", f"File decrypted: {output_path}")
    except:
        messagebox.showerror("Error", "Decryption failed. Invalid key or file.")

# GUI setup
root = tk.Tk()
root.title("Advanced Encryption Tool - CODTECH")
root.geometry("400x200")
root.config(bg="#f4f4f4")

title = tk.Label(root, text="AES-256 Encryption Tool", font=("Helvetica", 16, "bold"), bg="#f4f4f4")
title.pack(pady=10)

encrypt_btn = tk.Button(root, text="Encrypt File", command=encrypt_file, width=20, bg="#4CAF50", fg="white")
encrypt_btn.pack(pady=10)

decrypt_btn = tk.Button(root, text="Decrypt File", command=decrypt_file, width=20, bg="#2196F3", fg="white")
decrypt_btn.pack(pady=10)

root.mainloop()
import hashlib
import os
import tkinter as tk
from tkinter import filedialog, ttk


def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while (chunk := f.read(4096)):
            sha256.update(chunk)
    return sha256.hexdigest()

def verify_hash():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    expected_hash = hash_entry.get()
    calculated_hash = calculate_hash(file_path)
    if calculated_hash == expected_hash:
        result_label.config(text=f"Hash verification successful! Calculated hash: {calculated_hash}")
    else:
        result_label.config(text=f"Hash verification failed! Expected hash: {expected_hash}, Calculated hash: {calculated_hash}")

app = tk.Tk()
app.title("Hash Verifier")

frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

hash_label = ttk.Label(frame, text="Enter the expected SHA-256 hash:")
hash_label.grid(row=0, column=0, sticky=tk.W)

hash_entry = ttk.Entry(frame, width=40)
hash_entry.grid(row=0, column=1)

verify_button = ttk.Button(frame, text="Verify Hash", command=verify_hash)
verify_button.grid(row=1, column=0, columnspan=2)

result_label = ttk.Label(frame, text="")
result_label.grid(row=2, column=0, columnspan=2)

app.mainloop()
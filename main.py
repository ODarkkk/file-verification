import hashlib
import os
import tkinter as tk
from tkinter import filedialog, ttk

def calculate_hash(file_path, algorithm='sha256'):
    """Calculate the hash of a file using the specified algorithm.

    Args:
        file_path (str): The path to the file to hash.
        algorithm (str, optional): The hash algorithm to use. Defaults to 'sha256'.

    Returns:
        str: The hexadecimal representation of the hash.
    """


    match algorithm:
        case "sha256":
            hash_object = hashlib.sha256()
        case "sha224":
            hash_object = hashlib.sha224()
        case "sha384":
            hash_object = hashlib.sha384()
        case "sha512":
            hash_object = hashlib.sha512()
        case "sha1":
            hash_object = hashlib.sha1()
        case "md5":
            hash_object = hashlib.md5()
        case _:
            raise ValueError(f"Unknown hash algorithm: {algorithm}")


    with open(file_path, 'rb') as f:
        while (chunk := f.read(4096)):
            hash_object.update(chunk)
    return hash_object.hexdigest()

def verify_hash():
    """Verify the hash of a file against a given expected hash.

    Shows a file dialog to allow the user to select the file to hash and prompts the user for the expected hash.
    Displays a success or failure message based on whether the calculated hash matches the expected hash.
    """
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    algorithm = hash_algo_var.get()
    expected_hash = hash_entry.get()
    calculated_hash = calculate_hash(file_path, algorithm)

    if calculated_hash == expected_hash:
        result_label.config(text=f"Hash verification successful! Calculated hash: {calculated_hash}")
    else:
        result_label.config(text=f"Hash verification failed! Expected hash: {expected_hash}, Calculated hash: {calculated_hash}")

app = tk.Tk()
app.title("Hash Verifier")

frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

hash_algo_var = tk.StringVar(frame)
hash_algo_var.set('sha256')

hash_label = ttk.Label(frame, text="Select the hash algorithm:")
hash_label.grid(row=0, column=0, sticky=tk.W)

hash_algo_menu = ttk.Combobox(frame, textvariable=hash_algo_var, state='readonly')
hash_algo_menu['values'] = ('sha256', 'sha224', 'sha512', 'sha_384', 'sha1', 'md5')
hash_algo_menu.grid(row=0, column=1, sticky=(tk.W, tk.E))

hash_entry = ttk.Entry(frame, width=40)
hash_entry.grid(row=1, column=0, columnspan=2)

verify_button = ttk.Button(frame, text="Verify Hash", command=verify_hash)
verify_button.grid(row=2, column=0, columnspan=2)

result_label = ttk.Label(frame, text="")
result_label.grid(row=3, column=0, columnspan=2)

app.mainloop()
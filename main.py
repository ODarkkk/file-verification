import hashlib
import os
import tkinter as tk
from tkinter import filedialog, ttk
from repair_file import Repair
import shedule
import sys

# List of libraries you need to import
required_libraries = ['crc32c', 'tkinter', 'pandas', 'PIL', 'openpyxl']

# Try to import each required library
for lib in required_libraries:
    try:
        globals()[lib] = __import__(lib)
    except ImportError:
        # If import fails, append the directory of libraries to sys.path and try again
        sys.path.append('./lib')
        globals()[lib] = __import__(lib)
def calculate_hash(file_path, algorithm='sha256'):
    """Calculate the hash of a file using the specified algorithm."""
    hash_object = hashlib.new(algorithm)
    with open(file_path, 'rb') as f:
        while (chunk := f.read(4096)):
            hash_object.update(chunk)
    return hash_object.hexdigest()

def verify_hash():
    """Verify the hash of a file against a given expected hash."""
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    algorithm = hash_algo_var.get()
    expected_hash = hash_entry.get()
    calculated_hash = calculate_hash(file_path, algorithm)

    if calculated_hash == expected_hash:
        result_label.config(text=f"Hash verification successful! Calculated hash: {calculated_hash}")
        repair_text.delete(1.0, tk.END)
    else:
        result_label.config(text=f"Hash verification failed! Expected hash: {expected_hash}, Calculated hash: {calculated_hash}")
        repair_button = ttk.Button(frame, text="Repair", command=lambda: repair_callback(file_path))
        repair_button.grid(row=4, column=0, sticky=tk.W)

def repair_callback(file_path):
    repair_tool = Repair(os.path.dirname(file_path), os.path.dirname(file_path))
    repaired = repair_tool.repair_file(file_path, os.path.dirname(file_path))
    if repaired:
        repair_text.insert(tk.END, f"Repaired: {os.path.basename(file_path)}\n")
    else:
        repair_text.insert(tk.END, f"Failed to repair: {os.path.basename(file_path)}\n")

app = tk.Tk()
app.title("Hash Verifier")

frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

hash_algo_var = tk.StringVar(frame)


def open_config_tab():
    # Create a new window for the configuration tab
    config_window = tk.Toplevel(app)
    config_window.title("Settings")

    # Add the configuration elements in this new window
    #config_label = ttk.Label(config_window, text="Settings")
    #config_label.pack()

    shedule_button = ttk.Button(frame, text="Set a timer", command = )

    #verify_button = ttk.Button(frame, text="Verify Hash", command=verify_hash)
    #verify_button.grid(row=3, column=1, columnspan=2)



    # You can add more widgets and functionalities as needed



hash_algo_var.set('sha256')

hash_label = ttk.Label(frame, text="Select the hash algorithm:")
hash_label.grid(row=0, column=0, sticky=tk.W)

hash_algo_menu = ttk.Combobox(frame, textvariable=hash_algo_var, state='readonly')
hash_algo_menu['values'] = ('sha256', 'sha224', 'sha512', 'sha384', 'sha1', 'md5')
hash_algo_menu.grid(row=0, column=1, sticky=(tk.W, tk.E))

hash2_label = ttk.Label(frame, text="Put the hash of program (optional):")
hash2_label.grid(row=1, column=0, sticky=tk.W)

hash_entry = ttk.Entry(frame, width=40)
hash_entry.grid(row=1, column=1, columnspan=1)

verify_button = ttk.Button(frame, text="Verify Hash", command=verify_hash)
verify_button.grid(row=3, column=1, columnspan=2)

# Add a button to open the configuration tab
config_button = ttk.Button(frame, text="Settings", command=open_config_tab)
config_button.grid(row=5, column=0, sticky=(tk.W))


result_label = ttk.Label(frame, text="")
result_label.grid(row=3, column=0, columnspan=2)

repair_text_label = ttk.Label(frame, text="Repaired Files:")
repair_text_label.grid(row=6, column=0, columnspan=2)

repair_text = tk.Text(frame, height=10, width=40)
repair_text.grid(row=7, column=0, columnspan=2)

app.mainloop()

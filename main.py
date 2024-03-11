#import argparse, hashlib, sys
#from colorama import init, Fore
#
#def calculate_hash(file_path):
#   sha256_hash = hashlib.sha256()
#   with open(file_path, "rb") as file:
#      while True:
#         data = file.read(65536)
#         if not data:
#            break
#         sha256_hash.update(data)
#   return sha256_hash.hexdigest()
##oi = hashlib.
#def verify_hash(downloaded_file, expected_hash):
#   calculated_hash = calculate_hash(downloaded_file)
#   return calculated_hash == expected_hash
#
#init()
#
## Create an ArgumentParser object.
#parser = argparse.ArgumentParser(description="Verify the hash of a downloaded file.")
## Add the arguments you want to parse.
#parser.add_argument("downloaded_file", help="The path to the downloaded file.")
#parser.add_argument("expected_hash", help="The expected hash of the downloaded file.")
## Parse the command line arguments.
#args = parser.parse_args()
#
#if verify_hash(args.downloaded_file, args.expected_hash):
#   print(f"{Fore.GREEN}[+] Hash verification successful. The software is authentic.")
#else:
#   print(f"{Fore.RED}[-] Hash verification failed. The software may have been tampered with or is not authentic.")



import argparse
import hashlib
import sys
import os
from tkinter import *
from tkinter import ttk
#
import colorama
from colorama import Fore
colorama.init()

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
#
## Define a function to calculate the SHA-256 hash of a file.
#def calculate_hash(file_path):
#   # Create a SHA-256 hash object.
#   sha256_hash = hashlib.sha256()
#   # Open the file in binary mode for reading (rb).
#   with open(file_path, "rb") as file:
#       # Read the file in 64KB chunks to efficiently handle large files.
#       while True:
#           data = file.read(65536)  # Read the file in 64KB chunks.
#           if not data:
#               break
#           # Update the hash object with the data read from the file.
#           sha256_hash.update(data)
#   # Return the hexadecimal representation of the calculated hash.
#   return sha256_hash.hexdigest()
#
## Define a function to verify the calculated hash against an expected hash.
#def verify_hash(downloaded_file, expected_hash):
#   # Calculate the hash of the downloaded file.
#   calculated_hash = calculate_hash(downloaded_file)
#   # Compare the calculated hash with the expected hash and return the result.
#   print(hash(calculated_hash))
#   return calculated_hash == expected_hash
#
## Create a parser for handling command-line arguments.
#parser = argparse.ArgumentParser(description="Verify the hash of a downloaded software file.")
## Define two command-line arguments:
## -f or --file: Path to the downloaded software file (required).
## --hash: Expected hash value (required).
#parser.add_argument("-f", "--file", dest="downloaded_file", required=True, help="Path to the downloaded software file")
#parser.add_argument("--hash", dest="expected_hash", required=True, help="Expected hash value")
## Parse the command-line arguments provided when running the script.
#args = parser.parse_args()
## Check if the required command-line arguments were provided.
#if not args.downloaded_file or not args.expected_hash:
#   # Print an error message in red using colorama.
#   print(f"{Fore.RED}[-] Please Specify the file to validate and its Hash.")
#   # Exit the script.
#   sys.exit()
#
## Check if the hash of the file is accurate by calling the verify_hash function.
#if verify_hash(args.downloaded_file, args.expected_hash):
#   # If the hash is accurate, print a success message in green.
#   print(f"{Fore.GREEN}[+] Hash verification successful. The software is authentic.")
#else:
#   # If the hash does not match, print an error message in red.
#   print(f"{Fore.RED}[-] Hash verification failed. The software may have been tampered with or is not authentic.")

def hash_calculate(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Ler o arquivo em pequenos blocos para lidar com arquivos grandes
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256.update(byte_block)
    return sha256.hexdigest()

def corruption_check(file_path, last_hash=None):
    if not os.path.exists(file_path):
        return False  # Arquivo não existe
    if last_hash is not None and last_hash != new_hash:
        return True  # O hash mudou, indicando possível corrupção

    return False  # O arquivo parece estar íntegro

parser = argparse.ArgumentParser(description="Verify the hash of a downloaded software file.")
parser.add_argument("-f", "--file", dest="file_path", required=True, help="Path to the downloaded software file")
parser.add_argument("--hash", dest="expected_hash", required=False, help="Expected hash value")
    ## Parse the command-line arguments provided when running the script.
args = parser.parse_args()

new_hash = hash_calculate(args.file_path)



# Exemplo de uso


if corruption_check(args.file_path, args.expected_hash):
    print("File does corrupted.")
else:
    print("File doesn't corrupted.")
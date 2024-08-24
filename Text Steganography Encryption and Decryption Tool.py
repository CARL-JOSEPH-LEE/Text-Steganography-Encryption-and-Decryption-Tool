import tkinter as tk
from tkinter import messagebox
import random

# Function to generate random symbols (using only common visible symbols)
def generate_random_symbols(length):
    # Use only common visible symbols
    symbols = '!@#$%^&*()_+{}[]<>?/\\|'
    return ''.join(random.choice(symbols) for _ in range(length))

# Encryption function with more symbols for obfuscation, using standard visible symbols
def encrypt_text(plaintext, key):
    encrypted_text = []
    try:
        key = int(key)  # Ensure the key is an integer
    except ValueError:
        messagebox.showerror("Input Error", "Key must be an integer!")
        return ""

    for char in plaintext:
        # Insert the actual character
        encrypted_text.append(char)

        # Insert a large number of random symbols for greater obfuscation
        random_symbols = generate_random_symbols(random.randint(20, 50))
        encrypted_text.append(random_symbols)

    # Join everything and then apply the ASCII shift to the entire string
    encrypted_string = ''.join(encrypted_text)
    shifted_encrypted_string = ''.join([chr((ord(char) + key) % 128) for char in encrypted_string])

    return shifted_encrypted_string

# Decryption function with correct logic using standard visible symbols
def decrypt_text(ciphertext):
    all_decryptions = []

    # Try all possible key shifts (0 to 127)
    for key in range(128):
        # Perform the reverse shift (subtract the key)
        shifted_text = ''.join([chr((ord(char) - key) % 128) for char in ciphertext])

        # Filter out non-alphanumeric characters (i.e., keep only letters and digits)
        filtered_text = ''.join([char for char in shifted_text if char.isalnum()])

        # Add the result to the list with the corresponding key
        all_decryptions.append(f"Key {key}: {filtered_text}")

    return '\n'.join(all_decryptions)

# Function to handle encrypt button click
def on_encrypt_button_click():
    plaintext = entry_plaintext.get()
    key = entry_key.get()

    if not plaintext:
        messagebox.showerror("Input Error", "Plaintext cannot be empty!")
        return

    encrypted_message = encrypt_text(plaintext, key)
    text_encrypted_message.config(state=tk.NORMAL)
    text_encrypted_message.delete(1.0, tk.END)
    text_encrypted_message.insert(tk.END, encrypted_message)
    text_encrypted_message.config(state=tk.DISABLED)

# Function to handle decrypt button click
def on_decrypt_button_click():
    ciphertext = entry_ciphertext.get("1.0", tk.END).strip()

    if not ciphertext:
        messagebox.showerror("Input Error", "Ciphertext cannot be empty!")
        return

    decrypted_results = decrypt_text(ciphertext)
    text_decrypted_message.config(state=tk.NORMAL)
    text_decrypted_message.delete(1.0, tk.END)
    text_decrypted_message.insert(tk.END, decrypted_results)
    text_decrypted_message.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Text Steganography Encryption and Decryption Tool")
root.geometry("600x900")

# Plaintext input
label_plaintext = tk.Label(root, text="Enter Plaintext:")
label_plaintext.pack(pady=10)
entry_plaintext = tk.Entry(root, width=70)
entry_plaintext.pack()

# Key input for encryption
label_key = tk.Label(root, text="Enter Key (Integer) for Encryption:")
label_key.pack(pady=10)
entry_key = tk.Entry(root, width=70)
entry_key.pack()

# Key information
label_key_info = tk.Label(root, text="The key is used to shift the ASCII codes of the plaintext characters (mod 128).")
label_key_info.pack(pady=5)

# Encrypt button
button_encrypt = tk.Button(root, text="Encrypt", command=on_encrypt_button_click)
button_encrypt.pack(pady=10)

# Display encrypted message
label_encrypted_message = tk.Label(root, text="Encrypted Message:")
label_encrypted_message.pack(pady=10)
text_encrypted_message = tk.Text(root, width=80, height=10, state=tk.DISABLED)
text_encrypted_message.pack()

# Ciphertext input for decryption
label_ciphertext = tk.Label(root, text="Enter Ciphertext for Decryption:")
label_ciphertext.pack(pady=10)
entry_ciphertext = tk.Text(root, width=80, height=5)
entry_ciphertext.pack()

# Decrypt button
button_decrypt = tk.Button(root, text="Decrypt", command=on_decrypt_button_click)
button_decrypt.pack(pady=10)

# Display decrypted results
label_decrypted_message = tk.Label(root, text="Decrypted Messages (for each possible key):")
label_decrypted_message.pack(pady=10)
text_decrypted_message = tk.Text(root, width=80, height=15, state=tk.DISABLED)
text_decrypted_message.pack()

# Run the main loop
root.mainloop()

import tkinter as tk
from tkinter import messagebox
import random


# Function to generate random symbols (using only non-alphanumeric visible ASCII symbols)
def generate_random_symbols(length):
    # Use only visible ASCII characters excluding letters and digits (33-126, excluding A-Z, a-z, 0-9)
    symbols = ''.join(chr(i) for i in range(33, 127) if not chr(i).isalnum())
    return ''.join(random.choice(symbols) for _ in range(length))


# Encryption function using ASCII shift and converting to concatenated numbers (ord())
def encrypt_text(plaintext, key):
    encrypted_text = []
    try:
        key = int(key)  # Ensure the key is an integer
    except ValueError:
        messagebox.showerror("Input Error", "Key must be an integer!")
        return ""

    # Step 1: Insert random symbols and apply ASCII shift
    for char in plaintext:
        encrypted_text.append(char)  # Insert the actual character

        # Insert a large number of random symbols for greater obfuscation
        random_symbols = generate_random_symbols(random.randint(20, 50))
        encrypted_text.append(random_symbols)

    # Join everything into one string
    encrypted_string = ''.join(encrypted_text)

    # Step 2: Apply ASCII shift and convert to ASCII codes using ord()
    numeric_encrypted_string = ''
    for char in encrypted_string:
        shifted_char = chr(((ord(char) - 32 + key) % 95) + 32) if 32 <= ord(char) <= 126 else char
        ascii_value = ord(shifted_char)
        numeric_encrypted_string += str(ascii_value)  # Concatenate without spaces

    return numeric_encrypted_string


# Decryption function to reverse the encryption process
def decrypt_text(ciphertext):
    all_decryptions = []

    # Step 1: Try all possible key shifts (0 to 94)
    for key in range(95):
        decrypted_chars = []
        i = 0

        # Step 2: Convert numeric values back to characters
        while i < len(ciphertext):
            if ciphertext[i] != '1':  # Two-digit ASCII (32-99)
                num_str = ciphertext[i:i+2]
                i += 2
            else:  # Three-digit ASCII (100-126)
                num_str = ciphertext[i:i+3]
                i += 3

            try:
                ascii_value = int(num_str)
                shifted_value = ((ascii_value - 32 - key) % 95) + 32  # Reverse the ASCII shift
                decrypted_chars.append(chr(shifted_value))
            except ValueError:
                # Handle potential errors gracefully
                continue

        # Join the decrypted characters into a string
        decrypted_string = ''.join(decrypted_chars)

        # Filter out non-alphanumeric characters (i.e., keep only letters and digits)
        filtered_text = ''.join([char for char in decrypted_string if char.isalnum()])

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
label_key_info = tk.Label(root, text="The key is used to shift the ASCII codes of the plaintext characters (mod 95).")
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

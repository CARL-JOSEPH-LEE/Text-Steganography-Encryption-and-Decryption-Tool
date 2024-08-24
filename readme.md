
# Text Steganography Encryption and Decryption Tool

## Introduction

Welcome to the **Text Steganography Encryption and Decryption Tool**, an exciting and innovative application designed to blend the worlds of steganography and cryptography. This tool provides an easy-to-use graphical interface for encrypting and decrypting text using a combination of random symbol insertion and ASCII-based encryption. It offers a fascinating hands-on experience with the inner workings of cryptography, making it perfect for both beginners and enthusiasts.

## Features

-   **Steganographic Obfuscation**: Encrypts each character by hiding it behind random symbols, making it harder to detect patterns in the ciphertext.
-   **Key-Based ASCII Encryption**: Shift your characters using a user-defined key to scramble the message further.
-   **Brute-Force Decryption**: The decryption tool automatically tries every possible key (0-127) to help recover the original message.
-   **User-Friendly GUI**: Built using Tkinter, the tool provides a clean and intuitive interface for seamless encryption and decryption operations.

## How It Works

### Encryption

1.  **Insert Random Symbols**: For each character in your message, random symbols are inserted to obfuscate the content.
2.  **Apply ASCII Shift**: Using a numeric key, the program shifts the ASCII value of each character and symbol, creating an encrypted text that’s hard to reverse-engineer.

### Decryption

1.  **Reverse ASCII Shift**: The tool tries every possible key by reversing the ASCII shift for all characters.
2.  **Filter Symbols**: Non-alphanumeric characters (symbols) are filtered out, revealing the potential decrypted messages.

The brute-force decryption process will list all possible key shifts, allowing you to identify the correct decrypted message.

## Setup and Installation

To run the Text Steganography Encryption and Decryption Tool, follow these steps:

1.  **Clone the Repository**:
    
    `git clone https://github.com/CARL-JOSEPH-LEE/Text-Steganography-Encryption-and-Decryption-Tool.git` 
    
2.  **Navigate to the Project Directory**:

    `cd Text-Steganography-Encryption-and-Decryption-Tool` 
    
3.  **Run the Program**: Simply run the Python script using:
    
    `python main.py` 
    

This project relies on Python's standard library, specifically `tkinter` for the GUI, so no external dependencies are required.

## Usage

### Encryption

1.  Enter your plaintext message in the input field.
2.  Provide an encryption key (integer).
3.  Click **"Encrypt"** to see the encrypted message, which contains your original text obfuscated by random symbols and ASCII shifts.

### Decryption

1.  Paste the encrypted message in the decryption input field.
2.  Click **"Decrypt"** to display possible decrypted results. The program will list every potential decryption using keys from 0 to 127.
3.  Review the output to find the correct original message.

## Screenshots

Here's how the application looks: ![Main](images/main.png)

## Why Use This Tool?

In an era of heightened digital privacy concerns, this tool offers a simple yet effective method to secure your messages. Its steganographic and cryptographic combination provides a powerful means to hide sensitive information from prying eyes. Whether for educational purposes or real-world application, this tool equips you with a hands-on way to explore and understand encryption.

## Contribution

Contributions are welcome! Feel free to fork the repository, submit issues, or create pull requests. Let’s make cryptography more accessible together.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any questions, suggestions, or feedback:

-   **GitHub**: [CARL-JOSEPH-LEE](https://github.com/CARL-JOSEPH-LEE)
-   **Email**: carljosephlee3@gmail.com
import tkinter as tk

def caesar_cipher(message, key, mode):
    # Initialize an empty result string
    result = ""

    # If mode is 'decrypt', invert the key
    if mode == 'decrypt':
        key = 26 - key

    # Iterate over each character in the message
    for char in message:
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - 65 + key) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            result += char

    return result

def encrypt():
    message = plaintext_entry.get()
    key = int(shift_entry.get())
    ciphertext = caesar_cipher(message, key, 'encrypt')
    ciphertext_entry.delete(0, tk.END)
    ciphertext_entry.insert(0, ciphertext)

def decrypt():
    ciphertext = ciphertext_entry.get()
    key = int(shift_entry.get())
    plaintext = caesar_cipher(ciphertext, key, 'decrypt')
    output_entry.delete(0, tk.END)
    output_entry.insert(0, plaintext)

# Create the main window
window = tk.Tk()
window.title("Caesar Cipher Encryption and Decryption")

# Create the input widgets
plaintext_label = tk.Label(window, text="Enter plaintext:")
plaintext_label.pack()
plaintext_entry = tk.Entry(window)
plaintext_entry.pack()

shift_label = tk.Label(window, text="Enter shift pattern:")
shift_label.pack()
shift_entry = tk.Entry(window)
shift_entry.pack()

encrypt_button = tk.Button(window, text="Encrypt", command=encrypt)
encrypt_button.pack()

ciphertext_label = tk.Label(window, text="Enter ciphertext:")
ciphertext_label.pack()
ciphertext_entry = tk.Entry(window)
ciphertext_entry.pack()

decrypt_button = tk.Button(window, text="Decrypt", command=decrypt)
decrypt_button.pack()

# Create the output widgets
output_label = tk.Label(window, text="Decrypted result:")
output_label.pack()
output_entry = tk.Entry(window)
output_entry.pack()

# Start the main event loop
window.mainloop()

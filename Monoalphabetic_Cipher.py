import random
import tkinter as tk

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

# Encrypts the plain text message
def encrypt(original, key=None):
    if key is None:
        l = list(ALPHABET)
        random.shuffle(l)
        key = "".join(l)
    
    new = []
    for letter in original:
        if letter.lower() in ALPHABET:
            new.append(key[ALPHABET.index(letter.lower())])
        else:
            new.append(letter)
    
    return ["".join(new), key]

# Decrypts the encrypted message
def decrypt(cipher, key):
    new = []
    for letter in cipher:
        if letter.lower() in key:
            new.append(ALPHABET[key.index(letter.lower())])
        else:
            new.append(letter)
    
    return "".join(new)

# Define GUI
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Substitution Cipher")

        self.message_label = tk.Label(self, text="Enter the message to encrypt:")
        self.message_label.pack()

        self.message_entry = tk.Entry(self)
        self.message_entry.pack()

        self.key_label = tk.Label(self, text="Enter the key (optional):")
        self.key_label.pack()

        self.key_entry = tk.Entry(self)
        self.key_entry.pack()

        self.encrypt_button = tk.Button(self, text="Encrypt", command=self.encrypt_message)
        self.encrypt_button.pack()

        self.encrypted_label = tk.Label(self, text="")
        self.encrypted_label.pack()

        self.key_result_label = tk.Label(self, text="")
        self.key_result_label.pack()

        self.decrypt_button = tk.Button(self, text="Decrypt", command=self.decrypt_message, state=tk.DISABLED)
        self.decrypt_button.pack()

        self.decrypted_label = tk.Label(self, text="")
        self.decrypted_label.pack()

    def encrypt_message(self):
        message = self.message_entry.get()
        key = self.key_entry.get()

        if key:
            e = encrypt(message, key)
        else:
            e = encrypt(message)

        self.encrypted_label.config(text="Encrypted message: " + e[0])
        self.key_result_label.config(text="Key: " + e[1])

        self.decrypt_button.config(state=tk.NORMAL)

    def decrypt_message(self):
        encrypted_message = self.encrypted_label.cget("text").split(": ")[1]
        key = self.key_result_label.cget("text").split(": ")[1]

        d = decrypt(encrypted_message, key)
        self.decrypted_label.config(text="Decrypted message: " + d)

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()

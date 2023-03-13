import tkinter as tk

class Solution:
    def __init__(self):
        self.N = ord('z') + ord('a')
    
    def encrypt(self, text):
        return ''.join([chr(self.N - ord(s)) for s in text])
    
    def decrypt(self, text):
        return self.encrypt(text) # decryption is the same as encryption with this algorithm

class App:
    def __init__(self, master, mode):
        self.solution = Solution()
        
        # create input label and entry
        self.input_label = tk.Label(master, text="Input Text:")
        self.input_entry = tk.Entry(master)
        
        # create output label and entry
        self.output_label = tk.Label(master, text="Output Text:")
        self.output_entry = tk.Entry(master, state='readonly')
        
        # create encrypt/decrypt button
        if mode == 'encrypt':
            self.mode_button = tk.Button(master, text="Encrypt", command=self.encrypt)
        elif mode == 'decrypt':
            self.mode_button = tk.Button(master, text="Decrypt", command=self.decrypt)
        
        # layout widgets using grid layout
        self.input_label.grid(row=0, column=0, padx=5, pady=5)
        self.input_entry.grid(row=0, column=1, padx=5, pady=5)
        self.output_label.grid(row=1, column=0, padx=5, pady=5)
        self.output_entry.grid(row=1, column=1, padx=5, pady=5)
        self.mode_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    
    def encrypt(self):
        input_text = self.input_entry.get()
        output_text = self.solution.encrypt(input_text)
        self.output_entry.config(state='normal')
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, output_text)
        self.output_entry.config(state='readonly')
    
    def decrypt(self):
        input_text = self.input_entry.get()
        output_text = self.solution.decrypt(input_text)
        self.output_entry.config(state='normal')
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, output_text)
        self.output_entry.config(state='readonly')

# create the main window and start the event loop
root = tk.Tk()
root.title("Text Encryption/Decryption")

# create separate frames for encryption and decryption
encryption_frame = tk.LabelFrame(root, text="Encryption")
encryption_frame.pack(fill="both", expand="yes", padx=10, pady=10)

decryption_frame = tk.LabelFrame(root, text="Decryption")
decryption_frame.pack(fill="both", expand="yes", padx=10, pady=10)

# create instances of App for encryption and decryption with respective mode
encrypt_app = App(encryption_frame, 'encrypt')
decrypt_app = App(decryption_frame, 'decrypt')

root.mainloop()

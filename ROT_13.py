import tkinter as tk
import codecs

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.input_label1 = tk.Label(self, text="Masukkan teks yang ingin di-encode dengan ROT13:")
        self.input_label1.pack()
        self.input_text1 = tk.Entry(self)
        self.input_text1.pack()

        self.encode_button = tk.Button(self, text="Encode", command=self.encode_text)
        self.encode_button.pack()

        self.output_label1 = tk.Label(self, text="")
        self.output_label1.pack()

        self.input_label2 = tk.Label(self, text="Masukkan teks yang ingin di-decode dengan ROT13:")
        self.input_label2.pack()
        self.input_text2 = tk.Entry(self)
        self.input_text2.pack()

        self.decode_button = tk.Button(self, text="Decode", command=self.decode_text)
        self.decode_button.pack()

        self.output_label2 = tk.Label(self, text="")
        self.output_label2.pack()

        self.quit_button = tk.Button(self, text="Quit", fg="red",
                                      command=self.master.destroy)
        self.quit_button.pack()

    def encode_text(self):
        text = self.input_text1.get()
        rot13 = codecs.encode(text, 'rot_13')
        self.output_label1.config(text="Teks yang telah di-encode dengan ROT13: " + rot13)

    def decode_text(self):
        text = self.input_text2.get()
        decoded_text = codecs.decode(text, 'rot_13')
        self.output_label2.config(text="Teks yang telah di-decode dengan ROT13: " + decoded_text)

root = tk.Tk()
app = Application(master=root)
app.mainloop()

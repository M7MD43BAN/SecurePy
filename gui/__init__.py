import tkinter

import customtkinter

from ceaser_cipher_gui import ceaser_cipher_frame
from monoalphabetic_cipher_gui import monoalphabetic_cipher_frame
from playfair_cipher_gui import playfair_cipher_frame

if __name__ == "__main__":
    app = customtkinter.CTk()

    app.title("SecurePy")
    app.geometry('450x450')
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")

    # GUI setup
    # Create a label
    label = customtkinter.CTkLabel(app, text="SecurePy Techniques", height=10, width=120,
                                   font=('Helvetica', 18, 'bold'))
    label.pack(padx=10, pady=20)

    # Create tabview
    tabview = customtkinter.CTkTabview(app)
    tabview.pack(padx=36, pady=36)

    # Create a window for each encryption technique
    # Ceaser-Cipher
    tabview.add("Ceaser-Cipher")
    # Monoalphabetic-Cipher
    tabview.add("Monoalphabetic-Cipher")
    # Playfair-Cipher
    tabview.add("Playfair-Cipher")
    # Default tab
    tabview.set("Ceaser-Cipher")

    # Create a frame for Ceaser-Cipher technique
    text_var = tkinter.StringVar()
    ceaser_cipher_frame(tabview, text_var)

    # Create a frame for Monoalphabetic-Cipher technique
    text_var_mono = tkinter.StringVar()
    key_generate_mono = tkinter.StringVar()
    cipher_var_mono = tkinter.StringVar()
    monoalphabetic_cipher_frame(tabview, text_var_mono, key_generate_mono, cipher_var_mono)

    # Create a frame for Playfair-Cipher technique
    text_entry_playfair = tkinter.StringVar()
    key_text_entry = tkinter.StringVar()
    text_var_playfair = tkinter.StringVar()
    playfair_cipher_frame(tabview, text_entry_playfair, key_text_entry, text_var_playfair)

    app.mainloop()

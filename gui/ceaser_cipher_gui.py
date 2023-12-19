import tkinter

import customtkinter

from caesar_cipher.decryption import caesar_cipher_decryption
from caesar_cipher.encryption import caesar_cipher_encryption


def ceaser_cipher_frame(tabview, text_var):
    # Create a frame
    frame = customtkinter.CTkFrame(master=tabview.tab("Ceaser-Cipher"), width=400, height=200, corner_radius=0,
                                   bg_color='white')
    frame.pack(padx=20, pady=200)

    # Create an entry input for text
    text = customtkinter.CTkEntry(master=tabview.tab("Ceaser-Cipher"), placeholder_text='Text', width=150,
                                  height=30, border_width=2, corner_radius=10)
    text.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

    # create an entry input for shift value
    shift_text_entry = customtkinter.CTkEntry(master=tabview.tab("Ceaser-Cipher"), placeholder_text='Shift', width=150,
                                              height=30, border_width=2, corner_radius=10)
    shift_text_entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

    # create a button
    button = customtkinter.CTkButton(master=tabview.tab("Ceaser-Cipher"), text="Encrypt",
                                     command=lambda: button_pressed_encrypt(text, shift_text_entry, text_var))
    button.place(relx=0.3, rely=0.6, anchor=tkinter.CENTER)

    button = customtkinter.CTkButton(master=tabview.tab("Ceaser-Cipher"), text="Decrypt",
                                     command=lambda: button_pressed_dencrypt(text, shift_text_entry, text_var))
    button.place(relx=0.7, rely=0.6, anchor=tkinter.CENTER)

    # create a label for output
    encrypted_val_label = customtkinter.CTkLabel(master=tabview.tab("Ceaser-Cipher"), textvariable=text_var, height=50,
                                                 width=200, bg_color="gray", text_color='black', corner_radius=10)
    encrypted_val_label.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)


def button_pressed_encrypt(plaintext_entry, shift_text_entry, text_var):
    plaintext = str(plaintext_entry.get())
    shift = int(shift_text_entry.get())
    ciphertext = caesar_cipher_encryption(plaintext, shift)
    text_var.set(f"Encrypted value : {ciphertext}")


def button_pressed_dencrypt(ciphertext_entry, shift_text_entry, text_var):
    ciphertext = str(ciphertext_entry.get())
    shift = int(shift_text_entry.get())
    plaintext = caesar_cipher_decryption(ciphertext, shift)
    text_var.set(f"Decrypted value : {plaintext}")

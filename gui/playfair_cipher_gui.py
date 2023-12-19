import tkinter

import customtkinter

from playfair_cipher.decryption import playfair_decryption
from playfair_cipher.encryption import playfair_encryption


def playfair_cipher_frame(tabview, text_entry_playfair, key_text_entry, text_var_playfair):
    frame = customtkinter.CTkFrame(master=tabview.tab("Playfair-Cipher"), width=400, height=200, corner_radius=0,
                                   bg_color='white')
    frame.pack(padx=20, pady=200)
    # create an entry input
    text_entry_playfair = customtkinter.CTkEntry(master=tabview.tab("Playfair-Cipher"), placeholder_text='Text',
                                                 width=150, height=30, border_width=2, corner_radius=10)
    text_entry_playfair.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
    # create an entry input for key value
    key_text_entry = customtkinter.CTkEntry(master=tabview.tab("Playfair-Cipher"), placeholder_text='Key', width=150,
                                            height=30, border_width=2, corner_radius=10)
    key_text_entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
    # create a button
    button = customtkinter.CTkButton(master=tabview.tab("Playfair-Cipher"), text="Encrypt",
                                     command=lambda: button_pressed_playfair_encrypt(text_entry_playfair,
                                                                                     key_text_entry, text_var_playfair))
    button.place(relx=0.3, rely=0.6, anchor=tkinter.CENTER)
    # create a button
    button = customtkinter.CTkButton(master=tabview.tab("Playfair-Cipher"), text="Decrypt",
                                     command=lambda: button_pressed_playfair_decrypt(text_entry_playfair,
                                                                                     key_text_entry,
                                                                                     text_var_playfair))
    button.place(relx=0.7, rely=0.6, anchor=tkinter.CENTER)
    # create a label for output
    encrypted_val_label = customtkinter.CTkLabel(master=tabview.tab("Playfair-Cipher"), textvariable=text_var_playfair,
                                                 height=50, width=200, bg_color="gray", text_color='black',
                                                 corner_radius=10)
    encrypted_val_label.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)


def button_pressed_playfair_encrypt(text_entry_playfair, key_text_entry, text_var_playfair):
    plaintext = text_entry_playfair.get()
    key = key_text_entry.get()
    ciphertext = playfair_encryption(key, plaintext)
    text_var_playfair.set(ciphertext)


def button_pressed_playfair_decrypt(text_entry_playfair, key_text_entry, text_var_playfair):
    ciphertext = text_entry_playfair.get()
    key = key_text_entry.get()
    plaintext = playfair_decryption(key, ciphertext)
    text_var_playfair.set(plaintext)

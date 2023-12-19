import tkinter

import customtkinter

from monoalphabetic_cipher.decryption import monoalphabetic_decrypt
from monoalphabetic_cipher.encryption import monoalphabetic_encrypt


def monoalphabetic_cipher_frame(tabview, text_var_mono, key_generate_mono, cipher_var_mono):
    frame = customtkinter.CTkFrame(master=tabview.tab("Monoalphabetic-Cipher"), width=400, height=200, corner_radius=0,
                                   bg_color='white')
    frame.pack(padx=20, pady=200)
    # create an entry input
    text_entry_mono = customtkinter.CTkEntry(master=tabview.tab("Monoalphabetic-Cipher"), placeholder_text='Plaintext',
                                             width=150, height=30, border_width=2, corner_radius=10)
    text_entry_mono.place(relx=0.3, rely=0.1, anchor=tkinter.CENTER)
    # create an encrypt button
    button = customtkinter.CTkButton(master=tabview.tab("Monoalphabetic-Cipher"), text="Encrypt",
                                     command=lambda: button_pressed_encrypt(text_entry_mono, text_var_mono,
                                                                            key_generate_mono))
    button.place(relx=0.7, rely=0.1, anchor=tkinter.CENTER)
    # create a label for key
    key_decrypt_label = customtkinter.CTkEntry(master=tabview.tab("Monoalphabetic-Cipher"), placeholder_text='Key',
                                               textvariable=key_generate_mono, height=30, width=300, text_color='white')
    key_decrypt_label.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)
    # create a label for output
    encrypted_val_label = customtkinter.CTkLabel(master=tabview.tab("Monoalphabetic-Cipher"),
                                                 textvariable=text_var_mono,
                                                 height=30, width=150, bg_color="gray", text_color='black',
                                                 corner_radius=10)
    encrypted_val_label.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
    # create an entry input
    cipher_entry_mono = customtkinter.CTkEntry(master=tabview.tab("Monoalphabetic-Cipher"),
                                               placeholder_text='Cipher text',
                                               width=150, height=30, border_width=2, corner_radius=10)
    cipher_entry_mono.place(relx=0.3, rely=0.6, anchor=tkinter.CENTER)
    # create a decrypt button
    button = customtkinter.CTkButton(master=tabview.tab("Monoalphabetic-Cipher"), text="Decrypt",
                                     command=lambda: button_pressed_dencrypt(cipher_entry_mono, key_decrypt_label,
                                                                             cipher_var_mono))
    button.place(relx=0.7, rely=0.6, anchor=tkinter.CENTER)
    # create a label for key
    key_label = customtkinter.CTkEntry(master=tabview.tab("Monoalphabetic-Cipher"), placeholder_text='Key',
                                       height=30,
                                       width=300, text_color='white')
    key_label.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)
    # create a label for output
    cipher_val_label = customtkinter.CTkLabel(master=tabview.tab("Monoalphabetic-Cipher"), textvariable=cipher_var_mono,
                                              height=30, width=150, bg_color="gray", text_color='black',
                                              corner_radius=10)
    cipher_val_label.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)


def button_pressed_encrypt(text_entry, text_var_mono, key_generate_mono):
    plaintext = str(text_entry.get())
    ciphertext, key = monoalphabetic_encrypt(plaintext)
    text_var_mono.set(f"Encrypted value : {ciphertext}")
    key_generate_mono.set(f'{key}')


def button_pressed_dencrypt(cipher_entry, key_entry, cipher_var_mono):
    ciphertext = str(cipher_entry.get())
    key = str(key_entry.get())
    plaintext = monoalphabetic_decrypt(ciphertext, key)
    cipher_var_mono.set(f"Decrypted value : {plaintext}")

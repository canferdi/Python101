from tkinter import *
import base64
from tkinter import messagebox


def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def encryptNotes():
    title = entTitle.get()
    message = txtSecret.get(1.0, END)
    key = entKey.get()

    # Control unexpected states
    if len(title) == 0 or len(message) == 0 or len(key) == 0:
        messagebox.showerror("Error", "Please fill in the blanks")
    else:
        encMessage = encode(key, message)
        # Write secret notes to .txt file
        try:
            with open(title + '.txt', 'a') as file:
                file.write(encMessage)
        except FileNotFoundError:
            with open(title + '.txt', 'w') as file:
                file.write(encMessage)
        finally:
            entTitle.delete(0, END)
            txtSecret.delete(1.0, END)
            entKey.delete(0, END)


def decryptNotes():
    encMessage = txtSecret.get(1.0, END)
    key = entKey.get()

    # Control unexpected states
    if len(encMessage) == 0 or len(key) == 0:
        messagebox.showerror(title="Error", message="Please fill in the blanks")
    else:
        try:
            decMessage = decode(key, encMessage)
            txtSecret.delete(1.0, END)
            entKey.delete(0, END)
            txtSecret.insert(1.0, decMessage)
        except (ValueError, TypeError):
            messagebox.showerror(title="Error", message="Please make sure of encrypted info.")


# --GRAPHIC UI--
# Window
window = Tk()
window.minsize(450, 600)
window.config(bg="DarkCyan", padx=20, pady=20)
window.title("Secret Notes")

FONT = ("Arial", 13, "normal")
# Image Label
img = PhotoImage(file="secret2.png")
lblImg1 = Label(image=img, bg="DarkCyan")
lblImg1.pack(side=LEFT, anchor=NW)
lblImg2 = Label(image=img, bg="DarkCyan")
lblImg2.pack(side=RIGHT, anchor=NE)
# Title Label
lblTitle = Label(text="Enter your title", bg="DarkCyan", font=FONT)
lblTitle.pack()
# Title Entry
entTitle = Entry(width=25, bg="Silver", font=FONT)
entTitle.pack()
# Secret Label
lblSecret = Label(text="Enter your secret", bg="DarkCyan", font=FONT)
lblSecret.pack()
# Secret Text
txtSecret = Text(width=40, height=20, bg="Silver", font=FONT)
txtSecret.pack()
# MasterKey Label
lblKey = Label(text="Enter master key", bg="DarkCyan", font=FONT)
lblKey.pack()
# MasterKey Entry
entKey = Entry(width=25, bg="Silver", font=FONT)
entKey.pack(pady=5)
# Save & Encrypt Button
btnEncrypt = Button(text="Save & Encrypt", bg="LightSlateGray", font=FONT, command=encryptNotes)
btnEncrypt.pack(pady=5)
# Decrypt Button
btnDecrypt = Button(text="Decrypt", bg="LightSlateGray", font=FONT, command=decryptNotes)
btnDecrypt.pack(pady=5)

window.mainloop()

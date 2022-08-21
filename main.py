from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters

    shuffle(password_list)

    password = "".join(password_list)

    input_pass.delete(0, END)
    input_pass.insert(0, password)

    pyperclip.copy(password)

    return password

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    file = 'pass.txt'
    page = input_web.get()
    email = input_mail.get()
    password = input_pass.get()

    if 0 in (len(page), len(password), len(email)):
        messagebox.showerror(title="Provide all info", message="Please provide all information.")
    else:
        is_ok = messagebox.askokcancel(title=page, message="These are the details entered: \n"
                                                "Email: {} \n"
                                                "Password: {} \n"
                                                "Is it ok to save?".format(email, password))

        if is_ok:
            with open(file, 'a') as file:
                file.write('{} | {} | {}\n'.format(page, email, password))
                input_web.delete(0, END)
                input_pass.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
# main window
window = Tk()
window.title("Password Manager")
window.minsize(240, 240)
window.config(padx=50, pady=50)

# locker img
canvas = Canvas(width=200, height=200)
locker_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=locker_img)

# labels
label_web = Label(text="Website:")
label_mail = Label(text="Email/Username:")
label_pass = Label(text="Password:")

# inputs
input_web = Entry(width=40)
input_web.focus()
input_mail = Entry(width=40)
input_mail.insert(0, 'zaznaczony@gmail.com')
input_pass = Entry(width=20)

# buttons
butt_gen = Button(text="Generate Password", width=15, command=generate_pass)
butt_add = Button(text="Add", width=35, command=save_password)

# grid
canvas.grid(row=0, column=0, columnspan=3)
label_web.grid(row=1, column=0)
label_mail.grid(row=2, column=0)
label_pass.grid(row=3, column=0)

input_web.grid(row=1, column=1, columnspan=2)
input_mail.grid(row=2, column=1, columnspan=2)
input_pass.grid(row=3, column=1)

butt_gen.grid(row=3, column=2)
butt_add.grid(row=4, column=1, columnspan=2)

window.mainloop()

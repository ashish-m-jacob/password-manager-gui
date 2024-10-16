from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def submit_details():
    website = website_entry.get()
    email = uname_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it okay to save?")

        if is_okay:
            with open("info.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")

                website_entry.delete(0, END)
                pass_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label()
website_label.config(text="Website:")
website_label.grid(row=1, column=0, sticky="w")

uname_label = Label()
uname_label.config(text="Email/username:", justify="right")
uname_label.grid(row=2, column=0, sticky="w")

pass_label = Label()
pass_label.config(text="Password:", justify="right")
pass_label.grid(row=3, column=0, sticky="w")

# Entries
website_entry = Entry(width=42)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
website_entry.focus()

uname_entry = Entry(width=42)
uname_entry.grid(row=2, column=1, columnspan=2, sticky="w")
uname_entry.insert(0, "example@gmail.com")

pass_entry = Entry(width=21, justify="left")
pass_entry.grid(row=3, column=1, columnspan=1, sticky="w")

# Buttons
gen_pass = Button(text="Generate Password", justify="left", command=gen_pass)
gen_pass.grid(row=3, column=2)

add_button = Button(text="Add", width=59, command=submit_details)
add_button.grid(row=4, column=0, columnspan=3, sticky="e")

window.mainloop()
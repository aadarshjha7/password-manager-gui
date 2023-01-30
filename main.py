from tkinter import *
from tkinter import messagebox

screen = Tk()
screen.title("Password Manager")
screen.config(padx=20, pady=30)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo, )
canvas.grid(column=1, row=0, )
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_label = Label(text="User ID:")
email_label.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=35)
password_entry.grid(column=1, row=3, columnspan=2)


def add():
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Error", message="Don't leave any fields blank!")
        return

    with open("data.txt", "a") as file:
        file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)
    messagebox.showinfo(title="Success", message="Your data has been saved!")


add_button = Button(text="Add", width=26, command=add)
add_button.grid(column=1, row=4, columnspan=2, padx=10, pady=10)

screen.mainloop()

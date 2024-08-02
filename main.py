from tkinter import *
from tkinter import messagebox
import random

FONT_NAME = "Courier"
pass_dict = {
    1: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
    2: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
    3: ['!', '#', '$', '%', '&', '(', ')', '*', '+']

}



def clear_entry():
    web_entry.delete(0, END)
    email_entry.delete(0, END)
    pass_entry.delete(0, END)
    is_ok = messagebox.askyesno(title="Reset to Default?", message="Set email to patrickdamoose@gmail.com?")
    if is_ok:
        email_entry.insert(0, "patrickdamoose@gmail.com")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    final_list = []
    tempvar = 1
    if "Numbers" in listbox.selection_get() and "Symbols" not in listbox.selection_get():
        tempvar = 2
    elif "Symbols" in listbox.selection_get():
        tempvar = 3
    temp_int = random.randint(8, 14)
    for n in range(0, temp_int):
        dict_pull_var = random.randint(1, tempvar)
        dict_pull = pass_dict[dict_pull_var]
        pick = random.choice(dict_pull)
        final_list.append(pick)
    print(final_list)
    final = "".join(final_list)
    pass_entry.delete(0, END)
    pass_entry.insert(0, final)




# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    print(f"{website} {email} {password}")

    if website == 0 or email == 0:
        messagebox.showerror(title="Invalid Entry", message="One or more fields have no characters entered.")
    else:
        is_ok = messagebox.askokcancel(title=f"{website} Entry", message=f"You have entered the following information\n"
                                                                         f"Email: {email}\n Password: {password}\n"
                                                                         f"Is this okay?")
        if is_ok:
            with open("data.txt", "a") as my_file:
                my_file.write(f"{website} | {email} | {password}\n")
            clear_entry()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=90, pady=90)

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=210, highlightthickness=0)
canvas.create_image(105, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
web_label = Label(text="Website:", font=(FONT_NAME, 14))
web_label.grid(row=1, column=0)

email_label = Label(text="Email:", font=(FONT_NAME, 14))
email_label.grid(row=2, column=0)

pass_label = Label(text="Pass:", font=(FONT_NAME, 14))
pass_label.grid(row=3, column=0)

# Entry
web_entry = Entry(width=35)
web_entry.focus()
web_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.insert(0, "patrickdamoose@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

# Buttons

gen_button = Button(text="Generate", command=generate)
gen_button.grid(row=3, column=2)

add_button = Button(text="Add", command=add, width=36)
add_button.grid(row=4, column=1, columnspan=2)

# Listbox test
list_label = Label(text="Password Generation Complexity")
list_label.grid(row=5, column=1, columnspan=2)
choices = ["Letters", "Letters and Numbers", "Letters, Numbers, and Symbols"]
choicesvar = StringVar(value=choices)
listbox = Listbox(listvariable=choicesvar, height=3, width=30)
listbox.selection_set(0)
listbox.grid(row=6, column=1, columnspan=2)

window.mainloop()

from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
char = random.randint(8, 10)
symbol = random.randint(1, 2)
number = random.randint(1, 2)

def gen_pswd():
    # Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    letter = [password_list.append(random.choice(letters)) for _ in range(nr_letters)]

    sym = [password_list.append(random.choice(symbols)) for _ in range(nr_symbols)]

    num = [password_list.append(random.choice(numbers)) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    input3.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def search():
    try:
        with open("Passwords.json") as data_file:
            data = json.load(data_file)
            pswd = str(data[input1.get()]["password"])
            email = str(data[input1.get()]["email"])
        messagebox.showinfo(title=input1.get(), message=f"webside: {input1.get()}\nemail: {email}\n"
                                                        f"password: {pswd}")
    except KeyError:
        messagebox.showinfo(title="Error", message="Sorry, No data available")
    except FileNotFoundError:
        messagebox.showinfo(title="FileNotFoundError", message="First Add some data then try!")


def save_file():
    webside = input1.get()
    email = input2.get()
    pswd = input3.get()
    new_data = {
        webside: {
            "email": email,
            "password": pswd
        }
    }
    if len(webside) == 0 or len(email) == 0 or len(pswd) == 0:
        messagebox.showinfo(title="Error", message="You left places empty")

    else:
        is_ok = messagebox.askokcancel(title='Title', message=f"These are the detail "
                                                              f"enter:\nemail: {email}\n"
                                                      f"webside: {webside}\npassword: {pswd}")
        if is_ok:
            try:
                with open("Passwords.json", "r") as file:
                    # json.dump(new_data, file, indent=4)
                    # reading old data
                    data = json.load(file)
            except FileNotFoundError:
                print("file not found error")
                with open("Passwords.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)
                with open("Passwords.json", "w") as file:
                    # Saving new data into the file
                    json.dump(data, file, indent=4)

            finally:
                input1.delete(0, END)
                input3.delete(0, END)
                input1.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0, columnspan=2)

# Label1 (Website:)
label1 = Label(text="Website:")
label1.grid(column=0, row=1)

# Label2 (Email)
label2 = Label(text="Email/Username:")
label2.grid(column=0, row=2)

# Label3 (Password)
label3 = Label(text="Password:")
label3.grid(column=0, row=3)

# Entry1
input1 = Entry(width=25)
input1.grid(column=0, row=1, columnspan=3)
input1.focus()

# Entry2
input2 = Entry(width=40)
input2.insert(0, "youremail@gmail.com")
input2.grid(column=1, row=2, columnspan=2)

# Entry 3
input3 = Entry(width=25)
input3.grid(column=1, row=3, columnspan=1)
# ........................save Password ..................................#

# buttons
gen_psw = Button(text="Generate Password", command=gen_pswd)
gen_psw.grid(column=2, row=3, columnspan=3)

add = Button(text="Add", width=36, command=save_file)
add.grid(column=1, row=4, columnspan=3)

search = Button(text="Search", width=15, command=search)
search.grid(column=2, row=1, columnspan=3)


window.mainloop()

import tkinter as tk
import json
import os.path
from pathlib import Path

height = 600
width = 400


def get_data():
    output = ''
    with open('data.txt') as json_file:
        data = json.load(json_file)
        for p in data:
            username = '\nUsername: ' + p['username']
            password = '\nPassword: ' + p['password'] + \
                '\n----------------------------------------\n'
            output += f'{username} {password}'

    return output


def write_data(username, password):
    data = [
        {
            "username": username,
            "password": password
        }
    ]
    if(Path("data.txt").exists()):
        if(os.stat("data.txt").st_size != 0):
            with open('data.txt') as data_file:
                old_data = json.load(data_file)
                data += old_data

    with open('data.txt', 'w', encoding='utf-8') as of:
        json.dump(data, of, ensure_ascii=False, indent=4)


root = tk.Tk()

# Maximize Window
# root.state('zoomed')

canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()

first_frame = tk.Frame(root)
first_frame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.08)

second_frame = tk.Frame(root)
second_frame.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.08)

third_frame = tk.Frame(root)
third_frame.place(relx=0.25, rely=0.3, relwidth=0.5, relheight=0.08)

fourth_frame = tk.Frame(root)
fourth_frame.place(rely=0.4, relwidth=1, relheight=1)

username = tk.Entry(first_frame, justify='center',
                    font=('Times New Roman', 15))
username.insert(0, 'USERNAME')
username.bind("<FocusIn>", lambda args: username.delete('0', 'end'))
username.place(relwidth=1, relheight=1)

password = tk.Entry(second_frame, justify='center',
                    font=('Times New Roman', 15), show='*')
password.insert(0, 'PASSWORD')
password.bind("<FocusIn>", lambda args: password.delete('0', 'end'))
password.place(relwidth=1, relheight=1)

button = tk.Button(third_frame, bg='#ed4f3b', text='Submit',
                   command=lambda: write_data(username.get(), password.get()),
                   font=('Times New Roman', 19))
button.place(relwidth=1, relheight=1)

label = tk.Label(fourth_frame, font=('Times New Roman', 13), bg='#C4C7E3')
if(Path("data.txt").exists()):
    if(os.stat("data.txt").st_size != 0):
        label['text'] = get_data()
label.place(relwidth=1)


root.mainloop()

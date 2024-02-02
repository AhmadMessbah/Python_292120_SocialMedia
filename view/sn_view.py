from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg


def reset_form():
    send.set("")
    share.set("")


def share_btn():
    msg.showinfo("Post", "Shared")
    reset_form()


def send_btn():
    msg.showinfo("massage", "Sent")
    reset_form()


def log_in():
    msg.showinfo("Log In", "Successful")


def update_password():
    msg.showinfo("Password", "Upgraded")


def update_username():
    msg.showinfo("Username", "Upgraded")


def delete_account():
    msg.showinfo("Account", "Deleted")


def share():
    pass


def send():
    pass


win = Tk()
win.geometry("700x500")
win.title("Twitter")

# BIO
# lbl = Label(win, width=65, height=5, bg="gray49")
# lbl.bind()
# lbl.place(x=20, y=5)
Label(win, text="BIO").place(x=40, y=10)
Label(win, text="Followers :").place(x=40, y=50)
Label(win, text="Followings :").place(x=190, y=50)
Label(win, text="Posts :").place(x=360, y=50)

# Log In
Label(win, text="Log In :").place(x=600, y=180)
Label(win, text="Username :").place(x=591, y=100)
Label(win, text="Password :").place(x=591, y=50)
Button(win, text="Log In", command=log_in, width=15).place(x=565, y=150)
user = StringVar()
Entry(win, textvariable=user, width=18).place(x=565, y=75)
pas = StringVar()
Entry(win, textvariable=pas, width=18).place(x=565, y=125)

# Settings
Label(win, text="Setting :").place(x=600, y=180)
setting = StringVar()
Button(win, text="Update Password", command=update_password, width=15).place(x=565, y=240)
Button(win, text="Update Username", command=update_username, width=15).place(x=565, y=270)
Button(win, text="Delete Account", command=delete_account, width=15).place(x=565, y=210)

# Directs
sender = ttk.Combobox(win)
sender["values"] = ["user 1", "user 2"]
sender["state"] = "readonly"
sender.current(1)
sender.place(x=340, y=100)

table = ttk.Treeview(win, columns="a", show="headings", height=15)
table.heading("a", text="Direct")
table.place(x=340, y=120)

send = StringVar()
Entry(win, textvariable=send, width=33).place(x=340, y=450)
Button(win, text="send", command=send_btn).place(x=545, y=450)

# Posts
table = ttk.Treeview(win, columns="a", show="headings", height=15)
table.heading("a", text="Posts")
table.place(x=40, y=120)

share = StringVar()
Entry(win, textvariable=share, width=33).place(x=40, y=450)
Button(win, text="share", command=share_btn).place(x=245, y=450)

win.mainloop()

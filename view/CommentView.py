from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

from controller import CommentController
from controller.post_controller import PostController
from controller.user_controller import UserController
from model.entity import *


class CommentView():
    def __init__(self):
        self.win = Tk()
        self.win.geometry("1100x400")
        self.win.title("Comment Feed")
        self.controller = CommentController()

        Label(self.win, text="Comment Id").place(x=20, y=20)
        self.comment_id = IntVar()
        Entry(self.win, state="readonly", textvariable=self.comment_id).place(x=120, y=20)

        Label(self.win, text="Comment Text").place(x=20, y=60)
        self.comment_text = StringVar()
        Entry(self.win, textvariable=self.comment_text).place(x=120, y=60)

        Label(self.win, text="username").place(x=20, y=100)
        self.username = StringVar()
        Entry(self.win, state="readonly", textvariable=self.username).place(x=120, y=100)

        Label(self.win, text="Post ID").place(x=20, y=140)
        self.post_id = StringVar()
        Entry(self.win, state="readonly", textvariable=self.post_id).place(x=120, y=140)

        Label(self.win, text="Post Text").place(x=20, y=180)
        self.post_text = StringVar()
        Entry(self.win, state="readonly", textvariable=self.post_text).place(x=120, y=180)

        self.table = ttk.Treeview(self.win, columns=(1, 2, 3, 4, 5), show="headings")

        self.table.column(1, width=80)
        self.table.column(2, width=300)
        self.table.column(3, width=100)
        self.table.column(4, width=60)
        self.table.column(5, width=300)

        self.table.heading(1, text="Comment ID")
        self.table.heading(2, text="Comment Text")
        self.table.heading(3, text="UserName")
        self.table.heading(4, text="Post ID")
        self.table.heading(5, text="Post Text")

        self.table.bind("<<TreeviewSelect>>", self.Select_Post)

        Button(self.win, text="Save", width=8, command=self.Save_Click).place(x=20, y=300)
        Button(self.win, text="Edit", width=8, command=self.Edit_Click).place(x=100, y=300)
        Button(self.win, text="Remove", width=8, command=self.Remove_Click).place(x=180, y=300)
        Button(self.win, text="New Comment", width=14, command=self.reset_form).place(x=80, y=250)

        self.table.place(x=250, y=18)

        self.reset_form()
        self.win.mainloop()

    def Save_Click(self):
        pass
        # message = self.controller.save(self.text.get(), UserController.current_user)
        # msg.showinfo("Save", message)

        # self.reset_form()

    def Edit_Click(self):
        pass
        # if self.username.get() == UserController.current_user.username:
        #     message = self.controller.edit(self.id.get(),self.text.get(), UserController.current_user)
        #     msg.showinfo("Edit", message)
        # else:
        #     msg.showerror("Error", "This Post Doesnt Belong to You")
        # self.reset_form()

    def Remove_Click(self):
        pass
        # if self.username.get() == UserController.current_user.username:
        #     self.controller.remove(self.id.get())
        #     msg.showinfo("removed", "Post was removed")
        # else:
        #     msg.showerror("Error", "This Post Doesnt Belong to You")
        # self.reset_form()

    def reset_form(self):
        for item in self.table.get_children():
            self.table.delete(item)

        for comment in self.controller.find_all():
            self.table.insert("", END, values=[comment.id, comment.text, comment.user.username, comment.post.id, comment.post.text])

        self.comment_id.set("")
        self.comment_text.set("")
        self.username.set(UserController.current_user.username)
        self.post_id.set("")
        self.post_text.set("")

    def Select_Post(self, event):
        selected_item = self.table.focus()
        comment = self.table.item(selected_item, "values")
        if comment:
            self.comment_id.set(comment[0])
            self.comment_text.set(comment[1])
            self.username.set(comment[2])
            self.post_id.set(comment[3])
            self.post_text.set(comment[4])




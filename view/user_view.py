from tkinter import *
from view.Post_View import PostView

class UserView:
    def __init__(self, user):
        self.window = Tk()
        self.window.geometry("300x300")
        self.window.title("User Profile")
        self.user = user
        Label(self.window, text=user.name, font=("Arial", 20)).pack()

        if user.status == True:
            Button(self.window, width=8, text="Post", command=self.open_post_view).pack()
            Button(self.window, width=8, text="Like").pack()
            Button(self.window, width=8, text="Comment").pack()
        else:
            Label(self.window, text="Suspended Account", font=("Arial", 20)).pack()

        self.window.mainloop()

    def open_post_view(self):
        self.window.destroy()
        PostView(self.user)

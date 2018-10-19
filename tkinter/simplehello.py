#simplehello.py cwc
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()

"""

root = Tk()
To initialize Tkinter, we have to create a Tk root widget.
This is an ordinary window,
with a title bar and other decoration provided by your window manager.
You should only create one root widget for each program,
and it must be created before any other widgets.

https://docs.python.org/3.7/library/tkinter.html

"""

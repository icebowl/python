import tkinter as tk

class MainMenu:
    def __init__(self, master,*args,**kwargs):
        self.master = master
        self.master.minsize(500, 500)
        self.frame = tk.Frame(self.master, relief='raised', borderwidth=1, background="#00ff00")
        #    self.frame = tk.Frame(self.frame, )
        self.button1 = tk.Button(self.frame, text = 'Choas', width = 25, command = self.new_window)
        self.button1.pack()
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.place(x=100, y=100, anchor="nw", width=400, height=400)
        self.frame.pack(expand=True, fill='both')

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = ChoasWindow(self.newWindow)
    def close_windows(self):
        self.master.destroy()

class ChoasWindow:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()

if __name__ == '__main__':
    main()

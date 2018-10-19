import tkinter as tk

class MenuApp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.root.columnconfigure(0, weight = 0)
        self.root.rowconfigure(0, weight = 0)

        main_frame = tk.Frame(self.root, width = 500, height = 400, background = "#cccccc")
        main_frame.columnconfigure(0, weight = 0)
        main_frame.rowconfigure(0, weight = 0)
        main_frame.grid(row  = 0, column = 0)
        main_frame.place(x = 100, y = 100)

        label_frame = tk.Frame(main_frame, width = 200, height = 105, background = "blue")
        label_frame.grid(row  = 0, column = 0)

        button_frame = tk.Frame(main_frame, width = 100, height = 100, background = "green")
        button_frame.grid(row  = 1, column = 0)

def main():
    root = tk.Tk()
    MyApp = MenuApp(root)
    tk.mainloop()

if __name__ == '__main__':
    main()

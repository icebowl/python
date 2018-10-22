import tkinter as tk
from chaos_spiral import *
class MainMenu:
    def __init__(self, master,*args,**kwargs):
        self.master = master
        self.master.minsize(500, 500)
        self.master.wm_title("MENU")
        self.master.option_add("*Font", "helvetica")
        # start frame
        self.frame = tk.Frame(self.master, relief='raised', borderwidth=1, background="#eee8d5")
        self.frame.place(x=100, y=100,                    )

        self.button1 = tk.Button(self.frame, text = 'Chaos', width = 25, command = chaos)
        #self.button1 = tk.Button(self.frame, text = 'Chaos', width = 25, command = self.new_window)
        self.button1.pack()
        self.button2 = tk.Button(self.frame, text = 'Spiral', width = 25, command = callSpiral)
        #self.button1 = tk.Button(self.frame, text = 'Chaos', width = 25, command = self.new_window)
        self.button2.pack()
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.text1 = tk.Label(self.frame, text="Chaos (Sierpinski Triangle) : CW Coleman",font=('courier', '10'),background="#eee8d5" )
        self.text2 = tk.Label(self.frame, text="Resursion (Pop S0AR): CW Coleman : CW Coleman",font=('courier', '12'),background="#eee8d5" )
        self.text3 = tk.Label(self.frame, text = "SOAR (Stack of Activation Records)",font=('courier', '10'), background="#eee8d5")
        self.text1.pack()
        self.text2.pack()
        self.text3.pack()
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


"""

https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application
$base03:    #002b36;
$base02:    #073642;
$base01:    #586e75;
$base00:    #657b83;
$base0:     #839496;
$base1:     #93a1a1;
$base2:     #eee8d5;
$base3:     #fdf6e3;
$yellow:    #b58900;
$orange:    #cb4b16;
$red:       #dc322f;
$magenta:   #d33682;
$violet:    #6c71c4;
$blue:      #268bd2;
$cyan:      #2aa198;
$green:     #859900;

"""

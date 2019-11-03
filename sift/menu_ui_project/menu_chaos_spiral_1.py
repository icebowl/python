import tkinter as tk
from PIL import Image, ImageTk
from chaos_spiral import *
from ulam_circle import *
class MainMenu:
    def __init__(self, master,*args,**kwargs):
        self.master = master
        self.master.minsize(700, 700)
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
        self.button3 = tk.Button(self.frame, text = 'Ulam', width = 25, command = ulam)
        self.button3.pack()
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.text = tk.Label(self.frame, text="* * * * * * * * * * * * * \n \
Chaos (Sierpinski Triangle) \n  \
* * * * * * * * * * * * * \n  \
Spiral Resursion: \n \
{pop stack of activation records} \n \
* * * * * * * * * * * * * \n \
Ulam Spiral \n \
{turtle version with vector list) \n \
Cw. Coleman",font=('courier', '10'),background="#eee8d5" )
        self.text.pack()
        self.frame.pack(expand=True, fill='both')
        # display image
        load = Image.open("solarized-palette.png")
        render = ImageTk.PhotoImage(load)
        # labels can be text or images
        self.img = tk.Label(self.frame, image=render)
        self.img.image = render
        self.img.place(x=50, y=400)
        # * * * * * * * * *

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
apt install python3-pil python-pil python3-pil.imagetk python-pil.imagetk;
apt install python3-pil python-pil
apt install python3-pil.imagetk
apt install python-pil.imagetk

https://pythonprogramming.net/tkinter-adding-text-images/
https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application
https://stackoverflow.com/questions/23901168/how-do-i-insert-a-jpeg-image-into-a-python-tkinter-window
$base03:    #002b36; (dark grey)
$base02:    #073642;
$base01:    #586e75;
$base00:    #657b83;
$base0:     #839496;
$base1:     #93a1a1;
$base2:     #eee8d5; (cream)
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

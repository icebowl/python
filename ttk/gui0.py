# https://stackoverflow.com/questions/13926789/python-ttk-using-labelframes-to-clean-up-a-frame
from tkinter import *
from tkinter import ttk

class MakeGUI(object):
    def __init__(self,root):
        self.root = root
        self.root.title("Text Comparitor")
        ## build frame
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.pack()
        ## text labels
        ttk.Label(self.mainframe, text="Conversion Truth Tester", font=("Helvetica", 32)).grid(column=1, row=1, sticky=E)
        self.mainframe.pack(side="bottom", fill=BOTH, expand=True)
        self.mainframe.grid()
        ttk.Label(self.mainframe, text="Source Filename:").grid(column=1, row=2, sticky=W)
        ttk.Label(self.mainframe, text="Source Text:").grid(column=1, row=3, sticky=W)
        ttk.Label(self.mainframe, text="Converted Text:").grid(column=1, row=4, sticky=W)
        ttk.Label(self.mainframe, text="Cleaned Source:").grid(column=1, row=5, sticky=W)
        ttk.Label(self.mainframe, text="Cleaned Converted:").grid(column=1, row=6, sticky=W)
        ttk.Label(self.mainframe, text="Details:").grid(column=1, row=7, sticky=W)
        ## buttons
        self.close = ttk.Button(self.mainframe, text="Close",command=self.closeFrame).grid(column=1, row=9, sticky=SE)
        self.next = ttk.Button(self.mainframe, text="Next",command=self.nextPara).grid(column=1, row=9, sticky=S)
        self.next = ttk.Button(self.mainframe, text="Prev",command=self.prevPara).grid(column=1, row=9, sticky=SW)

    def closeFrame(self):
        self.root.destroy()

    def nextPara(self):
        pass

    def prevPara(self):
        pass

def main():
    root = Tk()
    makeGUI = MakeGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()

import sys,tty,termios
class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def get():
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k=='\x1b[A':
                print ("up")
        elif k=='\x1b[B':
                print ("down")
        elif k=='\x1b[C':
                print ("right")
        elif k=='\x1b[D':
                print ("left")
        else:
                print ("not an arrow key!")

def main():
        for i in range(0,20):
                get()

if __name__=='__main__':
        main()

'''
File descriptor is a low-level concept, it's an integer that represents an open file. Each open file is given a unique file descriptor.
In Unix, by convention, the three file descriptors 0, 1, and 2 represent standard input, standard output, and standard error, respectively.

>>> import sys
>>> sys.stdin.fileno()
0
>>> sys.stdout.fileno()
1
>>> sys.stderr.fileno()
2

tty.setraw(fd, when=termios.TCSAFLUSH)
    Change the mode of the file descriptor fd to raw. If when is omitted, it defaults to termios.TCSAFLUSH, and is passed to termios.tcsetattr().
tty.setcbreak(fd, when=termios.TCSAFLUSH)
    Change the mode of file descriptor fd to cbreak. If when is omitted, it defaults to termios.TCSAFLUSH, and is passed to termios.tcsetattr().



'''

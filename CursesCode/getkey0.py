import curses
import os

def main(stdsrc):
    stdsrc.nodelay(True)
    key=""
    stdsrc.clear()                
    stdsrc.addstr("Detected key:")
    while 1:          
        try:                 
           key = stdsrc.getkey()         
           stdsrc.clear()                
           stdsrc.addstr("Detected key:")
           stdsrc.addstr(str(key)) 
           if key == os.linesep:
              break           
        except Exception as e:
           # No input   
           pass         

curses.wrapper(main)

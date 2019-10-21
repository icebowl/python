'''
Python asigns __main__ to __name__  when python runs a file.
When python imports a file (module) it sets the name of __name__ to the name of the file.


'''
#import module_1
def printCWC():
    print(" CCC W     W     W CCC") 
    print("C     W   W W   W C   ")
    print("C      W W   W W  C   ")
    print(" CCC    W     W    CCC")
    
def main():
    print("thename.py file")
    print(__name__)
    printCWC()
    printCWC()

if __name__ == '__main__':    
    main()

import thename
print ("This is module_1.py")
#printCWC()
def main():
    print("thename.py file")
    print(__name__)
    thename.printCWC()

if __name__ == '__main__':    
    main()

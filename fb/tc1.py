from termcolor2 import c

# termcolor2
#print c("hello").red.on_white.blink.underline.dark

# ---  this is equal to the following ---

# termcolor
print (colored("hello", "red", "on_white", ["blink", "underline", "dark"]))

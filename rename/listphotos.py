#!/usr/bin/python
# https://www.tutorialspoint.com/python/os_listdir.htm

import os, sys

# Open a file
path = "~/http/wooten/photos/wootenphotos2018/"
dirs = os.listdir( path )

# This would print all the files and directories
for file in dirs:
   print (file)

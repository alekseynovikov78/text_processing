import os
import sys
import fnmatch


#to run the sctipt: python replace_lines2.py files_location
#The script just chanes line breaks from \n to \r\n, so that the line breaks show on both macs and pcs.

for arg in sys.argv[1:]:
    if fnmatch.fnmatch(arg, '*.txt'):
        fileContents = open(arg, "r").read()
        f= open(arg, "w", newline = "\r\n")
        f.write(fileContents)
        f.close



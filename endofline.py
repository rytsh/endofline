#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 22:03:23 2018

@author: ray
"""
import sys
import signal
import re

def signal_handler(signal, frame):
    """Catch Ctrl+C."""
    print('Exit!')
    sys.exit(1)

def linereg(line):
    return re.sub(r"(\s+)$","",line)

def main(readfile, writefile):
    try:
        with open(readfile, 'rt', encoding='utf-8') as f:
            with open(writefile, 'w', encoding = 'utf-8') as fw:
                for line in f:
                    #print(linereg(line))
                    fw.write(linereg(line) + "\n")
    
    except OSError as err:
        print("OS error: {0}".format(err))
        return False

    return True

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    
    if len(sys.argv) < 3:
        print("Give 2 filename one for read one for write")
        sys.exit(1)

    if sys.argv[1] != sys.argv[2]:
        if main(sys.argv[1],sys.argv[2]):
            print("======FINITO======")
    else:
        print("Wrong Argument")
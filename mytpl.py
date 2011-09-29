#!/usr/bin/python

import os
import sys

def init():
    if os.system("which 'git' > /dev/null") != 0:
        print >>sys.stderr, "Can't managed to find git, abort"
        sys.exit(1)

if __name__ == "__main__":
    init()

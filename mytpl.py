#!/usr/bin/python

import os
import sys

def init():
    if os.system("which 'git' > /dev/null") != 0:
        print >>sys.stderr, "Can't managed to find git, abort"
        sys.exit(1)
    if not os.path.exists(os.path.expanduser("~/.config/mytemplates/")):
        print "Creating templates dir in %s" % os.path.expanduser("~/.config/mytemplates/")
        os.mkdir(os.path.expanduser("~/.config/mytemplates/"))
    if os.system("cd ~/.config/mytemplates/ && git status > /dev/null 2>&1") != 0:
        print "Cloning templates in %s" % os.path.expanduser("~/.config/mytemplates/")
        if os.system("git clone git://github.com/Psycojoker/mytemplates.git ~/.config/mytemplates/") != 0:
            print sys.stderr, "Didn't managed to clone git repository in %s" % os.path.expanduser("~/.config/mytemplates/")
            print sys.stderr, "Abort"

if __name__ == "__main__":
    init()

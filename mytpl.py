#!/usr/bin/python

import os
import sys

DIR = os.path.expanduser("~/.config/mytemplates/")
GITURL = "git://github.com/Psycojoker/mytemplates.git"

def init():
    if os.system("which 'git' > /dev/null") != 0:
        print >>sys.stderr, "Can't managed to find git, abort"
        sys.exit(1)
    if not os.path.exists(DIR):
        print "Creating templates dir in %s" % DIR
        os.mkdir(DIR)
    if os.system("cd %s && git status > /dev/null 2>&1" % DIR) != 0:
        print "Cloning templates in %s" % DIR
        if os.system("git clone %s %s" % (GITURL, DIR)) != 0:
            print sys.stderr, "Didn't managed to clone git repository in %s" % DIR
            print sys.stderr, "Abort"

def load_templates():
    return filter(lambda x: x[0] != ".", os.listdir(DIR))

def manage_user_input(input, templates):
    if not input:
        print "Templates available:"
        print "\n".join(map(lambda x: " * " + x, templates))

if __name__ == "__main__":
    init()
    manage_user_input(sys.argv[1:], load_templates())

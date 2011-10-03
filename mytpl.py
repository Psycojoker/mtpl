#!/usr/bin/python

import os
import sys
import re

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

def _find_template(input, templates):
    return input[0] if input and input[0] in templates else False

def list_templates_and_quit(templates, exit=0):
    print "Templates available:"
    print "\n".join(map(lambda x: " * " + x, templates))
    sys.exit(exit)

def get_template(input, templates):
    if input[0] in templates:
        return input[0]

    good = filter(lambda x: re.match("^.*" + ".*".join(input[0]) + ".*$", x), templates)

    if len(good) == 1:
        print >>sys.stderr, ">>> matching '%s' <<<\n" % good[0]
        return good[0]

    if good:
        list_templates_and_quit(good)

    return None

def manage_user_input(input, templates):
    if not input:
        list_templates_and_quit(templates)

    template = get_template(input, templates)

    if template is None:
        print "Error: '%s' not an available template\n" % input[0]
        list_templates_and_quit(templates, exit=1)

    sys.stdout.write(open(DIR + template, "r").read())

if __name__ == "__main__":
    init()
    manage_user_input(sys.argv[1:], load_templates())

#!/usr/bin/python
# -*- coding:Utf-8 -*-

from setuptools import setup

setup(name='mtpl',
      version='0.2.1',
      description='scripts templates manager that use git',
      author='Laurent Peuch',
      long_description=open("README").read(),
      author_email='cortex@worlddomination.be',
      url='http://worlddomination.be/projects/mtpl.html',
      license= 'GPLv3+',
      # list of scripts supplied by your application
      scripts=['mtpl', 'mytemplates'],
      keywords='templates script cli git',
     )

# vim:set shiftwidth=4 tabstop=4 expandtab:

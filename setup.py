#!/usr/bin/env python
# -*- coding=utf-8 -*-
# Semplice Backup setup file
# Copyright © 2011 Semplice Team. All rights reserved.

import os, glob
from distutils.core import setup

# Taken from pylaivng (https://launchpad.net/pylaivng) setup.py. © Eugenio "g7" Paolantonio
tree = []
current_dir = os.getenv("PWD")

def generate_tree(directory, where):
	""" Generates a directory tree to be used with data_files.
	SYNTAX: generate_tree(directory, where)
	directory = directory to 'tree-ize'
	where = location to install the tree
	
	Examples:
	generate_tree("data","/var/www/pylaivng") - will generate a tree that will copy data/ directory in /var/www/pylaivng
	generate_tree("config/distributions", "/etc/pylaivng") - will generate a tree that will copy config/distributions in /etc/pylaivng/distributions """
	
	# Enter in the directory before the one that we should make the tree...
	if os.path.dirname(directory): os.chdir(os.path.dirname(directory))
	
	for root, dirs, files in os.walk(os.path.basename(directory)):
		filelist = []
		# adjust root
		if os.path.dirname(directory):
			root_real = os.path.join(os.path.dirname(directory), root)
		else:
			root_real = root

		if files:
			for filename in files:
				filelist.append(os.path.join(root_real, filename))
			if filelist:
				tree.append((os.path.join(where, root), filelist))
	
	# Return into current_dir
	os.chdir(current_dir)

generate_tree("sb", "/usr/share/sb/")

setup(name = "sb",
      version = "0.1",
      author = 'Luca B. (tuxpenguin)',
      author_email = "sidtux@gmail.com",
      description = "A simple backup program.",
      url = "http://semplice-linux.sourceforge.net",
      packages=['sb'],
      scripts=['sb/sb.py','sb/sbc.py'],
      data_files=tree,
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Topic :: Utilities",
          "License :: OSI Approved :: GNU General Public License (GPL)",
      ],
      requires=['os', 'sys', 'gi', 'sqlite3', 'tarfile', 'zipfile', 'time', 'ftplib', 'gettext']
)

#!/usr/bin/env python
# -*- coding=utf-8 -*-
# Semplice Backup setup file
# Copyright © 2011 Semplice Team. All rights reserved.

import os
from distutils.core import setup

setup(name = "sb",
      version = "0.1",
      author = 'Luca B. (tuxpenguin)',
      author_email = "sidtux@gmail.com",
      description = "A simple backup program.",
      url = "http://semplice-linux.sourceforge.net",
      packages=['sb'],
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Topic :: Utilities",
          "License :: OSI Approved :: GNU General Public License (GPL)",
      ],
      requires=['os', 'sys', 'gi', 'sqlite3', 'tarfile', 'zipfile', 'time', 'ftplib', 'gettext']
)

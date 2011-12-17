# -*- coding=utf-8 -*-
# Semplice Backup Compress Library
# Copyright © 2011 Semplice Team. All rights reserved.

import os, sys, tarfile, zipfile, libdb, time

class compress:
	""" This class cointains the functions that helps the program to compress files. """
	
	def backup(self, bk_file, directory, mode):		
		if mode == "bz2":
			ext = ".tar.bz2"
			op = "bz2"
		elif mode == "gz":
			ext = ".tar.gz"
			op = "gz"
		elif mode == "zip":
			ext = ".zip"
			op = ""
		
		name = time.strftime("sb%Y-%m-%d_%H.%M")
		if mode == "zip":
			archive = zipfile.ZipFile(directory + '/' + name + ext, "w")
			for x in bk_file:
				archive.write(x)
            archive.write('/tmp/.files.db')
			archive.close()
		else:
			archive = tarfile.open(directory + '/' + name + ext, "w:%s" % op)
			for x in bk_file:
				archive.add(x)
            archive.add('/tmp/.files.db')
			archive.close()
		
		self.archname = name + ext
		self.dirs = os.path.abspath(directory + "/" + name + ext)

    #def restore(self, bk_file):
        
        

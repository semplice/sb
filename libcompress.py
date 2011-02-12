# -*- coding=utf-8 -*-
# Semplice Backup 0.1
# Formerly known as µBackup 5.

import os, sys, tarfile, zipfile, libftp, time

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
			archive = zipfile.ZipFile(directory + name + ext, "w")
			archive.write(bk_file)
			archive.close()
		else:
			archive = tarfile.open(directory + name + ext, "w:%s" % op)
			archive.add(bk_file)
			archive.close()
		
		self.archname = name + ext
		self.dirs = os.path.abspath(directory + "/" + name + ext)

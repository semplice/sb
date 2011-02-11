# -*- coding=utf-8 -*-
# Semplice Backup 0.1
# Formerly known as µBackup 5.

import os, sys, tarfile, zipfile, libftp

class compress:
	""" This class cointains the functions that helps the program to compress files. """
	
	def backup(directory, ftp, mode):
		
		if mode == "bz2":
			ext = ".tar.bz2"
			op = "bz2"
		elif mode == "gz":
			ext = ".tar.gz"
			op = "gz"
		elif mode == "zip":
			ext = ".zip"
			op = ""
		
		name = strftime(pattern, gmtime())
		if mode == "zip":
			archive = zipfile.ZipFile(name + ext, "w")
			archive.write(directory)
			archive.close()
		else:
			archive = tarfile.open(name + ext, "w:%s" % op)
			archive.add(directory)
			archive.close()
		
		archname = name + ext
		dirs = directory

	def backup_gz(directory, ftp):
		self.backup(directory, ftp, "gz")
	
	def backup_bz2(directory, ftp):
		self.backup(directory, ftp, "bz2")
	
	def backup_zip(directory, ftp):
		self.backup(directory, ftp, "zip")

#class libcompress:
#    # The function that makes backups in tar.bz2 format
#    def backup_bz2(directory, ftp):
#        name = strftime(pattern, gmtime())
#        archive = tarfile.open(name + ".tar.bz2", "w:bz2")
#        archive.add("%s" % (directory))
#        archive.close()
#        archname = name + ".tar.bz2"
#        dirs = directory
#    
#    # The function that makes backups in tar.gz format
#    def backup_gz(directory, ftp):
#        print(sb.color(_('<blue>I: Backing-up with tar.gz format...</blue>')))
#        name = strftime(pattern, gmtime())
#        archive = tarfile.open(name + ".tar.gz", "w:gz")
#        archive.add("%s" % (directory))
#        archive.close()
#        archname = name + ".tar.gz"
#        dirs = directory
#        print(ulib.color(_('<green>I: Done! You can find your backup in the current working dir as</green> <cyan>%s.tar.gz</cyan><green>!</green>') % (name)))
#    
#    # The function that makes backups in zip format
#    def backup_zip(directory, ftp):
#        print(sb.color(_('<blue>I: Backing-up with zip format...</blue>')))
#        name = strftime(pattern, gmtime())
#        archive = zipfile.ZipFile(name + ".zip", "w")
#        archive.write("%s" % (directory))
#        archive.close()
#        archname = name + ".tzip"
#        dirs = directory
#        print(ulib.color(_('<green>I: Done! You can find your backup in the current working dir as</green> <cyan>%s.zip</cyan><green>!</green>') % (name)))

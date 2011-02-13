#!/usr/bin/python
# -*- coding=utf-8 -*-
# Semplice Backup 0.1
# Formerly known as µBackup 5.

import os, sys, gtk, pygtk, libcompress, libftp

class sbGui:

	mform = gtk.Builder()

	def __init__( self ):
		# Initialize the main window
		self.builder = gtk.Builder()
		self.builder.add_from_file("gtk.glade")
		self.window = self.builder.get_object("semplice_bkt")
		
		if self.window:
			self.window.connect("destroy", gtk.main_quit)
		
		# Get all objects in the interface
		
		# Main window
		self.pages = self.builder.get_object("pages")
		self.about = self.builder.get_object("aboutbox")
		self.fc_restore = self.builder.get_object("fc_restore")
		self.addfiledlg = self.builder.get_object("fc_backup")
		# Add file window
		self.fc_backup_add = self.builder.get_object("fc_backup_add")
		# Restore backup window
		self.fcr_cancelbtn = self.builder.get_object("fc_restore_cancel")
		self.fcr_openbtn = self.builder.get_object("fc_restore_choose")
		# Page 1
		self.startbk_btn = self.builder.get_object("newbk_btn")
		self.restorebk_btn = self.builder.get_object("restorebk_btn")
		# Menubar
		self.abtboxbtn = self.builder.get_object("about_menubtn")
		self.quitbtn = self.builder.get_object("quit_menubtn")
		# Pages 2, 3, 4, 5 buttons
		self.bknext_btn = self.builder.get_object("bknext_bkbtn")
		self.bknext2_btn = self.builder.get_object("bknext2_bkbtn")
		self.bknext3_btn = self.builder.get_object("bknext3_bkbtn")
		self.bkback_btn = self.builder.get_object("bkback_bkbtn")
		self.bkback2_btn = self.builder.get_object("bkback2_bkbtn")
		self.bkback3_btn = self.builder.get_object("bkback3_bkbtn")
		self.bkback4_btn = self.builder.get_object("bkback4_bkbtn")
		# Page 2
		self.addfile_btn = self.builder.get_object("addfile_bkbtn")
		self.rmfile_btn = self.builder.get_object("remove_bkbtn")
		self.treefiles = self.builder.get_object("treeview1")
		# Page 3
		self.bz2arch = self.builder.get_object("rb_bz2")
		self.gzarch = self.builder.get_object("rb_gz")
		self.ziparch = self.builder.get_object("rb_zip")
		self.sbiarch = self.builder.get_object("rb_sbi")
		# Page 4
		self.rb_localdir = self.builder.get_object("rb_localdir")
		self.rb_ftpdir = self.builder.get_object("rb_ftpdir")
		self.fc_localdir = self.builder.get_object("fc_localdir")
		self.label8 = self.builder.get_object('label8')
		self.label9 = self.builder.get_object('label9')
		self.label10 = self.builder.get_object('label10')
		self.label11 = self.builder.get_object('label11')
		self.label12 = self.builder.get_object('label12')
		self.ftpsrv_entry = self.builder.get_object("ftpsrv_entry")
		self.ftport_entry = self.builder.get_object("ftport_entry")
		self.ftpdir_entry = self.builder.get_object("ftpdir_entry")
		self.ftpuser_entry = self.builder.get_object("ftpuser_entry")
		self.ftpass_entry = self.builder.get_object("ftpass_entry")
		# Page 5
		self.lb_status = self.builder.get_object("lb_status")
		self.backuprogress = self.builder.get_object("progressbar1")
		self.bkstart_btn = self.builder.get_object("bkstart_bkbtn")

		# Connect all the buttons with their events
		
		# Menu bar
		self.abtboxbtn.connect("activate", self.aboutbox)
		self.quitbtn.connect("activate", self.quit)
		# Add file dialog
		self.fc_backup_add.connect("clicked", self.addtobklist)
		# Restore dialog
		self.fcr_openbtn.connect("clicked", self.restore_bk)
		# Home page
		self.startbk_btn.connect("clicked", self.page_next)
		self.restorebk_btn.connect("clicked", self.restorebox)
		# Pages 2, 3, 4 - Next
		self.bknext_btn.connect("clicked", self.page_next)
		self.bknext2_btn.connect("clicked", self.page_next)
		self.bknext3_btn.connect("clicked", self.page_next)
		# Pages 2, 3, 4, 5 - Back
		self.bkback_btn.connect("clicked", self.page_prev)
		self.bkback2_btn.connect("clicked", self.page_prev)
		self.bkback3_btn.connect("clicked", self.page_prev)
		self.bkback4_btn.connect("clicked", self.page_prev)
		# Page 2
		self.cell = gtk.CellRendererText()
		self.file_col = gtk.TreeViewColumn("File name", self.cell, text=0)
		self.treefiles.append_column(self.file_col)
		self.addfile_btn.connect("clicked", self.add_file)
		self.rmfile_btn.connect("clicked", self.rmfrombklist)
		cell = gtk.CellRendererText()
		self.f_list = gtk.ListStore(str)
		self.treefiles.set_model(self.f_list)
		# Page 5 - Start backup!
		self.bkstart_btn.connect("clicked", self.start_bk)
		
		self.rb_localdir.connect("toggled", self.rbk_activate)
		self.rb_ftpdir.connect("toggled", self.rbk_activate)
		self.rbk_activate('self')

		dic = { 
			"on_semplice_bkt_destroy" : self.quit,
		}

		self.builder.connect_signals(dic)

	def aboutbox(self, obj):
		self.about.show()
		result = self.about.run()
		self.about.hide()
		
	def restorebox(self, obj):
		self.fc_restore.show()
		result = self.fc_restore.run()
		self.fc_restore.hide()

	def add_file(self, obj):
		self.addfiledlg.show()
		result = self.addfiledlg.run()
		self.addfiledlg.hide()

	def addtobklist(self, obj):
		self.f_list.append(self.addfiledlg.get_filenames())
		
	def rmfrombklist(self, obj):
		list_selection = self.treefiles.get_selection()
		model, list_selected = list_selection.get_selected()
		if list_selected is not None:
			self.f_list.remove(list_selected)

	def page_one(self, obj):
		if obj == self.bkstart_btn:
			self.lb_status.set_label("Ready.")
			self.bkstart_btn.set_label("Start!")
			self.bkstart_btn.connect("clicked", self.start_bk)
			self.backuprogress.set_fraction(0)
			print(obj)
		self.pages.set_current_page(0)

	def page_next(self, obj):
		""" This function will change the current notebook page. """
		if obj == self.bknext2_btn:
			if self.bz2arch.get_active() == True:
				self.archtype = ".tar.bz2"
				print("I: .tar.bz2 archive chosen")
			elif self.gzarch.get_active() == True:
				self.archtype = ".tar.gz"
				print("I: .tar.gz archive chosen")
			elif self.ziparch.get_active() == True:
				self.archtype = ".zip"
				print("I: .zip archive chosen")
			elif self.sbiarch.get_active() == True:
				self.archtype = ".sbi"
				print("I: .sbi archive chosen")
		self.pages.next_page()
		
	def page_prev(self, obj):
		""" This function will change the current notebook page. """
		self.pages.prev_page()
		
	def rbk_activate(self, obj):
		if self.rb_localdir.get_active() == True:
			self.fc_localdir.set_sensitive(True)
			self.label8.set_sensitive(False)
			self.label9.set_sensitive(False)
			self.label10.set_sensitive(False)
			self.label11.set_sensitive(False)
			self.label12.set_sensitive(False)
			self.ftpsrv_entry.set_sensitive(False)
			self.ftport_entry.set_sensitive(False)
			self.ftpdir_entry.set_sensitive(False)
			self.ftpuser_entry.set_sensitive(False)
			self.ftpass_entry.set_sensitive(False)
		elif self.rb_ftpdir.get_active() == True:
			self.fc_localdir.set_sensitive(False)
			self.label8.set_sensitive(True)
			self.label9.set_sensitive(True)
			self.label10.set_sensitive(True)
			self.label11.set_sensitive(True)
			self.label12.set_sensitive(True)
			self.ftpsrv_entry.set_sensitive(True)
			self.ftport_entry.set_sensitive(True)
			self.ftpdir_entry.set_sensitive(True)
			self.ftpuser_entry.set_sensitive(True)
			self.ftpass_entry.set_sensitive(True)
	
	def start_bk(self, obj):
		self.bkback4_btn.set_sensitive(False)
		self.bkstart_btn.set_sensitive(False)
		self.archformat = self.archtype
		print("I: Starting backup...")
		print("You have chosen the following archive format: %s" % (self.archformat))
		if self.rb_localdir.get_active() == True:
			self.localdest = self.fc_localdir.get_uri()
			self.param, self.localdest = self.localdest.split("file://",1)
			print("You have chosen to save the backup in the following local dir: %s" % (self.localdest))
		elif self.rb_ftpdir.get_active() == True:
			self.ftpsrv = self.ftpsrv_entry.get_text()
			if self.ftport_entry.get_text() != "":
				self.ftport = self.ftport_entry.get_text()
			else:
				self.ftport = "80"
			self.ftpdir = self.ftpdir_entry.get_text()
			self.ftpuser = self.ftpuser_entry.get_text()
			self.ftpass = self.ftpass_entry.get_text()
			bk_ftp = libftp.libftp()
			bk_ftp.upload(self.bk_arch_name, self.host, self.port, self.user, self.directory)
			self.localdest = "ftp://%s@%s:%s/%s" % (self.ftpuser, self.ftpsrv, self.ftport, self.ftpdir)
			print("Localdest: %s" % (self.localdest))
		print(self.treefiles.get_columns())
		self.bkstart_btn.set_label("Finish!")
		self.lb_status.set_label("Finished! Backup saved in: %s" % (self.localdest))
		self.backuprogress.set_fraction(1.00)
		self.bkstart_btn.set_sensitive(True)
		self.bkstart_btn.connect("clicked", self.quit)
			
	def restore_bk(self, obj):
		self.restorefile = self.fc_restore.get_uri()
		self.param, self.restorefile = self.restorefile.split("file://",1)
		print("You have chosen to restore this archive: %s" % (self.restorefile))
		self.pages.set_current_page(5)
			
	def quit(self, obj):
		sys.exit(0)
        
sbGui = sbGui()
sbGui.window.show()
gtk.main()

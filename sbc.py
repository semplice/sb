#!/usr/bin/python
# -*- coding=utf-8 -*-
# Semplice Backup 0.1
# Formerly known as µBackup 5.

import os, sys, locale, gettext, libcompress, libftp

# These lines are needed to translate automatically this application
# into supported languages
#gettext.bindtextdomain('sb', 'po/')
#gettext.textdomain('sb')
#_ = gettext.gettext

class sbcli:
    def color(self, string):
        colors = {"default":0, "black":30, "red":31, "green":32, "yellow":33,
              "blue":34,"magenta":35, "cyan":36, "white":37, "black":38,
              "black":39} #33[%colors%m
        for color in colors:
            color_string = "\033[%dm\033[1m" % colors[color]
            string = string.replace("<%s>" % color, color_string).replace("</%s>" % color, "\033[0m")
        return string
    
    def __init__(self):
        # Help text
        self.help = """Semplice Backup 0.1
Usage: sbc <option> <directory>

Options:

    -b, --bz2             Makes an archive in tar.bz2 format.
    -g, --gz              Makes an archive in tar.gz format.
    -h, --help            Shows this help.
    -z, --zip             Makes an archive in zip format.

Just add 'f' before the archive format you want to upload the archive on the FTP server you need to backup to.
e.g.: sbc -fg /path/to/file
      sbc --fgz /path/to/file"""
    
        # Checks that the user has passed an argument
        if len(sys.argv) < 1:
            print(self.help)
            sys.exit(1)
    
        # This code analyzes the arguments given by user and executes the chosen action
        # of, if there's something wrong, shows an error to the user.
        if "--help" in sys.argv or "-h" in sys.argv:
            print(self.help)
        elif "--bz2" in sys.argv or "-b" in sys.argv:
            self.backup(sys.argv[1])
        elif "--gz" in sys.argv or "-g" in sys.argv:
            self.backup(sys.argv[1])
        elif "--zip" in sys.argv or "-z" in sys.argv:
            self.backup(sys.argv[1])
        elif "--fbz2" in sys.argv or "-fb" in sys.argv:
            self.ftp_backup(sys.argv[1])
        elif "--fgz" in sys.argv or "-fg" in sys.argv:
            self.ftp_backup(sys.argv[1])
        elif "--fzip" in sys.argv or "-fz" in sys.argv:
            self.ftp_backup(sys.argv[1])
        else:
            unrec_arg = sys.argv[1]
            print("sbc: unrecognized option '%s'" % (unrec_arg))
            print("Try `sbc --help' for more information.")
            sys.exit(1)
            
    def backup(self, bk_format):
        if bk_format == "--bz2":
            self.bk_file = sys.argv[sys.argv.index("--bz2")+1]
            if sys.argv[sys.argv.index("--bz2")+2] != '':
                self.dest_dir = sys.argv[sys.argv.index("--bz2")+2]
            else:
                self.dest_dir = os.getcwd()
            bk_archtype = 'bz2'
        elif bk_format == "-b":
            self.bk_file = sys.argv[sys.argv.index("-b")+1]
            if sys.argv[sys.argv.index("-b")+2] != '':
                self.dest_dir = sys.argv[sys.argv.index("-b")+2]
            else:
                self.dest_dir = os.getcwd()
            bk_archtype = 'bz2'
        elif bk_format == "--gz":
            self.bk_file = sys.argv[sys.argv.index("--gz")+1]
            if sys.argv[sys.argv.index("--gz")+2] != '':
                self.dest_dir = sys.argv[sys.argv.index("--gz")+2]
            else:
                self.dest_dir = os.getcwd()
            bk_archtype = 'gz'
        elif bk_format == "-g":
            self.bk_file = sys.argv[sys.argv.index("-g")+1]
            if sys.argv[sys.argv.index("-g")+2] != '':
                self.dest_dir = sys.argv[sys.argv.index("-g")+2]
            else:
                self.dest_dir = os.getcwd()
            bk_archtype = 'gz'
        elif bk_format == "--zip":
            self.bk_file = sys.argv[sys.argv.index("--zip")+1]
            if sys.argv[sys.argv.index("--zip")+2] != '':
                self.dest_dir = sys.argv[sys.argv.index("--zip")+2]
            else:
                self.dest_dir = os.getcwd()
            bk_archtype = 'zip'
        elif bk_format == "-z":
            self.bk_file = sys.argv[sys.argv.index("-z")+1]
            if sys.argv[sys.argv.index("--bz2")+2] != '':
                self.dest_dir = sys.argv[sys.argv.index("-z")+2]
            else:
                self.dest_dir = os.getcwd()
            bk_archtype = 'zip'
        print(self.color('<blue>I: Backing-up with %s format...</blue>' % (bk_archtype)))
        bk_create = libcompress.compress()
        bk_create.backup(self.bk_file, self.dest_dir, bk_archtype)
        print(self.color('<green>I: Done! You can find your backup in the current working dir as</green> <cyan>%s</cyan><green>!</green>' % (bk_create.archname)))
        
    def ftp_backup(self, bk_type):
        if self.bk_type == "--fbz2":
            self.bk_file = sys.argv[sys.argv.index("--fbz2")+1]
            self.bk_arch = 'bz2'
        elif self.bk_type == "-fb":
            self.bk_file = sys.argv[sys.argv.index("-fb")+1]
            self.bk_arch = 'bz2'
        elif self.bk_type == "--fgz":
            self.bk_file = sys.argv[sys.argv.index("--fgz")+1]
            self.bk_arch = 'gz'
        elif self.bk_type == "-fg":
            self.bk_file = sys.argv[sys.argv.index("-fg")+1]
            self.bk_arch = 'gz'
        elif self.bk_type == "--fzip":
            self.bk_file = sys.argv[sys.argv.index("--fzip")+1]
            self.bk_arch = 'zip'
        elif self.bk_type == "-fz":
            self.bk_file = sys.argv[sys.argv.index("-fz")+1]
            self.bk_arch = 'zip'
        self.dest_dir = '/tmp/'
        print(self.color('<blue>I: Backing-up with %s format...</blue>' % (self.bk_archtype)))
        self.bk_arch_name = self.dest_dir + libcompress.compress().archname
        compress.backup(self.bk_arch_name, self.dest_dir, self.bk_arch)
        print(self.color('<blue>I: Uploading %s on %s:$s as %s in %s...</blue>' % (libcompress.compress().archname, self.host, self.port, self.user, self.directory)))
        libftp.upload(self.bk_arch_name, self.host, self.port, self.user, self.directory)
        print(self.color('<green>I: Done! Uploaded your backup as</green> <cyan>%s</cyan> <green>on</green> <cyan>%s</cyan><green>!</green>' % (libcompress.compress().archname, self.host)))

sbcli()

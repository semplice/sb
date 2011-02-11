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
    def color(string):
        colors = {"default":0, "black":30, "red":31, "green":32, "yellow":33,
              "blue":34,"magenta":35, "cyan":36, "white":37, "black":38,
              "black":39} #33[%colors%m
        for color in colors:
            color_string = "\033[%dm\033[1m" % colors[color]
            string = string.replace("<%s>" % color, color_string).replace("</%s>" % color, "\033[0m")
        return string
    
    def __init__(self):
        # Help text
        help = """
        Semplice Backup 0.1
        Usage: sbc <option> <directory>
            
        Options:
    
            -b, --bz2             Makes an archive in tar.bz2 format.
            -g, --gz              Makes an archive in tar.gz format.
            -h, --help            Shows this help.
            -z, --zip             Makes an archive in zip format.
    
        Just add 'f' before the archive format you want to upload the archive on the FTP server you need to backup to.
        e.g.: sb -fg /path/to/file
              sb --fgz /path/to/file
        """
    
        # Checks that the user has passed an argument
        if len(sys.argv) < 1:
            print(help)
            sys.exit(1)
    
        # This code analyzes the arguments given by user and executes the chosen action
        # of, if there's something wrong, shows an error to the user.
        if "--help" in sys.argv or "-h" in sys.argv:
            print(help)
        elif "--bz2" in sys.argv or "-b" in sys.argv:
            if "--bz2" in sys.argv:
                bk_file = sys.argv[sys.argv.index("--bz2")+1]
                dest_dir = sys.argv[sys.argv.index("--bz2")+2]
            else:
                bk_file = sys.argv[sys.argv.index("-b")+1]
                dest_dir = sys.argv[sys.argv.index("-b")+2]
            print(color('<blue>I: Backing-up with tar.bz2 format...</blue>'))
            compress.backup_bz2(bk_file, dest_dir)
            print(color('<green>I: Done! You can find your backup in the current working dir as</green> <cyan>%s.tar.bz2</cyan><green>!</green>' % (name)))
        elif "--gz" in sys.argv or "-g" in sys.argv:
            if "--gz" in sys.argv:
                bk_file = sys.argv[sys.argv.index("--gz")+1]
                dest_dir = sys.argv[sys.argv.index("--gz")+2]
            else:
                bk_file = sys.argv[sys.argv.index("-g")+1]
                dest_dir = sys.argv[sys.argv.index("-g")+2]
            print(color('<blue>I: Backing-up with tar.bz2 format...</blue>'))
            compress.backup_gz(bk_file, dest_dir)
            print(color('<green>I: Done! You can find your backup in the current working dir as</green> <cyan>%s.tar.gz</cyan><green>!</green>' % (name)))
        elif "--zip" in sys.argv or "-z" in sys.argv:
            if "--zip" in sys.argv:
                bk_file = sys.argv[sys.argv.index("--zip")+1]
                dest_dir = sys.argv[sys.argv.index("--zip")+2]
            else:
                bk_file = sys.argv[sys.argv.index("-z")+1]
                dest_dir = sys.argv[sys.argv.index("-z")+2]
            print(color('<blue>I: Backing-up with tar.bz2 format...</blue>'))
            compress.backup_zip(bk_file, dest_dir)
            print(color('<green>I: Done! You can find your backup in the current working dir as</green> <cyan>%s.tar.zip</cyan><green>!</green>' % (name)))
        elif "--fbz2" in sys.argv or "-fb" in sys.argv:
            if "--fbz2" in sys.argv:
                bk_file = sys.argv[sys.argv.index("--fbz2")+1]
            else:
                bk_file = sys.argv[sys.argv.index("-fb")+1]
            dest_dir = 'ftp'
            print(sb.color(_('<blue>I: Backing-up with tar.bz2 format...</blue>')))
            compress.backup_bz2(bk_file, dest_dir)
            print(color('<blue>I: Uploading %s on %s:$s as %s in %s...</blue>' % (bkarchive, host, port, user, directory)))
            libftp.upload(bkarchive, host, port, user, directory)
            print(color('<green>I: Done! Uploaded your backup as</green> <cyan>%s</cyan> <green>on</green> <cyan>%s</cyan><green>!</green>' % (bkarchive, host)))
        elif "--fgz" in sys.argv or "-fg" in sys.argv:
            if "--fgz" in sys.argv:
                bk_file = sys.argv[sys.argv.index("--fgz")+1]
            else:
                bk_file = sys.argv[sys.argv.index("-fg")+1]
            dest_dir = 'ftp'
            compress.backup_gz(bk_file, dest_dir)
            print(color('<blue>I: Uploading %s on %s:$s as %s in %s...</blue>' % (bkarchive, host, port, user, directory)))
            libftp.upload(bkarchive, host, port, user, directory)
            print(color('<green>I: Done! Uploaded your backup as</green> <cyan>%s</cyan> <green>on</green> <cyan>%s</cyan><green>!</green>' % (bkarchive, host)))
        elif "--fzip" in sys.argv or "-fz" in sys.argv:
            if "--fzip" in sys.argv:
                bk_file = sys.argv[sys.argv.index("--fzip")+1]
                dest_dir = sys.argv[sys.argv.index("--fzip")+2]
            else:
                bk_file = sys.argv[sys.argv.index("-fz")+1]
                dest_dir = sys.argv[sys.argv.index("-fz")+2]
            dest_dir = 'ftp'
            compress.backup_zip(bk_file, dest_dir)
            print(color('<blue>I: Uploading %s on %s:$s as %s in %s...</blue>' % (bkarchive, host, port, user, directory)))
            libftp.upload(bkarchive, host, port, user, directory)
            print(color('<green>I: Done! Uploaded your backup as</green> <cyan>%s</cyan> <green>on</green> <cyan>%s</cyan><green>!</green>' % (bkarchive, host)))
        else:
            print(help)
            sys.exit(1)

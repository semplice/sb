# -*- coding=utf-8 -*-
# Semplice Backup 0.1
# Formerly known as µBackup 5.
# The following lines import necessary modules

import os, sys, ftplib
from time import strftime, gmtime

class ftplib:
    def upload(bkarchive, host, port, ftpdir, user, passw):
        ftp = ftplib.FTP(host,user,passw)
        ftp.cwd(ftpdir)
        archive = open(bkarchive,'rb')
        ftp.storbinary('STOR ' + bkarchive, archive)
        archive.close()
        ftp.quit()


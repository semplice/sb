# -*- coding=utf-8 -*-
# Semplice Backup 0.1
# Formerly known as µBackup 5.

# The following line is needed to import necessary modules
import os, sys, tarfile, zipfile, ulib, sqlite3

# Declares the database to be used
db_connect = sqlite3.connect('.data.db')
db = db_connect.cursor()

# Saves changes and closes database
def db_close():
    db_connect.commit()
    db.close()

# This is an useful function that allows to execute the SQL command you need
def db_command(arguments):
    db.execute(arguments)
    db_close()

# Used to insert settings in the database
def db_insert(arguments):
    db.execute('INSERT INTO %s' % (arguments))
    db_close()

# Checks that a table exists
def db_table_exist(arguments):
    db.execute('SELECT name FROM sqlite_master WHERE type = table AND name = "%s";' % (arguments))
    db_close()

# Selects a value
def db_select(arg1, arg2, arg3):
    db.execute('SELECT value FROM %s WHERE %s = "%s";' % (arg1, arg2, arg3))
    db_close()

# Deletes a table or value
def db_delete(arg1, arg2, arg3):
    db.execute('DELETE FROM %s WHERE %s = "%s";' % (arg1, arg2, arg3))
    db_close()

# setupdb() creates the configuration database filling it with default settings
def setupdb():
    db.execute('CREATE TABLE archives (year date(0), month date(0), day date(0), hour date(0), mins date(0), secs date(0), archive varchar2(0), dir varchar2(0), destdir varchar2(0));')
    db.execute('CREATE TABLE ftpbackups (year date(0), month date(0), day date(0), hour date(0), mins date(0), secs date(0), archive varchar2(0), dir varchar2(0), destdir varchar2(0));')
# These are future tables for future features ;)
#    db.execute('CREATE TABLE clean (year date(0), month date(0), day date(0), hour date(0), mins date(0), secs date(0), success char(1), archive varchar2(0), dir varchar2(0));')
    db_close()


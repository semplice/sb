# -*- coding=utf-8 -*-
# Semplice Backup DB Library
# Copyright © 2011 Semplice Team. All rights reserved.

# The following line is needed to import necessary modules
import os, sys, sqlite3

# Declares the database to be used
db_connect = sqlite3.connect('/tmp/.files.db')
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
    db.execute('CREATE TABLE backup (file varchar2(0), dir varchar2(0);')
    db_close()


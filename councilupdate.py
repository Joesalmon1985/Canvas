#!/usr/bin/env python
# vim: tabstop=4 softtabstop=4 shiftwidth=4 smarttab expandtab:

__author__      = "Joe Salmon"
__copyright__   = "Copyright (c) 2015, The Green Party UK"

import sqlite3
import importcsvfile
from sys import argv

# This program creates a new table within a specified database containing updated information from the electoral register, using a text file which gives the names of the files used by the electoral register.

# This def creates the required tables
def createcouncilupdatefiles (databaseused):
    print "creating required tables" 
    with sqlite3.connect( databaseused ) as conn:
        cursor = conn.cursor()
        tobedone = 'DROP TABLE if exists councilfullupdated;'
        cursor.execute( tobedone )
        conn.commit()
        tobedone = '''CREATE TABLE councilfullupdated(
  "pd" TEXT,
  "eno" TEXT,
  "firstname" TEXT,
  "surname" TEXT,
  "fulladdress" TEXT,
  "street" TEXT,
  "address_1" TEXT,
  "address_2" TEXT,
  "address_3" TEXT,
  "address_4" TEXT,
  "address_5" TEXT,
  "address_6" TEXT,
  "address_7" TEXT,
  "v12" TEXT,
  "v14" TEXT,
  "green" TEXT,
  "intent" TEXT,
  "surveyn" TEXT,
  "knocked" TEXT
  "other1" TEXT,
  "other2" TEXT,
  "remove"
);'''
        cursor.execute( tobedone )
        conn.commit()
         
        with sqlite3.connect( databaseused ) as conn:
            cursor = conn.cursor()
            tobedone = 'DROP TABLE if exists toremove;'
            cursor.execute( tobedone )
            tobedone = '''CREATE TABLE toremove(
  "pd" TEXT,
  "eno" TEXT,
  "firstname" TEXT,
  "surname" TEXT,
  "fulladdress" TEXT,
  "street" TEXT,
  "address_1" TEXT,
  "address_2" TEXT,
  "address_3" TEXT,
  "address_4" TEXT,
  "address_5" TEXT,
  "address_6" TEXT,
  "address_7" TEXT,
  "remove" text
);'''
            cursor.execute( tobedone )
            conn.commit()

            with sqlite3.connect( databaseused ) as conn:
                cursor = conn.cursor()
                tobedone = 'DROP TABLE if exists councilremovedupdated;'
                cursor.execute( tobedone )
                tobedone = '''CREATE TABLE councilremovedupdated(
  "pd" TEXT,
  "eno" TEXT,
  "firstname" TEXT,
  "surname" TEXT,
  "fulladdress" TEXT,
  "street" TEXT,
  "address_1" TEXT,
  "address_2" TEXT,
  "address_3" TEXT,
  "address_4" TEXT,
  "address_5" TEXT,
  "address_6" TEXT,
  "address_7" TEXT,
  "v12" TEXT,
  "v14" TEXT,
  "green" TEXT,
  "intent" TEXT,
  "surveyn" TEXT,
  "knocked" TEXT
  "other1" TEXT,
  "other2" TEXT,
  "remove")
'''
                cursor.execute( tobedone )
                conn.commit()
                
                with sqlite3.connect( databaseused ) as conn:
                    cursor = conn.cursor()
                    tobedone = 'DROP TABLE if exists councilupdated;'
                    cursor.execute( tobedone )
                    tobedone = '''CREATE TABLE councilupdated(  
  "pd" TEXT,
  "eno" TEXT,
  "firstname" TEXT,
  "surname" TEXT,
  "fulladdress" TEXT,
  "street" TEXT,
  "address_1" TEXT,
  "address_2" TEXT,
  "address_3" TEXT,
  "address_4" TEXT,
  "address_5" TEXT,
  "address_6" TEXT,
  "address_7" TEXT,
  "v12" TEXT,
  "v14" TEXT,
  "green" TEXT,
  "intent" TEXT,
  "surveyn" TEXT,
  "knocked" TEXT
  "other1" TEXT,
  "other2" TEXT,
  "remove");
'''
                    cursor.execute( tobedone )
                    conn.commit()
                    print "done!"

#this def doesn't work at the moment and gives an unhelpful error message of IOError: [Errno 2] No such file or directory: 'council02.csv \n'




def councilupdatetxtlist (textlist, databaseused, outtable):
    filelist = open(textlist, 'r')
    otherlist = open(textlist, 'r')
    for a in otherlist:
        line = filelist.readline( )
        print "file to open %r" % (line)
        print "importing council data %r" % (line)
        importcsvfile.importcsvfile (line,databaseused)

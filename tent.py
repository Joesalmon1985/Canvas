#!/usr/bin/env python
# vim: tabstop=4 softtabstop=4 shiftwidth=4 smarttab expandtab:

__author__      = "Joe Salmon"
__copyright__   = "Copyright 2015"

from sys import argv
import sqlite3
import csv
import re

def importcsvfile (csvfile,db):    #import a csv file called 'csvfile' into an SQlite database called db.
    filereader = csv.reader( open(csvfile, 'rt'), delimiter=',') #rt means read text, delimiter tells it we'll use commas.

    # count of lines read, we will stop at 10
    c = 0

    # Note how many filled COLUMNs in the most filled-in ROW
    biggestHead = 0
    for fdsa in filereader:
        c = c+1
        if c > 9:
            break

        # Note how many filled COLUMNs in ROW c
        posHead = 0
        for column in fdsa:
            #print column
            if column == '':
                break
            else:
                posHead = posHead + 1
                lastrow = posHead
        if lastrow < biggestHead:
            biggestHead = biggestHead
        else:
            biggestHead = lastrow
            biggestrow = c
        
    print "you probably need the headings from row %r and these are %r columns" % (biggestrow, biggestHead)
        
    
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    filereader = csv.reader( open(csvfile, 'rt'), delimiter=',') #
    c=0
    for something in filereader:
        c=c+1
        if c == biggestrow:
            print "trying with row %r as headings" % (c) 
            cur.execute("drop table if exists %r;" % (csvfile))       
            cur.execute("create table %r(%r);" % (csvfile,something))      
    print "This will now create table %s, in database %s" % (csvfile,db)
    print "it's just a pain it's not bloody understood the comma"
        
            

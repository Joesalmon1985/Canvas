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
            if column == '':
                break
            else:
                posHead = posHead + 1

        # If the ROW is more filled in than the current best, then record it
        if posHead > biggestHead:
            biggestHead = posHead
            biggestrow = c

    print "You want the headings from row %r, and there are %r columns" % (biggestrow, biggestHead)

    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("drop table if exists %r;" % (csvfile))
    cur.execute("create table %r(data);" % (csvfile))
    print "This will now create table %s, in database %s" % (csvfile,db)


from sys import argv
import sqlite3
import csv
import re

def importcsvfile (csvfile,db):    #import a csv file called 'csvfile' into an SQlite database called db.
    filereader = csv.reader( open(csvfile, 'rt'), delimiter=',') #rt means read text, delimiter tells it we'll use commas.
    c = 0
    biggestHead = 0
    for fdsa in filereader:
        c = c+1
        if c > 9:
            break
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
        
    print "I've broken out"
    print "you need the headings from row %r and these are %r columns" % (biggestrow, biggestHead)
            
    
    
    
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("drop table if exists %r;" % (csvfile))       
    cur.execute("create table %r(data);" % (csvfile))      
    print "This will now create table %s, in database %s" % (csvfile,db)

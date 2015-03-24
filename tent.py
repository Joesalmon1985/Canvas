from sys import argv
import sqlite3
import csv
import re

def importcsvfile (csvfile):    #import a csv file called 'csvfile'
    filereader = csv.reader( open(csvfile, 'rt'), delimiter=',') #rt means read text, delimiter tells it we'll use commas.
    c = 0
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
        print c, posHead
    print "I've broken out"



#!/usr/bin/env python
# vim: tabstop=4 softtabstop=4 shiftwidth=4 smarttab expandtab:

__author__      = "Joe Salmon"
__copyright__   = "Copyright (c) 2015, The Green Party UK"

import sqlite3
import importcsvfile
from sys import argv

# This has a go at using specified csv files as existing uptodate council data, and another as the existing canvassing records, to create a
# new file which is up to date. If you want to change the existing data it uses, this must be done by changing the script. It will ask what
# you want the database file you are using to be called

print """This has a go at using specified csv files as existing uptodate council data, and another as the existing canvassing records, to create a new file which is up to date. If you want to change the existing data it uses, this must be done by changing the script. It will ask what you want the database file you are using to be called"""

print "what would you like your database to be called?"
databaseused = raw_input (">")


# List of the different files of council data to be used, change this list to change the data that is used
listcouncildata = [
        "council02.csv",
        "council03.csv",
        "council05.csv"
        ]

print listcouncildata

for fdsa in listcouncildata:
    print "importing council data %s" % (fdsa)
    importcsvfile.importcsvfile (fdsa,databaseused)

print "creating councilfullupdated file" 
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



for bit in listcouncildata:
    print "adding data to councilfull from %s" % (bit)
    with sqlite3.connect( databaseused ) as conn:
        cursor = conn.cursor()
        tobedone = '''insert into councilfullupdated (pd,eno,firstname,surname,fulladdress,address_1,address_2,address_3,address_4,address_5,address_6,address_7, remove) select pd,eno,firstname,surname,address1||address2||address3||address4||address5||address6||address7,address1,address2,address3,address4,address5,address6,address7, remove from %r where remove is not 'D';''' % (bit)
        cursor.execute( tobedone )
        conn.commit()


# creating table of people who need to be removed in the updates

print "creating table of people who need to be removed in the updates" 
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


# adding to the toremove table

print "adding to the toremove table"


for bit in listcouncildata:
    print "adding data to the toremovetable from %s" % (bit)
    tobedone = '''insert into toremove (pd, eno, firstname, surname, address_1, address_2, address_3, address_4, address_5, address_6, address_7) select pd, eno, firstname, surname, address1, address2, address3, address4, address5, address6, address7
from %r where remove is 'D';''' % (bit)
    cursor.execute( tobedone )
    conn.commit()

 
# setting remove column to remove
print "setting remove column to remove"

with sqlite3.connect( databaseused ) as conn:
    cursor = conn.cursor()
    tobedone = ''' UPDATE toremove SET remove = 'remove';'''
    cursor.execute( tobedone )
    conn.commit()

# creating table councilremovedupdated which now has the remove column populated with remove if someone should be removed

print "creating table councilremovedupdated which now has the remove column populated with remove if someone should be removed"
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
    tobedone = '''insert into councilremovedupdated (pd, eno, firstname, surname, fulladdress, street, address_1, address_2, address_3, address_4, address_5, address_6, address_7, remove) 
select 
councilfullupdated.pd, councilfullupdated.eno, councilfullupdated.firstname, councilfullupdated.surname, councilfullupdated.fulladdress, councilfullupdated.street, councilfullupdated.address_1, councilfullupdated.address_2, councilfullupdated.address_3, councilfullupdated.address_4, councilfullupdated.address_5, councilfullupdated.address_6, councilfullupdated.address_7, toremove.remove from councilfullupdated left outer join toremove on councilfullupdated.firstname = toremove.firstname and councilfullupdated.surname = toremove.surname and councilfullupdated.address_1 = toremove.address_1;'''
    cursor.execute( tobedone )
    conn.commit()

# Creating final table which only contains people who should not be removed from the data
print "Creating final table which only contains people who should not be removed from the data"
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

# added data
print "adding the final bit of data to councilupdated"

with sqlite3.connect( databaseused ) as conn:
    cursor = conn.cursor()
    tobedone = '''insert into councilupdated (pd, eno, firstname, surname, fulladdress, street, address_1, address_2, address_3, address_4, address_5, address_6, address_7) 
select pd, eno, firstname, surname, fulladdress, street, address_1, address_2, address_3, address_4, address_5, address_6, address_7 from councilremovedupdated where remove is not 'remove';'''
    cursor.execute( tobedone )
    conn.commit()

# removing duplicate information from council updated
print "removing duplicate information from council updated"

with sqlite3.connect( databaseused ) as conn:
    cursor = conn.cursor()
    tobedone = '''delete from councilupdated where rowid not in 
(select min(rowid) from councilupdated group by firstname, surname, address_1);'''
    cursor.execute( tobedone )
    conn.commit()

# At this point in the old SQL script, the street name field would now be added in. This feature is a little redundant now 
# as we need to work off postcodes, and something to be fixed

print "At this point in the old SQL script, the street name field would now be added in. This feature is a little redundant now as we need to work off postcodes, and something to be fixed"

# We now have a table within the database called councilupdated, which is the current electoral register with all updates taken into account
print "We now have a table within the database called councilupdated, which is the current electoral register with all updates taken into account"

    
    

#!/usr/bin/env python
# vim: tabstop=4 softtabstop=4 shiftwidth=4 smarttab expandtab:

import unittest
import glob
import re
import sqlite3
import importcsvfile
import inspect

class FreshData:

    # This def creates the required tables
    def createfreshfiles (self, databaseused):
        #print "creating required tables"
        self.createfreshdatanomembers (databaseused)
        self.createfreshdatamembers (databaseused)
        self.createmembersdata (databaseused)
        self.createfreshdatanohalls (databaseused)
        self.createfreshdatanohallsnoflat (databaseused)
        self.createcouncildata (databaseused)
        self.createolddata (databaseused)
        self.createstudent1 (databaseused)
        self.createstudent2 (databaseused)
        self.createstudent3 (databaseused)

    def uppercasememberpostcode (self, databaseused):
        print "nothing done yet"

    def updateyearmoved (self, databaseused):
        print "nothing done yet"

    def insertintofreshdatanomembers (self, databaseused):
        print "nothing done yet"

    def importmemberdatacsv (self, databaseused, membercsv):
        print inspect.stack()[0][3], "( ", databaseused, ", ", membercsv, " ): "
        importcsvfile.importcsvfile (membercsv, databaseused)
        if not databaseused.endswith( ".db" ):
            print inspect.stack()[0][3], "( ): Expected a DB file, got ", databaseused
            # throw?
            return
        with sqlite3.connect( databaseused ) as conn:
            cursor = conn.cursor()
            tobedone = """INSERT INTO membersdata SELECT * from '%s';""" % (membercsv)
            cursor.execute( tobedone )
            conn.commit()

    def importcouncildatacsv (self, databaseused, councilcsv):
        importcsvfile.importcsvfile (councilcsv, databaseused)
        with sqlite3.connect( databaseused ) as conn:
            cursor = conn.cursor()
            tobedone = """INSERT INTO councildata SELECT * from '%s';""" % (councilcsv)
            cursor.execute( tobedone )
            conn.commit()

    def importcouncildatasql (self, databaseused):
        print "nothing done yet"

    def importolddatacsv (self, databaseused, oldcsv):
        importcsvfile.importcsvfile (oldcsv, databaseused)
        with sqlite3.connect( databaseused ) as conn:
            cursor = conn.cursor()
            tobedone = """INSERT INTO olddata SELECT * from '%s';""" % (oldcsv)
            cursor.execute( tobedone )
            conn.commit()

    def importolddatasql (self, databaseused):
        print "nothing done yet"

    def insertintofreshdatamembers (self, databaseused):
        print "nothing done yet"

    def createfreshdatanomembers (self, databaseused):
        with sqlite3.connect( databaseused ) as conn:
            cursor = conn.cursor()
            tobedone = 'DROP TABLE if exists freshdatanomembers;'
            cursor.execute( tobedone )
            conn.commit()
            tobedone = '''CREATE TABLE freshdatanomembers(
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
  "priorres" TEXT,
  "v12" TEXT,
  "v14" TEXT,
  "v15",
  "green" TEXT,
  "intent" TEXT,
  "surveyn" TEXT,
  "datemovedin" TEXT,
  "knocked" TEXT,
  "other1" TEXT,
  "other2" TEXT,
  "partymember" TEXT
);
      '''
            cursor.execute( tobedone )
            conn.commit()

    def createfreshdatamembers (self, databaseused):
        with sqlite3.connect( databaseused ) as conn:
            cursor = conn.cursor()
            tobedone = 'DROP TABLE if exists freshdatamembers;'
            cursor.execute( tobedone )
            conn.commit()
            tobedone = '''CREATE TABLE freshdatamembers(
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
  "priorres" TEXT,
  "v12" TEXT,
  "v14" TEXT,
  "green" TEXT,
  "intent" TEXT,
  "surveyn" TEXT,
  "datemovedin" TEXT,
  "knocked" TEXT,
  "other1" TEXT,
  "other2" TEXT,
  "partymember" TEXT
);
      '''
            cursor.execute( tobedone )
            conn.commit()

    def createfreshdatanohallsnoflat (self, databaseused):
        with sqlite3.connect( databaseused ) as conn:
            cursor = conn.cursor()
            tobedone = 'DROP TABLE if exists freshdatanohallsnoflat;'
            cursor.execute( tobedone )
            conn.commit()
            tobedone = '''CREATE TABLE freshdatanohallsnoflat(
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
  "priorres" TEXT,
  "v12" TEXT,
  "v14" TEXT,
  "green" TEXT,
  "intent" TEXT,
  "surveyn" TEXT,
  "datemovedin" TEXT,
  "knocked" TEXT,
  "other1" TEXT,
  "other2" TEXT,
  "partymember" TEXT
);
      '''
            cursor.execute( tobedone )
            conn.commit()

    def createmembersdata (self, databaseused):
        with sqlite3.connect( databaseused ) as conn:
            cursor = conn.cursor()
            tobedone = 'DROP TABLE if exists membersdata;'
            cursor.execute( tobedone )
            conn.commit()
            tobedone = '''CREATE TABLE membersdata(
  "Contact Name" TEXT,
  "Joint member name" TEXT,
  "Postal Greeting" TEXT,
  "Email Greeting" TEXT,
  "First Name" TEXT,
  "Last Name" TEXT,
  "Do not mail" TEXT,
  "Addressee" TEXT,
  "Contact ID" TEXT,
  "Membership Type" TEXT,
  "Start Date" TEXT,
  "End Date" TEXT,
  "Member Since" TEXT,
  "Source" TEXT,
  "Status" TEXT,
  "Street Address" TEXT,
  "Supplemental Address 1" TEXT,
  "Supplemental Address 2" TEXT,
  "City" TEXT,
  "Postal Code" TEXT,
  "Country" TEXT,
  "Email" TEXT,
  "Phone (primary)" TEXT,
  "Mobile" TEXT,
  "Ward" TEXT,
  "Local authority" TEXT,
  "Westminster parliament constituency" TEXT,
  "Local party" TEXT,
  "Regional party" TEXT,
  "Override local party" TEXT
);
      '''
            cursor.execute( tobedone )
            conn.commit()

    def createolddata (self, databaseused):
        with sqlite3.connect( databaseused ) as conn:
            cursor = conn.cursor()
            tobedone = 'DROP TABLE if exists olddata;'
            cursor.execute( tobedone )
            conn.commit()
            tobedone = '''CREATE TABLE olddata(
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
  "priorres" TEXT,
  "v12" TEXT,
  "v14" TEXT,
  "v15" TEXT,
  "green" TEXT,
  "intent" TEXT,
  "surveyn" TEXT,
  "datemovedin" TEXT,
  "knocked" TEXT,
  "other1" TEXT,
  "other2" TEXT,
  "partymember" TEXT
);
      '''
            cursor.execute( tobedone )
            conn.commit()

    def createstudent1 (self, databaseused):
        with sqlite3.connect( databaseused ) as conn:
            cursor = conn.cursor()
            tobedone = 'DROP TABLE if exists student1;'
            cursor.execute( tobedone )
            conn.commit()
            tobedone = '''CREATE TABLE student1(
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
  "priorres" TEXT,
  "v12" TEXT,
  "v14" TEXT,
  "green" TEXT,
  "intent" TEXT,
  "surveyn" TEXT,
  "datemovedin" TEXT,
  "knocked" TEXT,
  "other1" TEXT,
  "other2" TEXT,
  "partymember" TEXT
);
      '''
            cursor.execute( tobedone )
            conn.commit()

    def createstudent2 (self, databaseused):
        with sqlite3.connect( databaseused ) as conn:
            cursor = conn.cursor()
            tobedone = 'DROP TABLE if exists student2;'
            cursor.execute( tobedone )
            conn.commit()
            tobedone = '''CREATE TABLE student2(
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
  "priorres" TEXT,
  "v12" TEXT,
  "v14" TEXT,
  "green" TEXT,
  "intent" TEXT,
  "surveyn" TEXT,
  "datemovedin" TEXT,
  "knocked" TEXT,
  "other1" TEXT,
  "other2" TEXT,
  "partymember" TEXT
);
      '''
            cursor.execute( tobedone )
            conn.commit()

    def createstudent3 (self, databaseused):
        with sqlite3.connect( databaseused ) as conn:
            cursor = conn.cursor()
            tobedone = 'DROP TABLE if exists student3;'
            cursor.execute( tobedone )
            conn.commit()
            tobedone = '''CREATE TABLE student3(
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
  "priorres" TEXT,
  "v12" TEXT,
  "v14" TEXT,
  "green" TEXT,
  "intent" TEXT,
  "surveyn" TEXT,
  "datemovedin" TEXT,
  "knocked" TEXT,
  "other1" TEXT,
  "other2" TEXT,
  "partymember" TEXT
);
      '''
            cursor.execute( tobedone )
            conn.commit()

    def createcouncildata (self, databaseused):
        with sqlite3.connect( databaseused ) as conn:
            cursor = conn.cursor()
            tobedone = 'DROP TABLE if exists councildata;'
            cursor.execute( tobedone )
            conn.commit()
            tobedone = '''CREATE TABLE councildata(
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
  "priorres" TEXT,
  "v12" TEXT,
  "v14" TEXT,
  "green" TEXT,
  "intent" TEXT,
  "surveyn" TEXT,
  "datemovedin" TEXT,
  "knocked" TEXT,
  "other1" TEXT,
  "other2" TEXT,
  "partymember" TEXT
);
      '''
            cursor.execute( tobedone )
            conn.commit()
    def createfreshdatanohalls (self, databaseused):
        with sqlite3.connect( databaseused ) as conn:
            cursor = conn.cursor()
            tobedone = 'DROP TABLE if exists freshdatanohalls;'
            cursor.execute( tobedone )
            conn.commit()
            tobedone = '''CREATE TABLE freshdatanohalls(
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
  "priorres" TEXT,
  "v12" TEXT,
  "v14" TEXT,
  "green" TEXT,
  "intent" TEXT,
  "surveyn" TEXT,
  "datemovedin" TEXT,
  "knocked" TEXT,
  "other1" TEXT,
  "other2" TEXT,
  "partymember" TEXT
);
      '''
            cursor.execute( tobedone )
            conn.commit()

    def createfreshdata ( thing ):
        print thing
        print "nothing here yet"

    def olddataextracol (self, databaseused):
        with sqlite3.connect( databaseused ) as conn:
            cursor = conn.cursor()
            tobedone = '''ALTER TABLE olddata add column v12;'''
            cursor.execute( tobedone )
            conn.commit()

    def priorresupdate1 (self, databaseused):
        with sqlite3.connect( databaseused ) as conn:
            cursor = conn.cursor()
            tobedone = """UPDATE olddata SET priorres = 'yes';"""
            cursor.execute( tobedone )
            tobedone = """UPDATE olddata SET datemovedin = '2015' where datemovedin is NULL;"""
            cursor.execute( tobedone )
            conn.commit()

    def insertdatafreshdatanomembers (self, databaseused):
        #print "this is it"
        with sqlite3.connect( databaseused ) as conn:
            cursor = conn.cursor()
            tobedone = """insert into freshdatanomembers ('pd','eno','firstname','surname','fulladdress','street','address_1','address_2','address_3','address_4','address_5','address_6','address_7','v12','v14','green','intent','surveyn','knocked','other1','other2','datemovedin','priorres')
select councildata.pd, councildata.eno, councildata.firstname, councildata.surname, councildata.fulladdress, councildata.street, councildata.address_1, councildata.address_2,councildata.address_3,councildata.address_4,councildata.address_5,councildata.address_6,councildata.address_7,
olddata.v12, olddata.v14, olddata.green, olddata.intent, olddata.surveyn, olddata.knocked, olddata.other1, olddata.other2, olddata.datemovedin, olddata.priorres
from councildata
left outer join olddata on councildata.firstname = olddata.firstname and councildata.surname = olddata.surname and councildata.address_1 = olddata.address_1;"""
            cursor.execute( tobedone )
            conn.commit()

    def priorresupdate2 (self, databaseused):
        with sqlite3.connect( databaseused ) as conn:
            cursor = conn.cursor()
            tobedone = """UPDATE freshdatanomembers SET datemovedin = '2015' where priorres IS NOT 'yes';"""
            cursor.execute( tobedone )
            conn.commit()
            tobedone = """UPDATE freshdatanomembers SET priorres = 'no' where datemovedin is '2015';"""
            cursor.execute( tobedone )
            conn.commit()

    def removeduplicates (self, databaseused):
        with sqlite3.connect( databaseused ) as conn:
            cursor = conn.cursor()
            tobedone = """delete from freshdata1 where rowid not in (select min(rowid) from freshdata1 group by firstname, surname, address_1);"""
            cursor.execute( tobedone )
            conn.commit()

    def makemembersdatawork (self, databaseused):
        with sqlite3.connect( databaseused ) as conn:
            cursor = conn.cursor()
            tobedone = """ALTER TABLE membersdata add column partymember;"""
            cursor.execute( tobedone )
            tobedone = """ALTER TABLE membersdata add column street;"""
            cursor.execute( tobedone )
            tobedone = """UPDATE membersdata SET partymember = 'yes';"""
            cursor.execute ( tobedone )
            tobedone = """UPDATE membersdata SET postcode = UPPER( postcode )"""
            cursor.execute ( tobedone )
            conn.commit()

    def insertintofreshdatamembers (self, databaseused):
        print "well this won't work yet"

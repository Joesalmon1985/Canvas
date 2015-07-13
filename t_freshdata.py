#!/usr/bin/env python
# vim: tabstop=4 softtabstop=4 shiftwidth=4 smarttab expandtab:

import unittest
import glob
import re
import sqlite3
from freshdata import FreshData

# A thing that wrote the csv files from this script would maybe be better.
naDataBase = 'testtoday.db'
naOldDatacsv = 'testmeold.csv'
naCouncilDatacsv = 'testcouncildata.csv'
naMemberDatacsv = 'testmemberdata.csv'

class T( unittest.TestCase ):

 # Tests the def that runs all the file creation defs. I can't think of a way to test this beyond just trying to run the def, or all of the tests that have been run already.
    def test_createfreshfiles (self):
        fd = FreshData ( )
        fd.createfreshfiles ( naDataBase )
        with sqlite3.connect( naDataBase ) as conn:
            cursor = conn.cursor()
            torun = """select count (*) from freshdatanomembers"""
            cursor.execute ( torun )
            r = cursor.fetchone ( )
            foundfreshdatanomembers = r [0]
        #print foundfreshdatanomembers
        self.assertEqual(0, foundfreshdatanomembers, 'A table was not created')

# tests the def that creates the table containing all the council & past canvassing data, without members shown.
    def test_createfreshdatanomembers (self):
        fd = FreshData ( )
        fd.createfreshdatanomembers ( naDataBase )
        with sqlite3.connect( naDataBase ) as conn:
            cursor = conn.cursor()
            torun = """select count (*) from freshdatanomembers"""
            cursor.execute ( torun )
            r = cursor.fetchone ( )
        foundfreshdatanomembers = r [0]
        #print foundfreshdatanomembers
        self.assertEqual(0, foundfreshdatanomembers, 'The table was created')

# tests the def that creates the table containing all the council & past canvassing data, with members shown.
    def test_createfreshdatamembers (self):
        fd = FreshData ( )
        fd.createfreshdatamembers ( naDataBase )
        with sqlite3.connect( naDataBase ) as conn:
            cursor = conn.cursor()
            torun = """select count (*) from freshdatamembers"""
            cursor.execute ( torun )
            r = cursor.fetchone ( )
        foundfreshdatamembers = r [0]
        #print foundfreshdatamembers
        self.assertEqual(0, foundfreshdatamembers, 'The table was created')

# tests the def that creates the table containing all the council & past canvassing data, with members shown, and no halls of residence
    def test_createfreshdatanohalls (self):
        fd = FreshData ( )
        fd.createfreshdatanohalls ( naDataBase )
        with sqlite3.connect( naDataBase ) as conn:
            cursor = conn.cursor()
            torun = """select count (*) from freshdatanohalls"""
            cursor.execute ( torun )
            r = cursor.fetchone ( )
        foundfreshdatanohalls = r [0]
        #print foundfreshdatanohalls
        self.assertEqual(0, foundfreshdatanohalls, 'The table was created')

# tests the def that creates the table containing all the council & past canvassing data, with members shown, and no halls of residence or flats
    def test_createfreshdatanohallsnoflat (self):
        fd = FreshData ( )
        fd.createfreshdatanohallsnoflat ( naDataBase )
        with sqlite3.connect( naDataBase ) as conn:
            cursor = conn.cursor()
            torun = """select count (*) from freshdatanohallsnoflat"""
            cursor.execute ( torun )
            r = cursor.fetchone ( )
        foundfreshdatanohallsnoflat = r [0]
        #print foundfreshdatanohallsnoflat
        self.assertEqual(0, foundfreshdatanohallsnoflat, 'The table was created')

# tests the def that creates the table containing all the members data
    def test_createmembersdata (self):
        fd = FreshData ( )
        fd.createmembersdata ( naDataBase )
        with sqlite3.connect( naDataBase ) as conn:
            cursor = conn.cursor()
            torun = """select count (*) from membersdata"""
            cursor.execute ( torun )
            r = cursor.fetchone ( )
        foundmembersdata = r [0]
        #print foundmembersdata
        self.assertEqual(0, foundmembersdata, 'The table was created')

# tests the def that creates the table containing council data
    def test_createcouncildata (self):
        fd = FreshData ( )
        fd.createcouncildata ( naDataBase )
        with sqlite3.connect( naDataBase ) as conn:
            cursor = conn.cursor()
            torun = """select count (*) from councildata"""
            cursor.execute ( torun )
            r = cursor.fetchone ( )
        foundcouncildata = r [0]
        #print foundcouncildata
        self.assertEqual(0, foundcouncildata, 'The table was created')

# tests the def that creates the table containing old canvassing data
    def test_createolddata (self):
        fd = FreshData ( )
        fd.createolddata ( naDataBase )
        with sqlite3.connect( naDataBase ) as conn:
            cursor = conn.cursor()
            torun = """select count (*) from olddata"""
            cursor.execute ( torun )
            r = cursor.fetchone ( )
        foundolddata = r [0]
        #print foundolddata
        self.assertEqual(0, foundolddata, 'The table was created')

# tests the def that creates the table used for student hall data removal
    def test_createstudent1 (self):
        fd = FreshData ( )
        fd.createstudent1 ( naDataBase )
        with sqlite3.connect( naDataBase ) as conn:
            cursor = conn.cursor()
            torun = """select count (*) from student1"""
            cursor.execute ( torun )
            r = cursor.fetchone ( )
        foundstudent1 = r [0]
        #print foundstudent1
        self.assertEqual(0, foundstudent1, 'The table was created')

# tests the def that creates the table used for student hall data removal
    def test_createstudent2 (self):
        fd = FreshData ( )
        fd.createstudent2 ( naDataBase )
        with sqlite3.connect( naDataBase ) as conn:
            cursor = conn.cursor()
            torun = """select count (*) from student2"""
            cursor.execute ( torun )
            r = cursor.fetchone ( )
        foundstudent2 = r [0]
        #print foundstudent2
        self.assertEqual(0, foundstudent2, 'The table was created')

# tests the def that creates the table used for student hall data removal
    def test_createstudent3 (self):
        fd = FreshData ( )
        fd.createstudent3 ( naDataBase )
        with sqlite3.connect( naDataBase ) as conn:
            cursor = conn.cursor()
            torun = """select count (*) from student3"""
            cursor.execute ( torun )
            r = cursor.fetchone ( )
        foundstudent3 = r [0]
        #print foundstudent3
        self.assertEqual(0, foundstudent3, 'The table was created')

            # tests the def that imports the past canvassing data from a csv file.
    def test_importolddatacsv (self):
        fd = FreshData ( )
        fd.importolddatacsv ( naDataBase, naOldDatacsv  )
        with sqlite3.connect( naDataBase ) as conn:
            cursor = conn.cursor()
            torun = '''select * from olddata'''
            cursor.execute( torun )
            r = cursor.fetchone ( )
        #print r
        check1 = r[0]
        check2 = r[1]
        check3 = r[2]
        check4 = r[10]
        check5 = r[11]
        print check1
        print check2
        print check3
        print check4
        print check5
        self.assertEqual('HEA', check1, 'The data has not been imported right'  )
        self.assertEqual('25', check2, 'The data has not been imported right'   )
        self.assertEqual('D', check3, 'The data has not been imported right'    )
        self.assertEqual('27 ASH CRESCENT', check4, 'The data has not been imported right'  )
        self.assertEqual('LEEDS', check5, 'The data has not been imported right'    )

# tests the def that imports the council data from a csv
    def test_importcouncildatacsv (self):
        fd = FreshData ( )
        fd.importcouncildatacsv ( naDataBase, naCouncilDatacsv  )
        with sqlite3.connect( naDataBase ) as conn:
            cursor = conn.cursor()
            torun = '''select * from councildata'''
            cursor.execute( torun )
            r = cursor.fetchone ( )
            print r
            check1 = r[0]
            check2 = r[1]
            check3 = r[2]
            check4 = r[10]
            check5 = r[11]
            print check1
            print check2
            print check3
            print check4
            print check5
        self.assertEqual('HEA', check1, 'The data has not been imported right'  )
        self.assertEqual('25', check2, 'The data has not been imported right'   )
        self.assertEqual('D', check3, 'The data has not been imported right'    )
        self.assertEqual('27 ASH CRESCENT', check4, 'The data has not been imported right'  )
        self.assertEqual('LEEDS', check5, 'The data has not been imported right'    )

# tests the def that imports the member data from a csv
    def test_importmemberdatacsv (self):
        fd = FreshData ( )
        fd.importmemberdatacsv ( naDataBase, naMemberDatacsv  )
        with sqlite3.connect( naDataBase ) as conn:
            cursor = conn.cursor()
            torun = '''select * from membersdata'''
            cursor.execute( torun )
            r = cursor.fetchone ( )
            print r
            check1 = r[0]
            check2 = r[3]
            check3 = r[2]
            check4 = r[10]
            check5 = r[11]
            print check1
            print check2
            print check3
            print check4
            print check5
        self.assertEqual('Billy Jones', check1, 'The data has not been imported right'  )
        self.assertEqual('Dear Billy', check2, 'The data has not been imported right'   )
        self.assertEqual('Dear Billy', check3, 'The data has not been imported right'   )
        self.assertEqual('2015-01-16', check4, 'The data has not been imported right'   )
        self.assertEqual('2016-01-15', check5, 'The data has not been imported right'   )

# tests the def that adds extra columns to the old data. Total mess.
#   def test_olddataextracol (self):
#           fd = FreshData ( )
#       fd.createfreshfiles ( naDataBase )
#       fd.olddataextracol (naDataBase)
#       with sqlite3.connect( naDataBase ) as conn:
#           cursor = conn.cursor()
#           torun = """INSERT INTO olddata (v12, v14, v15, green, intent, surveyn, knocked, other1, other2, datemovedin, priorres) VALUES ('Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata')"""
#           cursor.execute( torun )
#           conn.commit ( )
#           torun = """SELECT v12, v14, v15, green, intent, surveyn, knocked, other1, other2, datemovedin, priorres FROM olddata"""
#           cursor.execute (torun)
#           r = cursor.fetchone ( )
#           print r
#           check1 = r[0]
#       self.assertEqual('Somedata', check1, 'The data has not been imported right' )

# tests the def that updates the prior res info on old data

    def test_priorresupdate1 (self):
        fd = FreshData ( )
        fd.createfreshfiles ( naDataBase )
        with sqlite3.connect( naDataBase ) as conn:
            cursor = conn.cursor()
            torun = """INSERT INTO olddata (firstname, surname, address_1, address_2, v12, v14, v15, green, intent, surveyn, knocked, other1, other2, datemovedin, priorres) VALUES ('Roger', 'More', '34 Fun street', 'LS4 1EP', 'Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','2010','Somedata')"""
            torun = """INSERT INTO olddata (firstname, surname, address_1, address_2, v12, v14, v15, green, intent, surveyn, knocked, other1, other2)
VALUES ('Sandy', 'More', '34 Fun street', 'LS4 1EP', 'Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata')"""
            cursor.execute( torun )
            fd.priorresupdate1 ( naDataBase  )
        with sqlite3.connect( naDataBase ) as conn:
            cursor = conn.cursor()
            torun = '''select datemovedin, priorres from olddata'''
            cursor.execute( torun )
            r = cursor.fetchmany (2)
            count = 0
            for a in r:
                print a
                count = count + 1
                if count == 1:
                    print a[0]
                    print a[1]
                    check1 = a[0]
                if count == 2:
                    print a[0]
                    print a[1]
                    check2 = a[0]
        self.assertEqual('2010', check1, 'The originl date moved in has not been kept'  )
        self.assertEqual('2015', check2, 'a blank date has not been filled' )
        self.assertEqual('yes', check3, 'The prior res has not been set to yes' )

# tests the def that adds data to freshdatanomembers
    def test_insertdatafreshdatanomembers (self):
        fd = FreshData ( )
        fd.createfreshfiles ( naDataBase )
        with sqlite3.connect ( naDataBase ) as conn:
            cursor = conn.cursor()
            torun = """INSERT INTO olddata (firstname, surname, address_1, address_2, v12, v14, v15, green, intent, surveyn, knocked, other1, other2, datemovedin, priorres)
VALUES ('Steve', 'Funnyname', '34 Busy street', 'LS3 4EP', 'Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata')"""
            cursor.execute( torun )
            torun = """INSERT INTO olddata (firstname, surname, address_1, address_2, v12, v14, v15, green, intent, surveyn, knocked, other1, other2, datemovedin, priorres)
VALUES ('Roger', 'More', '34 Fun street', 'LS4 1EP', 'Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','yes')"""
            cursor.execute( torun )
            torun = """INSERT INTO councildata (firstname, surname, fulladdress, address_1, address_2, address_3, address_4, address_5, address_6, address_7)
VALUES ('Roger', 'More', '34 Fun street', 'LS4 1EP', 'Leeds','Again','Somedata','Somefdsa','fdsafd','rerer')"""
            cursor.execute( torun )
            torun = """INSERT INTO councildata (firstname, surname, fulladdress, address_1, address_2, address_3, address_4, address_5, address_6, address_7)
VALUES ('Daisy', 'Dares', '54 Fun street', 'LS1 14P', 'Leeds','Again','Somedata','Somefdsa','fdsafd','rerere')"""
            cursor.execute( torun )
            conn.commit ( )
        fd.insertdatafreshdatanomembers (naDataBase)
        torun = """SELECT firstname, priorres from freshdatanomembers;"""
        cursor.execute( torun )
        r = cursor.fetchone (  )
        check1 = r [0]
        check2 = r [1]
        print check1
        print check2
        self.assertEqual('Roger', check1, 'The data has not been imported right'    )
        self.assertEqual('yes', check2, 'The prior res status has been lost'    )

# tests the def that updates the prior res info on freshdatanomembers data
    def test_priorresupdate2 (self):
        fd = FreshData ( )
        fd.createfreshfiles ( naDataBase )
        with sqlite3.connect( naDataBase ) as conn:
            cursor = conn.cursor()
            torun = """INSERT INTO freshdatanomembers (firstname, surname, address_1, address_2, v12, v14, v15, green, intent, surveyn, knocked, other1, other2, datemovedin, priorres) VALUES ('Roger', 'More', '34 Fun street', 'LS4 1EP', 'Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','2011','yes')"""
            cursor.execute( torun)
            torun = """INSERT INTO freshdatanomembers (firstname, surname, address_1, address_2, v12, v14, v15, green, intent, surveyn, knocked, other1, other2) VALUES ('Sandy', 'More', '34 Fun street', 'LS4 1EP', 'Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata')"""
            cursor.execute( torun )
            fd.priorresupdate2 ( naDataBase  )
        with sqlite3.connect( naDataBase ) as conn:
            cursor = conn.cursor()
            torun = '''select datemovedin, priorres, firstname from freshdatanomembers'''
            cursor.execute( torun )
            r = cursor.fetchone ( )
            print r
            check1 = r[0]
            print check1
            check2 = r[1]
            print check2
        self.assertEqual('2011', check1, 'The data has not been imported right' )
        self.assertEqual('no', check2, 'The data has not been imported right'   )

    def test_makemembersdatawork (self):
        fd = FreshData ( )
        fd.createfreshfiles ( naDataBase )
        fd.importmemberdatacsv (naMemberDatacsv, naDataBase)
        fd.makemembersdatawork ( naDataBase )
        with sqlite3.connect ( naDataBase ) as conn:
            cursor = conn.cursor()
            tobedone = """SELECT street from membersdata;"""
            cursor.execute( torun )
            r = cursor.fetchone ( )
            print r
            check1 = r[0]
            tobedone = """SELECT partymember from membersdata;"""
            cursor.execute( torun )
            r = cursor.fetchone ( )
            print r
            check2 = r[0]
        self.assertEqual('none', check1, 'The street column is not added'   )
        self.assertEqual('yes', check2, 'The party member column is not added'  )

    def insertintofreshdatamembers (self):
        fd = FreshData ( )
        fd.createfreshfiles ( naDataBase )
        with sqlite3.connect ( naDataBase ) as conn:
            cursor = conn.cursor()
            tobedone = """SELECT street from membersdata;"""
            torun = """INSERT INTO freshdatanomembers (firstname, surname, address_1, address_2, v12, v14, v15, green, intent, surveyn, knocked, other1, other2, datemovedin, priorres)
VALUES ('Roger', 'More', '34 Fun street', 'LS4 1EP', 'Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','2011','yes')"""
            cursor.execute( torun)
            torun = """INSERT INTO freshdatanomembers (firstname, surname, address_1, address_2, v12, v14, v15, green, intent, surveyn, knocked, other1, other2)
VALUES ('Sandy', 'More', '34 Fun street', 'LS4 1EP', 'Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata','Somedata')"""
            cursor.execute( torun )
            torun = """INSERT INTO membersdata ('firstname', 'lasname', 'postcode', 'Email', 'Phone')
VALUES ('Sandy', 'More','LS4 1EP', 'sandy@internet','07446543978')"""
            cursor.execute( torun )
            conn.commit ( )
        fd.insertintofreshdatamembers ( naDatabase )
        tobedone = """SELECT * from freshdatamembers;"""
        cursor.execute( tobedone)
        self.assertEqual('none', check1, 'The street column is not added'   )
        self.assertEqual('yes', check2, 'The party member column is not added'  )

#       insert into freshdata2 (pd, eno, firstname, surname, fulladdress, street, address_1, address_2, address_3, address_4, address_5, address_6, address_7, priorres, v12, v14, green, intent, surveyn, knocked, other1, other2, yearmovedin, partymember)
# select freshdata1.pd, freshdata1.eno, freshdata1.firstname, freshdata1.surname, freshdata1.fulladdress, freshdata1.street, freshdata1.address_1, freshdata1.address_2, freshdata1.address_3, freshdata1.address_4, freshdata1.address_5, freshdata1.address_6, freshdata1.address_7, freshdata1.priorres, freshdata1.v12, freshdata1.v14, freshdata1.green, freshdata1.intent, freshdata1.surveyn, freshdata1.knocked, freshdata1.other1, freshdata1.other2, freshdata1.yearmovedin, streetmembers.partymember
# from freshdata1 left outer join streetmembers on freshdata1.firstname = streetmembers.FirstName and freshdata1.surname = streetmembers.Lastname and freshdata1.street = streetmembers.street;

#!/usr/bin/env python
# vim: tabstop=4 softtabstop=4 shiftwidth=4 smarttab expandtab:

import unittest
import glob
import re
import sqlite3
from freshdata import FreshData


# If the same database file is used, fails don't always show when testing the findcouncildata bit of the file
naDataBase = 'testmetoday.db'
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
			print foundfreshdatanomembers
			testran = 1
    		self.assertEqual(0, foundfreshdatanomembers, 'A table was not created')
    		self.assertEqual(1, testran, 'The test ran okay')

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
			print foundfreshdatanomembers
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
			print foundfreshdatamembers
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
			print foundfreshdatanohalls
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
			print foundfreshdatanohallsnoflat
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
			print foundmembersdata
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
			print foundcouncildata
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
			print foundolddata
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
			print foundstudent1
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
			print foundstudent2
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
			print foundstudent3
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
	  	self.assertEqual('HEA', check1, 'The data has not been imported right'	)
	  	self.assertEqual('25', check2, 'The data has not been imported right'	)
	  	self.assertEqual('D', check3, 'The data has not been imported right'	)
	  	self.assertEqual('27 ASH CRESCENT', check4, 'The data has not been imported right'	)
	  	self.assertEqual('LEEDS', check5, 'The data has not been imported right'	)

#!/usr/bin/env python
# vim: tabstop=4 softtabstop=4 shiftwidth=4 smarttab expandtab:

import unittest
import glob
import re
import sqlite3
import importcsvfile

class FreshData:

    # This def creates the required tables
	def createfreshfiles (self, databaseused):
	    	print "creating required tables"
		fd = FreshData ( )
	    	fd.createfreshdatanomembers (databaseused)


	def uppercasememberpostcode (self, databaseused):
		print "nothing done yet"
	    	
	    
	def updateyearmoved (self, databaseused):
		print "nothing done yet"
	    
	def insertintofreshdatanomembers (self, databaseused):
		print "nothing done yet"

	def importcouncildatacsv (self, databaseused):
		print "nothing done yet"

	def importcouncildatasql (self, databaseused):
		print "nothing done yet"

	def importolddatacsv (self, databaseused, oldcsv):
		csvused = str.rstrip (oldcsv)
		print "importing csv data"
		importcsvfile.importcsvfile (csvused, databaseused)
		print "imported csv data"
		print oldcsv
		print csvused
		
		with sqlite3.connect( databaseused ) as conn:
			cursor = conn.cursor()
			tobedone = """INSERT INTO olddata SELECT * from '%s';""" % (csvused)
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
  "green" TEXT,
  "intent" TEXT,
  "surveyn" TEXT,
  "yearmovedin" TEXT,
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
  "yearmovedin" TEXT,
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
  "yearmovedin" TEXT,
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
  "yearmovedin" TEXT,
  "knocked" TEXT,
  "other1" TEXT,
  "other2" TEXT,
  "partymember" TEXT
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
  "green" TEXT,
  "intent" TEXT,
  "surveyn" TEXT,
  "yearmovedin" TEXT,
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
  "yearmovedin" TEXT,
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
  "yearmovedin" TEXT,
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
  "yearmovedin" TEXT,
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
  "yearmovedin" TEXT,
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
  "yearmovedin" TEXT,
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

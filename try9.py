import importcsvfile
import sqlite3
import councilupdate

print """This script will try to merge existing canvassing data with up to date information from the electoral register. It will work in a db file called hope.db, it will work on the assumption that there are 3 files with the council data in."""

print "assuming text list is councildata.txt"
textlist = 'councildata.txt'
print "assuming db is called hope.db"
databaseused = 'hope.db'
print "assuming output table should be called updatedelectoralreg"
outtable = 'updatedelectoralreg'

councilupdate.councilupdatetxtlist (textlist, databaseused, outtable)

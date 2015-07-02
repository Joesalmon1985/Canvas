import importcsvfile
import sqlite3

print """This script will try to merge existing canvassing data with up to date information from the electoral register. It will work in a db file called hope.db What is the name of the csv file with your existing canvassing data?"""

# this opens a connection to a dbfile called hope.db
filenamedb = 'hope'
conn = sqlite3.connect(filenamedb)
cur = conn.cursor()

# this asks the user the name the csv file with the raw canvassing data
rawcandata = raw_input('>')

# ths imports the raw data from the csv file into the hope.db file
importcsvfile.importcsvfile (rawcandata,filenamedb)

print "added %r into hope.db" % (rawcandata)


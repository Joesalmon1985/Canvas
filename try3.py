#!/usr/bin/env python
# vim: tabstop=4 softtabstop=4 shiftwidth=4 smarttab expandtab:

__author__      = "Joe Salmon"
__copyright__   = "Copyright (c) 2015, The Green Party UK"

import sqlite3
import importcsvfile
from sys import argv

# This has a go at using a specified csv file as existing data, and another as the new updates to the register and make a new thingy

script, rawcandata, councildata = argv
filenamedb = 'positive'

print "adding raw canvassing data to database positive.db, table name is %s" % (rawcandata)

importcsvfile.importcsvfile (rawcandata,filenamedb)

print "adding up to date electoral register informoatnion to database positive.db, table name is %s" % (councildata)

importcsvfile.importcsvfile (councildata,filenamedb)

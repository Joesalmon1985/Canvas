#!/usr/bin/env python
# vim: tabstop=4 softtabstop=4 shiftwidth=4 smarttab expandtab:

"""try.py: Tests the tent module"""

__author__      = "Joe Salmon"
__copyright__   = "Copyright 2015, Planet Earth"

import tent
import sqlite3, csv
from sys import argv 

# this tells try to test using the file specified when running python, i.e. running python try.py councilfull.csv will
# mean that python tries to open councilfull.csv.
script, filename = argv

# This tells python to start using SQLITE3 with a database called whatever what typed after python joesqlite.py.
conn = sqlite3.connect( 'db' )

# This tells python to start typing in the running sqlite3 program.
cur = conn.cursor()

tent.importcsvfile( filename )

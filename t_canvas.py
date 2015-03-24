#!/usr/bin/env python
# vim: tabstop=4 softtabstop=4 shiftwidth=4 smarttab expandtab:

import unittest

from canvas import Canvas

naFile = 'work/councilfull.csv'
naTable = 'councilfull'

class T( unittest.TestCase ):

    def test_sqliteimport( self ):
        c = Canvas( )
        c.sqliteimport( naFile, naTable )

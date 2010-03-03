#!/usr/bin/env python
# -*- coding: utf-8 -*-
# copy orf files which corresponding jpg ones by Witek Firlej http://grizz.pl

__project__      = "copyorfs"
__author__    = "Witold Firlej (http://grizz.pl)"
__license__   = "GPL"
__copyright__ = "Witold Firlej"
__version__ = "0.35"

import glob,os
print os.path.realpath(os.curdir)
print os.curdir
for infile in glob.glob("*.[jJ][pP][gG]"):
	print "copying: "+infile[:-4]+".ORF" 			# [:-4] cutting extension
	os.system("cp ../"+infile[:-4]+".ORF .")
print "\nDone!\n"

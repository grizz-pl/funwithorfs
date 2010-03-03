#!/usr/bin/env python
# -*- coding: utf-8 -*-
# delete orf files without corresponding jpgs by Witek Firlej http://grizz.pl

__project__      = "deleteorfs"
__author__    = "Witold Firlej (http://grizz.pl)"
__license__   = "GPL"
__copyright__ = "Witold Firlej"
__version__ = "0.15"

import glob,os
print os.path.realpath(os.curdir)
print os.curdir
os.system("mkdir todelete") 						# being cerful is very important ;)
for infile in glob.glob("*.[oO][rR][fF]"):
	if not os.path.isfile(infile[:-4]+".[jJ][pP][gG]"):
		print "deleting: "+infile[:-4]+".ORF" 			# [:-4] cutting extension
		os.system("mv "+infile[:-4]+".ORF todelete/")
print "\nDone!\n"

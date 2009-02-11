#!/usr/bin/env python

import os, re, glob

CURDIR = os.path.abspath('.')
mask = '*.pyc'

c = 0
for f in glob.glob(os.path.join(CURDIR, mask)):
    if os.path.isfile(f):
	print 'Delete: %s' % f
	os.remove(f)
	c = c + 1
for root, dirs, files in os.walk(CURDIR):
    for dir in dirs:
	for f in glob.glob(os.path.join(dir, mask)):
	    if os.path.isfile(os.path.join(root, f)):
		print 'Delete: %s' % os.path.join(root, f)
	    	os.remove(f)
	        c = c + 1
print '\n%s %s files deleted.' % (c, mask)

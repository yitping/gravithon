#!/usr/bin/python

import argparse
from astropy.io import fits

parser = argparse.ArgumentParser(description='Print out HDU information of a GRAVITY FITS file.')
parser.add_argument('fitslist', metavar='fits', nargs=1,
		help='fits files to read')
args = parser.parse_args()

gf = fits.open(args.fitslist[0])
gf.info()
for t in gf[:]:
	if (t.is_image):
		continue
	print(t.name + ': ' + ', '.join(t.columns.names))

gf.close()


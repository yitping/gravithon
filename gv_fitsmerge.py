#!/usr/bin/python

# Merge FITS tables into one main file

import argparse
from astropy.io import fits

parser = argparse.ArgumentParser(description='Merge FITS tables into one main FITS file')
parser.add_argument('main', metavar='main', nargs=1,
        help='main fits file to be merged to')
parser.add_argument('exts', metavar='exts', nargs='*',
        help='extension name - fits file pair')
args = parser.parse_args()

#print(args.main)
#print(args.exts)

# TODO: check that the size of args.exts is even

print('reading ' + args.main[0] + '...')
mf = fits.open(args.main[0], mode='update')
sz = len(mf)
#print(sz)
for i in range(len(args.exts)/2):
    print('appending ' + args.exts[i*2+1] + ' as ' + args.exts[i*2].upper() + '...')
    ni = fits.open(args.exts[i*2+1])
    mf.append(ni[0])
    mf[sz+i].name = args.exts[i*2]

#print(len(mf))
mf.flush()
mf.close()


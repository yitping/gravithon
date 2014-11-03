# http://docs.astropy.org/en/stable/io/fits/api/tables.html#astropy.io.fits.FITS_rec.from_columns
# http://docs.astropy.org/en/stable/io/fits/index.html
# http://docs.scipy.org/doc/numpy/user/basics.rec.html
# http://docs.astropy.org/en/stable/io/fits/index.html#creating-a-new-table-file
# http://ssb.stsci.edu/doc/stsci_python_x/pyfits.docs/html/users_guide/users_table.html

#
# write_imaging_data.py
#
# PURPOSE
#    write a FITS binary table in the IMAGING_DETECTOR format
#       that describes the data in the IMAGING_DATA table


###### MISSING #####
## header keywords


#
# CAVEAT
#    this will produce a primary HDU + bintable extension; APPENDBIN option in 
#       boss will only take bintable and ignore (empty) primary HDU
#
# VERSION HISTORY
# 2014-10-09   written by Leonard Burtscher
#
import numpy as np
from astropy.io import fits
from datetime import datetime

phases=np.genfromtxt('data/phases.txt')
baseline_ids=np.genfromtxt('data/IO.txt')
baseline_def=np.genfromtxt('data/baseline_def.txt')
pol_split=np.genfromtxt('data/polarization_split.txt',dtype=str)
pol_combined=np.genfromtxt('data/polarization_combined.txt',dtype=str)

detid=3
nout=24
#
# instrument modes that require different IMAGING_DETECTOR tables:
#    - LOW/MEDIUM/HIGH spectral resolution
#    - with and without Wollaston
# 
modes=['l','lw']

for mode in modes:
	if mode=='lw' or mode=='mw' or mode=='hw':
		pol=pol_split
		m='split'
	else:
		pol=pol_combined
		m='combined'

	PX=np.genfromtxt('data/PX_'+mode+'.txt',delimiter=',')
	PY=np.genfromtxt('data/PY_'+mode+'.txt',delimiter=',')
	
	region=[]
	detector=[]
	ports=[]
	correlation=[]
	regname=[]
	center=[]
	
	for i in np.arange(nout):
		ibl_id=baseline_ids[i]-1
		if ibl_id < 0:
			ibl=-1
		else:
			ibl=baseline_def[ibl_id]

		if ibl==12:
			iport=[1,2]
		elif ibl==13:
			iport=[1,3]
		elif ibl==14:
			iport=[1,4]
		elif ibl==23:
			iport=[2,3]
		elif ibl==24:
			iport=[2,4]
		elif ibl==34:
			iport=[3,4]
		elif ibl==-1:
			iport=[0,0]
		else:
			quit()
		
		if m=='combined':
			ipol=pol_combined[i]
			icenter=[np.average(PX),np.average(PY[i,:])]
		else:
			ipol=pol_split[2*i]
			icenter=[np.average(PX),np.average(PY[2*i,:])]

		if phases[i]==0:
			iphase='A'
		elif phases[i]==90:
			iphase='B'
		elif phases[i]==180:
			iphase='C'
		elif phases[i]==270:
			iphase='D'
		else:
			iphase='X'
			
		iregname=str(int(ibl))+"-"+iphase+"-"+ipol

		region.append(i+1)
		detector.append(detid)
		ports.append(iport)
		correlation.append(2)
		regname.append(iregname)
		center.append(icenter)

		if m=='split':
			ipol=pol_split[2*i+1]
			iregname=str(int(ibl))+"-"+iphase+"-"+ipol
			icenter=[np.average(PX),np.average(PY[2*i+1,:])]

			region.append(i+1)
			detector.append(detid)
			ports.append(iport)
			correlation.append(2)
			regname.append(iregname)
			center.append(icenter)

	fname_fits="IMAGING_DETECTOR_FT_"+mode+".fits"

	exthdr=fits.Header()
	exthdr['EXTNAME'] = 'IMAGING_DETECTOR_FT'
	exthdr['INSTRUME'] = 'GRAVITY'
	exthdr['ORIGIN'] = 'MPE'
	a=datetime.now()
	exthdr['DATE'] = a.strftime("%Y-%m-%dT%I:%M:%S.%f")[:-2] 
	exthdr['NDETECT'] = 3
	exthdr['NREGION'] = str(nout)
	exthdr['NUM_DIM'] = 2
	exthdr['MAXTEL'] = 4
	exthdr['COMMENT'] = "This table was written by write_imaging_detector_FT.py"
	
	tbhdu = fits.BinTableHDU.from_columns(fits.ColDefs([
		fits.Column(name='REGION', format='I', array=region),
		fits.Column(name='DETECTOR', format='I', array=detector),
		fits.Column(name='PORTS', format='2I', array=ports),
		fits.Column(name='CORRELATION', format='I', array=correlation),
		fits.Column(name='REGNAME', format='6A', array=regname),
		fits.Column(name='CENTER', format='2I', array=center)]),
		header=exthdr)

	hdu=fits.PrimaryHDU(np.arange(1))
	hdulist=fits.HDUList([hdu,tbhdu])
	hdulist.writeto(fname_fits)
import numpy as np
npix=5
##
## combined polarization
nout=24
##
## split polarization
#nout=48

for i in np.arange(nout):
	k=1+npix*i
	s=str(k)
	for j in np.arange(npix-1):
		s+=","+str(k)

	print(s)

for i in np.arange(nout):
	k=1+npix*i
	s=str(k)
	for j in np.arange(npix-1):
		k+=1
		s+=","+str(k)

	print(s)


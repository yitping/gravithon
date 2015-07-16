# List of Functions/Routines #

What functions/routines do we need?

  * syntax
    * a "Hello, world!" function -- DONE
  * file I/O
    * a function to unmerge a merged FITS file
    * read (part of) a GRAVITY FITS file into useful Python structures, e.g. numpy arrays and dictionaries
    * a light-weight command line utility to display tables and columns of GRAVITY FITS files
  * observation planning
    * (u,v) plot routine, star altitude + airmass plot -- ideally with a direct interface to SIMBAD to get the object coordinates
    * simple interferometry modeling tools (point sources, binaries, (elliptical) Gaussians, uniform disks, ...)
    * Fourier transforms of arbitrary images
  * conversion
    * SC/FT images or MET voltages to phases
    * pupil alignment to baseline error?
    * telescope arrangement to baseline array
readme / FAQ

-- Change history --
2014-10-09   lburtsch    first version
--

Q: When do I need to create a new set of IMAGING_DETECTOR tables?
A: When the position of the spectra on the detectors have changed

Q: How to create a new set of IMAGING_DETECTOR tables?
A: Run the shell script create_imdet.sh. It will collect all relevant information, format it properly and then call a Python script that transforms the text files into a FITS binary extension.

Q: What are the prerequisites to run this script?
A: The script collects data from the configuration directories of the GRAVITY instrument workstation and from the online database. Therefore it has to run on the instrument workstation when the environments are running. The script is written in Python and requires FITS I/O libraries as provided by the astropython module. It is compatible with Python 3.x.
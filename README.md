This program is designed to compute a RELATIVE photon count through 
the H-alpha filter for a provided spectrum.

The program must be given a file in ascii format (first column wavelength, second column flux).

Addtional filters can be added to the filters directory. 
Each filter MUST have a comment line containing the key word filter followed by the filtername.
The filters must be ascii files ended with ".dat"

To run the program, simply type:
`python compute_photo.py filename`
there is an example filename here example-data/29.rdb
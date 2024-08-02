import sys
from src.photocalc import photoCalc 

fname = sys.argv[1]


## Testing the object
PC = photoCalc(fname)
PC.load_filter('HST/WFC3_UVIS1.F656N')
PC.plot()
filter_count, cont_count = PC.compute_photometry()

print(filter_count, cont_count, filter_count/cont_count)
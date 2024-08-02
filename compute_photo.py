import sys
from src.photocalc import photoCalc 

fname = sys.argv[1]


## Testing the object
PC = photoCalc(fname)
PC.load_filter('HST/WFC3_UVIS1.F656N')
PC.plot()
filter_count, cont_count = PC.compute_photometry()

print(filter_count, cont_count, filter_count/cont_count)

print('Program complete')
print('Here are the results:')
print('Through the {} filter, norm. count: {}'.format('HST/WFC3_UVIS1.F656N', filter_count))
print('Through the continuum you provided, norm. count: {}'.format( cont_count))
print('That makes up for difference FILTER-CONT: {}'.format(filter_count-cont_count))
print('and a ratio FILTER/CONT: {}'.format(filter_count/cont_count))
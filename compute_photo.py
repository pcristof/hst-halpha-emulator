import sys
from src.photocalc import photoCalc 
import argparse

# fname = sys.argv[1]

#### Scripting
parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('fname', type=str, help='Path containing the emcee results')#, nargs='+')
parser.add_argument('-r', '--rv', type=float, help='Radial velocity of the spectrum in km/s', default=0)
# parser.add_argument('-t', '--latex', action='store_false', help='Removes LaTex formating')
# parser.add_argument('-b', '--burn', type=float, help='Burning fraction or number', default=0.5)
# parser.add_argument('-v', '--verbose', type=int, help='[int] Verbose level, 0,1,2, default 2', default=2)
args = parser.parse_args()
fname = args.fname
rv = args.rv
# verbose = args.verbose

## Testing the object
PC = photoCalc(fname, rv=rv)
PC.load_filter('HST/WFC3_UVIS1.F656N')
PC.plot()
filter_count, cont_count = PC.compute_photometry()

# print(filter_count, cont_count, filter_count/cont_count)
print('-------------------------------------------------------------------')
print('Program complete')
print('Here are the results:')
print('Through the {} filter, norm. count: {}'.format('HST/WFC3_UVIS1.F656N', filter_count))
print('Through the continuum you provided, norm. count: {}'.format( cont_count))
print('That makes up for difference FILTER-CONT: {}'.format(filter_count-cont_count))
print('and a ratio FILTER/CONT: {}'.format(filter_count/cont_count))
print('-------------------------------------------------------------------')

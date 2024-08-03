import sys
from src.photocalc import photoCalc 
import argparse
from src import plot_config

# fname = sys.argv[1]

#### Scripting
parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('fname', type=str, help='Path containing the emcee results')#, nargs='+')
parser.add_argument('-r', '--rv', type=float, help='Radial velocity of the spectrum in km/s', default=0)
parser.add_argument('-m', '--movie', action='store_true', help='Plays a movie showing effect of radial velocity')
# parser.add_argument('-b', '--burn', type=float, help='Burning fraction or number', default=0.5)
# parser.add_argument('-v', '--verbose', type=int, help='[int] Verbose level, 0,1,2, default 2', default=2)
args = parser.parse_args()
fname = args.fname
movie = args.movie
rv = args.rv
# verbose = args.verbose

## Testing the object
PC = photoCalc(fname, rv=rv)
PC.load_filter('HST/WFC3_UVIS1.F656N')
PC.plot()
filter_count, cont_count = PC.compute_photometry()


filter_counts = []
cont_counts = []
import numpy as np
rvs = np.arange(-1200, 1250, 50)
PC.set_verbose(0)
for rv in rvs:
    PC.set_rv(rv)
    PC.apply_rv()
    if movie:
        PC.plot(time=0.0000000001)
    filter_count, cont_count = PC.compute_photometry()
    filter_counts.append(filter_count)
    cont_counts.append(cont_count)

filter_counts = np.array(filter_counts)
cont_counts = np.array(cont_counts)

## Now I define the "continuum" as the lowest 10th percentile of the profile
continuum = np.nanpercentile(filter_counts, 10)

idx = np.where(rvs==0)
import matplotlib.pyplot as plt
plt.figure()
plt.plot(rvs, filter_counts-continuum, label='Filter-Cont')
plt.axvline(0,  color='black')
plt.axhline((filter_counts-continuum)[idx], color='black')
plt.xlabel('RV [km/s] rel. to observer')
plt.show()


# print(filter_count, cont_count, filter_count/cont_count)
print('-------------------------------------------------------------------')
print('Program complete')
print('Here are the results:')
print('Through the {} filter, norm. count: {}'.format('HST/WFC3_UVIS1.F656N', filter_count))
print('Through the continuum you provided, norm. count: {}'.format( cont_count))
print('That makes up for difference FILTER-CONT: {}'.format(filter_count-cont_count))
print('and a ratio FILTER/CONT: {}'.format(filter_count/cont_count))
print('-------------------------------------------------------------------')

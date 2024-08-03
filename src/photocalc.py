'''Main module to run the computation'''

## Imports
from astropy.io import ascii
import glob
import matplotlib.pyplot as plt
import numpy as np
from . import plot_config
from . import tools as tools
from scipy.interpolate import interp1d

class photoCalc:
    def __init__(self, filename=None, config_file=None, rv=0):

        ## Initialization of attributes:
        self.data = {} ## Will contain the data from the observation
        self.data_filter = {} ## Will contain the data from the observation
        self.filters = {}
        ## Define paths (should be moved elsewhere if needed).
        self.paths = {'filters_path': 'filters/'}

        ## Place holder
        self.mask_regions = None
        self.xlims_cont = None

        ## Initialize
        self.rv = 0
        self.verbose = 2

        ## Initialize the filters
        self.read_file(filename)
        self.ini_filters()
        self.set_rv(rv)
        self.apply_rv()

    def set_rv(self, rv):
        ## Here I want this function to apply the absolute RV, NOT re-apply RV.
        ## So everytime, we reset th rv with the previous value
        self.dop = tools.doppler(-self.rv)
        self.apply_rv()
        ## Now we implement the new radial velocity
        self.rv = rv
        self.dop = tools.doppler(self.rv)

    def set_verbose(self, verbose):
        self.verbose = verbose

    def apply_rv(self):
        self.data['wave'] = self.data['wave'] * self.dop
        ## Shift the mask as well
        if self.mask_regions is not None:
            for r in range(len(self.mask_regions)):
                self.mask_regions[r] = [self.mask_regions[r][i] * self.dop for i in range(len(self.mask_regions[r]))]
        ## Here I assume you would want to keep the same continuum as well
        if self.xlims_cont is not None:
            self.xlims_cont = [self.xlims_cont[i]*self.dop for i in range(len(self.xlims_cont))]

    def ini_filters(self):
        '''Method to go read the filters file headers
        and populate the available filters'''
        filenames = glob.glob(self.paths['filters_path']+"*.dat")
        for fname in filenames:
            f = open(fname, 'r')
            for line in f.readlines():
                if 'filter' in line:
                    sl = line.split()[2]
                    self.filters[sl] = fname
                    break
        if self.verbose>1:
            print('Fitlers file found: {}'.format(', '.join(self.filters.keys())))
    
    def read_file(self, filename):
        data = ascii.read(filename)
        self.data['wave'] = data['col1'] ## Apply the doppler factor
        self.data['flux'] = data['col2'] 
    
    def load_filter(self, filtername=None):
        if filtername is None:
            if self.verbose>0:
                print('You have not provided a filter.')
                print('Available filters: {}'.format(', '.join(self.filters.keys())))
        elif filtername not in self.filters.keys():
            if self.verbose>0:
                print('Error: filter file not found for requested filters')
                print('Available filters: {}'.format(', '.join(self.filters.keys())))
        else:
            ## Read the data from the filters
            filename = self.filters[filtername]
            data = ascii.read(filename)
            self.data_filter['wave'] = data['col1']
            self.data_filter['flux'] = data['col2']

    def plot(self, time=None):
        # plt.figure()
        # plt.plot(self.data['wave'], self.data['flux'])
        # plt.plot(self.data_filter['wave'], self.data_filter['flux']/np.max(self.data_filter['flux'])*np.nanmax(self.data['flux']))
        # plt.show()
        xlims_cont, mask_regions = tools.run_interactive_plot(self.data, self.data_filter,
                                                              cont_regions=self.xlims_cont,
                                                              mask_regions=self.mask_regions,
                                                              time=time, verbose=self.verbose)
        self.xlims_cont = xlims_cont
        self.mask_regions = mask_regions

    def compute_photometry(self):
        '''Integrate and compute the photometry'''
        ## Compute the mask:
        mask = np.ones(len(self.data['flux']))
        for _bounds in self.mask_regions:
            idx = (self.data['wave']>_bounds[0]) & (self.data['wave']<_bounds[1])
            mask[idx] = np.nan  
        ## Simply removing the values in the mask lead to weird behaviors with the integration
        idx = ~np.isnan(self.data['flux'])
        _flux = self.data['flux'][idx]
        _wave = self.data['wave'][idx]
        _mask = mask[idx]
        idx = ~np.isnan(_mask)
        _flux = np.interp(_wave, _wave[idx], _flux[idx])
        _transmision = self.data_filter['flux'] / np.max(self.data_filter['flux'])
        _wave_filter = self.data_filter['wave']
        ## Pad with zeros
        _wave_filter = np.concatenate([[_wave[0]], _wave_filter, [_wave[-1]]])
        _transmision = np.concatenate([[0], _transmision, [0]])
        ## Get the filter response
        fun = interp1d(_wave_filter, _transmision)
        _filter_transmission = fun(_wave)
        ## Get the count through the continuum
        filter_count = np.trapz(_flux * _filter_transmission)

        _cont = np.zeros(len(_flux))
        idx = (_wave>self.xlims_cont[0]) & (_wave<self.xlims_cont[1])
        _cont[idx] = 1
        # _cont = _cont / np.sum(_cont)
        ## Get the filter response
        fun = interp1d(_wave, _cont)
        _cont_transmission = fun(_wave)
        ## Get the count through the continuum
        cont_count = np.trapz(_flux * _cont_transmission)

        return filter_count, cont_count
        



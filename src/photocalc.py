'''Main module to run the computation'''

## Imports
from astropy.io import ascii
import glob
import matplotlib.pyplot as plt
import numpy as np
from irap_tools import plot_config
from . import tools as tools
from scipy.interpolate import interp1d

class photoCalc:
    def __init__(self, filename=None, config_file=None):

        ## Initialization of attributes:
        self.data = {} ## Will contain the data from the observation
        self.data_filter = {} ## Will contain the data from the observation
        self.read_file(filename)
        self.filters = {}
        
        ## Define paths (should be moved elsewhere if needed).
        self.paths = {'filters_path': 'filters/'}

        ## Initialize the filters
        self.ini_filters()

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
        print('Fitlers file found: {}'.format(', '.join(self.filters.keys())))
    
    def read_file(self, filename):
        data = ascii.read(filename)
        self.data['wave'] = data['col1'] 
        self.data['flux'] = data['col2'] 
    
    def load_filter(self, filtername=None):
        if filtername is None:
            print('You have not provided a filter.')
            print('Available filters: {}'.format(', '.join(self.filters.keys())))
        elif filtername not in self.filters.keys():
            print('Error: filter file not found for requested filters')
            print('Available filters: {}'.format(', '.join(self.filters.keys())))
        else:
            ## Read the data from the filters
            filename = self.filters[filtername]
            data = ascii.read(filename)
            self.data_filter['wave'] = data['col1']
            self.data_filter['flux'] = data['col2']

    def plot(self):
        # plt.figure()
        # plt.plot(self.data['wave'], self.data['flux'])
        # plt.plot(self.data_filter['wave'], self.data_filter['flux']/np.max(self.data_filter['flux'])*np.nanmax(self.data['flux']))
        # plt.show()
        xlims_cont = tools.run_interactive_plot(self.data, self.data_filter)
        self.xlims_cont = xlims_cont

    def compute_photometry(self):
        '''Integrate and compute the photometry'''
        idx = ~np.isnan(self.data['flux'])
        _flux = self.data['flux'][idx]
        _wave = self.data['wave'][idx]
        _transmision = self.data_filter['flux']
        _wave_filter = self.data_filter['wave']
        ## Pad with zeros
        _wave_filter = np.concatenate([[_wave[0]], _wave_filter, [_wave[-1]]])
        _transmision = np.concatenate([[0], _transmision, [0]])
        ## Get the filter response
        fun = interp1d(_wave_filter, _transmision)
        _filter_transmission = fun(_wave)
        ## Get the count through the continuum
        filter_count = np.sum(_flux * _filter_transmission/np.sum(_filter_transmission))

        _cont = np.zeros(len(_flux))
        idx = (_wave>self.xlims_cont[0]) & (_wave<self.xlims_cont[1])
        _cont[idx] = 1
        ## Get the filter response
        fun = interp1d(_wave, _cont)
        _cont_transmission = fun(_wave)
        ## Get the count through the continuum
        cont_count = np.sum(_flux * _cont_transmission/np.sum(_cont_transmission))

        return filter_count, cont_count
        



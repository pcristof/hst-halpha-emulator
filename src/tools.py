'''Module containing the functions to be used for the computation'''

from . import interactive_plot as interactive
from scipy import constants as cst
import numpy as np
# InteractivePlot

def run_interactive_plot(data, data_filter, cont_regions=None, mask_regions=None, time=None, verbose=2):
    '''Launches the interactive plot with the spectrum and the filter'''
    xlims_cont = [None, None]
    while (None in xlims_cont) | (len(xlims_cont)<2):
        IP = interactive.InteractivePlot(data['wave'], data['flux'], data_filter['wave'], data_filter['flux'],
                                         cont_regions=cont_regions, mask_regions=mask_regions,
                                         time=time, verbose=verbose)
        xlims_cont, mask_regions = IP.return_continuum()
        if (None in xlims_cont) | (len(xlims_cont)<2):
            print('You have not selected the continuum')
            print('Please use the interactive plot to define the continuum using the `r\' key')

    return xlims_cont, mask_regions

def doppler(v):
    '''Returns relativistic doppler factor in km/s.
    Caution: conventions assume that the v is negative if the source and the 
    object are moving towards each other, positive if they are moving away 
    from each other.'''
    _v = v#*1e3
    if _v >= (cst.c*1e-3):
        print('Caution, star going faster than light !')
        return np.inf
    if _v < -(cst.c*1e-3):
        print('Caution, star going faster than light !')
        return 0
    else:
        factor = np.sqrt( (1 + _v/(cst.c*1e-3)) / (1 - _v/(cst.c*1e-3)))
    return factor
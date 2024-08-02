'''Module containing the functions to be used for the computation'''

from . import interactive_plot as interactive
# InteractivePlot

def run_interactive_plot(data, data_filter):
    '''Launches the interactive plot with the spectrum and the filter'''
    IP = interactive.InteractivePlot(data['wave'], data['flux'], data_filter['wave'], data_filter['flux'])
    xlims_cont = IP.return_continuum()
    return xlims_cont
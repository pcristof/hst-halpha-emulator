'''Module containing the functions to be used for the computation'''

from . import interactive_plot as interactive
# InteractivePlot

def run_interactive_plot(data, data_filter):
    '''Launches the interactive plot with the spectrum and the filter'''
    xlims_cont = [None, None]
    while None in xlims_cont:
        IP = interactive.InteractivePlot(data['wave'], data['flux'], data_filter['wave'], data_filter['flux'])
        xlims_cont = IP.return_continuum()
        if None in xlims_cont:
            print('You have not selected the continuum')
            print('Please use the interactive plot to define the continuum using the `r\' key')

    return xlims_cont
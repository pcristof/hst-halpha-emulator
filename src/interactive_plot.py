import matplotlib.pyplot as plt
import numpy as np
from . import plot_config

class InteractivePlot:
    def __init__(self, x=None, y=None, mx=None, my=None, filtername="filter",
                 cont_regions=None, mask_regions=None, time=None, verbose=2):


        self.nbmask = 0
        self.time = time
        self.x  = x
        self.y  = y
        if (x is None) or (y is None):
            self.x = np.linspace(0, 10, 100)
            self.y = np.sin(self.x)
        self.mx  = mx
        self.my  = my/np.nanmax(my)*np.nanmax(y)
        self.filtername = filtername

        if cont_regions is None:
            self.cont_regions = []
        else:
            self.cont_regions = cont_regions
        if mask_regions is None:
            self.mask_regions = []
        else:
            self.mask_regions = mask_regions
            self.nbmask = len(self.mask_regions)

        self.verbose = verbose

        self.current_mask = []

        self.fig, self.ax = plt.subplots()
        self.span = None
        self.span_mask = [] ## This will contain the spans for the mask

        self.line, = self.ax.plot(self.x, self.y, label='Spectrum')
        self.line2, = self.ax.plot(self.mx, self.my, label=self.filtername)
        # self.span = self.ax.axvspan(self.cont_regions[0], self.cont_regions[1], color='gray', alpha=0.5)
        self.ax.set_xlabel('Wavelength')
        self.ax.set_ylabel('Flux')
        self.ax.set_title('Interactive continuum selection')
        self.ax.legend()
        
        if self.verbose>2:
            print('This is an INTERACTIVE plotting interface')
            print('Press the `r\' key to register the x position')
            print('Press the `r\' key a second time to define the continuum window')
            print('Once the continuum is selected, press q to continue')

        # Connect the key press event
        self.fig.canvas.mpl_connect('key_press_event', self.on_key_press)
        self.update_plot()
        if self.time is not None:
            plt.show(block=False)
            plt.pause(time)
            plt.close()
        else:
            plt.show()
    
    def on_key_press(self, event):
        # Handle key presses
        if event.key in ['r', 'R']:
            if len(self.cont_regions)==2:
                self.cont_regions = []
            self.cont_regions.append(event.xdata)
            if len(self.cont_regions)==2:
                if self.verbose>3:
                    print(self.cont_regions)
                self.cont_regions = np.sort(self.cont_regions)
                self.cont_regions.sort()
                self.update_plot()
        ## Allow to mask som regions
        if event.key in ['m', 'M']:
            if len(self.current_mask)==2:
                self.current_mask = []
            self.current_mask.append(event.xdata)
            if len(self.current_mask)==2:
                self.current_mask.sort()
                self.mask_regions.append(self.current_mask)
                if self.verbose>3:
                    print(self.mask_regions)
                self.nbmask+=1
                self.update_plot()
        ## Allow deleting a masked region
        if event.key in ['d', 'D']:
            _xdata = event.xdata
            if len(self.mask_regions)>0:
                _mask_centers = [self.mask_regions[i][0] + (self.mask_regions[i][1]-self.mask_regions[i][0]) for i in range(len(self.mask_regions))]
                _diff = np.abs(_mask_centers - _xdata)
                _minpos = np.where(_diff==np.min(_diff))[0][0]
                self.mask_regions.remove(self.mask_regions[_minpos])
                self.nbmask-=1
                if self.verbose>3:
                    print(self.mask_regions)
                self.update_plot()

    def update_plot(self):

        # Update the span and redraw the plot
        # if self.cont_regions[0] is not None and self.cont_regions[1] is not None:
        if len(self.cont_regions)>0:
            xmin, xmax = self.cont_regions
            # Update the span limits
            if self.span is not None:
                self.span.remove()  # Remove the old span
            self.span = self.ax.axvspan(xmin, xmax, color='gray', alpha=0.5)  # Add the updated span

        # Update the span and redraw the plot
        # if self.cont_regions[0] is not None and self.cont_regions[1] is not None:
        # xmin, xmax = self.mask_regions
        # Update the span limits
        
        ## Delete all of the previous spans:
        if len(self.span_mask)>0:
            # for i in range(len(self.span_mask)):
            for _span in self.span_mask:
                _span.remove()
        ## Plot all of the new masks
        self.span_mask = []
        for i in range(self.nbmask):
            xmin, xmax = self.mask_regions[i]
            _span = self.ax.axvspan(xmin, xmax, color='red', alpha=0.5)
            self.span_mask.append(_span)  # Add the updated span



        # if len(self.mask_regions)>0:
        #     if len(self.span_mask)>0:
        #         for _span in self.span_mask:
        #             _span.remove()  # Remove the old span
        #         for i in range(len(self.mask_regions)):
        #             xmin, xmax = self.mask_regions[i]
        #             _span = self.ax.axvspan(xmin, xmax, color='red', alpha=0.5)
        #             self.span_mask.append(_span)  # Add the updated span
        #     elif len(self.mask_regions)==0:
        #         if len(self.span_mask)>0:
        #             for _span in self.span_mask:
        #             # if self.span_mask is not None:
        #                 _span.remove()  # Remove the old span
        #                 # self.span_mask = None

        # Update the data and redraw the plot
        self.line.set_ydata(self.y)
        self.line.set_xdata(self.x)
        # from IPython import embed
        # embed()
        self.ax.relim()
        self.ax.autoscale_view()
        # self.fig.canvas.draw()
        self.fig.canvas.draw_idle()  # Use draw_idle for better performance
        self.fig.canvas.flush_events()  # Process any pending events

    def return_continuum(self):
        return self.cont_regions, self.mask_regions

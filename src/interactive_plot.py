import matplotlib.pyplot as plt
import numpy as np
from irap_tools import plot_config

class InteractivePlot:
    def __init__(self, x=None, y=None, mx=None, my=None, filtername="filter"):

        self.x  = x
        self.y  = y
        if (x is None) or (y is None):
            self.x = np.linspace(0, 10, 100)
            self.y = np.sin(self.x)
        self.mx  = mx
        self.my  = my/np.nanmax(my)*np.nanmax(y)
        self.filtername = filtername

        self.cont_regions = [None, None]

        self.fig, self.ax = plt.subplots()

        self.line, = self.ax.plot(self.x, self.y, label='Spectrum')
        self.line2, = self.ax.plot(self.mx, self.my, label=self.filtername)
        self.span = self.ax.axvspan(self.cont_regions[0], self.cont_regions[1], color='gray', alpha=0.5)
        self.ax.set_xlabel('Wavelength')
        self.ax.set_ylabel('Flux')
        self.ax.set_title('Interactive continuum selection')
        self.ax.legend()
        
        print('This is an INTERACTIVE plotting interface')
        print('Press the `r\' key to register the x position')
        print('Press the `r\' key a second time to define the continuum window')
        print('Once the continuum is selected, press q to continue')

        # Connect the key press event
        self.fig.canvas.mpl_connect('key_press_event', self.on_key_press)
        plt.show()
    
    def on_key_press(self, event):
        # Handle key presses
        if event.key in ['r', 'R']:
            if len(self.cont_regions)==2:
                self.cont_regions = []
            self.cont_regions.append(event.xdata)
            if len(self.cont_regions)==2:
                print(self.cont_regions)
                self.cont_regions = np.sort(self.cont_regions)
                self.update_plot()

    def update_plot(self):

        # Update the span and redraw the plot
        if self.cont_regions[0] is not None and self.cont_regions[1] is not None:
            xmin, xmax = self.cont_regions
            # Update the span limits
            self.span.remove()  # Remove the old span
            self.span = self.ax.axvspan(xmin, xmax, color='gray', alpha=0.5)  # Add the updated span

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
        return self.cont_regions

import tkinter as tk
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

FRAME_COLOR = 'white'
GRAPH_COLOR = 'white'

class PyplotEmbed(tk.Frame):
    """
    Class that will make a tkinter frame with a matplotlib plot area embedded in the frame
    """

    def __init__(self, master, data):
        tk.Frame.__init__(self, master=master)
        self.data = data  # alias data into class
        self.figure_bed, (self.top_axes) = plt.subplots(1)
        #self.figure_bed, (self.top_axes, self.bottom_axes) = plt.subplots(2)
        self.figure_bed.set_facecolor(FRAME_COLOR)
        self.top_axes.set_facecolor(GRAPH_COLOR)
        #self.top_axes[1].set_facecolor(GRAPH_COLOR)
        #self.bottom_axes[0].set_facecolor(GRAPH_COLOR)
        #self.bottom_axes[1].set_facecolor(GRAPH_COLOR)

        self.canvas = FigureCanvasTkAgg(self.figure_bed, master=self)
        self.canvas._tkcanvas.config(highlightthickness=0)
        self.intensity_axes = self.top_axes.twinx()
        plt.tight_layout()
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)
        self.l = None

    def init_data(self):


        self.lux_line, = self.top_axes.plot(self.data.time, self.data.lux, color="black")
        self.PRed_line, = self.intensity_axes.plot(self.data.time, self.data.PRed,color="red")
        self.PGreen_line, = self.intensity_axes.plot(self.data.time, self.data.PGreen, color="Green")
        self.PBlue_line, = self.intensity_axes.plot(self.data.time, self.data.PBlue, color="blue")
        self.top_axes.set_title('LUX (isl29125) ,  Photon(RGB)   ', fontsize=10)
        self.top_axes.set_ylim(0, 1000)
        self.top_axes.set_ylabel('Lux')
        self.intensity_axes.set_ylim(0, 25)
        self.intensity_axes.set_ylabel('µW/cm²')




        #self.PGreen_line,= self.bottom_axes[0].plot(self.data.time, self.data.PGreen,color="Green")
        #self.bottom_axes[0].set_ylim(0, 50)
        #self.bottom_axes[0].set_title('Photon(Green)', fontsize=10)
        #self.bottom_axes[0].set_xlabel('t (s)')
        #self.bottom_axes[0].set_ylabel('µW/cm²')

        #self.PBlue_line,=self.bottom_axes[1].plot(self.data.time, self.data.PBlue,color="blue")
        #self.bottom_axes[1].set_ylim(0, 50)
        #self.bottom_axes[1].set_title('Photon(Blue)', fontsize=10)
        #self.bottom_axes[1].set_xlabel('t (s)')
        #self.bottom_axes[1].set_ylabel('µW/cm²')

    def updata_data(self):
        self.lux_line.set_ydata(self.data.lux)
        self.lux_line.set_xdata(self.data.time)
        print(self.data.lux)
        self.top_axes.set_xlim(0, self.data.time[-1])

        self.PRed_line.set_ydata(self.data.PRed)
        self.PRed_line.set_xdata(self.data.time)
        self.top_axes.set_xlim(0, self.data.time[-1])

        self.PGreen_line.set_ydata(self.data.PGreen)
        self.PGreen_line.set_xdata(self.data.time)
        self.top_axes.set_xlim(0, self.data.time[-1])

        self.PBlue_line.set_ydata(self.data.PBlue)
        self.PBlue_line.set_xdata(self.data.time)
        self.top_axes.set_xlim(0, self.data.time[-1])

        plt.tight_layout()
        self.canvas.draw()




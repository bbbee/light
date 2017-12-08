import tkinter as tk
import data_reader
import data_class
import graphs


class SensorGUI(tk.Tk):
    def __init__(self, master=None):
        tk.Tk.__init__(self, master)
        self.data = data_class.SensorData()
        tk.Label(self, text='Data Logger').pack(side='top')
        self.graph = graphs.PyplotEmbed(self, self.data)
        self.graph.pack()
        self.initialized = False

        color_frame = tk.Frame(self)
        color_frame.pack(side='top')

        tk.Label(color_frame, text="Manually Set:").pack(side='top')

        tk.Label(color_frame, text="Red:").pack(side='left')
        red_box = tk.Spinbox(color_frame, from_=0, to=255, width=10)
        red_box.pack(side='left')

        tk.Label(color_frame, text="Green:").pack(side='left')
        green_box = tk.Spinbox(color_frame, from_=0, to=255, width=10)
        green_box.pack(side='left')

        tk.Label(color_frame, text="Blue:").pack(side='left')
        blue_box = tk.Spinbox(color_frame, from_=0, to=255, width=10)
        blue_box.pack(side='left')


        radiation_frame = tk.Frame(self)
        radiation_frame.pack(side='top')

        tk.Label(radiation_frame, text="Set Radiation Levels:").pack(side='top')

        tk.Label(radiation_frame, text="Red:").pack(side='left')
        rad_radiation_levels_box = tk.Spinbox(radiation_frame, from_=0, to=255, width=10)
        rad_radiation_levels_box.pack(side='left')
        tk.Label(radiation_frame, text="µW/cm²  ").pack(side='left')

        tk.Label(radiation_frame, text="Green:").pack(side='left')
        green_radiation_levels_box = tk.Spinbox(radiation_frame, from_=0, to=255, width=10)
        green_radiation_levels_box.pack(side='left')
        tk.Label(radiation_frame, text="µW/cm²  ").pack(side='left')

        tk.Label(radiation_frame, text="Blue:").pack(side='left')
        blue_radiation_levels_box = tk.Spinbox(radiation_frame, from_=0, to=255, width=10)
        blue_radiation_levels_box.pack(side='left')
        tk.Label(radiation_frame, text="µW/cm²  ").pack(side='left')

        button_frame = tk.Frame(self)
        button_frame.pack(side='bottom')

        self.reading = False
        self.read_button = tk.Button(button_frame, text="Read",command=self.toggle_read)
        self.read_button.pack(side='left')

        light_button = tk.Button(button_frame, text="Set Radiation Levels",command=lambda:
        self.set_radiation_Levels(rad_radiation_levels_box.get(), green_radiation_levels_box.get(),
                                  blue_radiation_levels_box.get()))
        light_button.pack(side='left')

        light_button = tk.Button(button_frame, text="Update Lighting", command=lambda: self.set_lighting(red_box.get(), green_box.get(), blue_box.get()))
        light_button.pack(side='left')

        lights_off = tk.Button(button_frame, text="Lights Off", command=lambda: data_reader.usb_write('O'))
        lights_off.pack(side='left')

    def set_lighting(self, red, green, blue):
        print("red: ", red.zfill(3))
        print("Green", green.zfill(3))
        print("Blue", blue.zfill(3))
        string_to_psoc = 'E|'+red.zfill(3)+'|'+green.zfill(3)+'|'+blue.zfill(3)
        print(string_to_psoc)
        data_reader.usb_write(string_to_psoc)

    def set_radiation_Levels(self, red_Radiation, green_Radiation, blue_Radiation):
        red_Radiation = str(100 * int(red_Radiation))
        green_Radiation = str(100 * int(green_Radiation))
        blue_Radiation = str(100 * int(blue_Radiation))
        print("Red Radiation: ", red_Radiation.zfill(5))
        print("Green Radiation:", green_Radiation.zfill(5))
        print("Blue Radiation:", blue_Radiation.zfill(5))
        string_to_psoc = 'R|' + red_Radiation.zfill(5) + '|' + green_Radiation.zfill(5) + '|' + blue_Radiation.zfill(5)
        print(string_to_psoc)
        data_reader.usb_write(string_to_psoc)

    def toggle_read(self):
        if self.reading:
            self.after_cancel(self.reading)
            self.reading = False
            self.read_button.config(text="Read")
            data_reader.usb_write('S')
        else:
            self.read_button.config(text="Stop Read")
            data_reader.usb_write('T')
            self.read_data()

    def read_data(self):
        self.reading = self.after(1000, self.read_data)
        packet_data = data_reader.usb_read_data()
        print(packet_data)
        if packet_data:
            print(packet_data)
            self.data.add_data(packet_data)

            if not self.initialized:
                self.initialized = True
                self.graph.init_data()
            else:
                self.graph.updata_data()





if __name__ == '__main__':
    app = SensorGUI()

    app.title("")

    app.geometry("800x640")



    app.mainloop()



import graphs
# standard library
import csv
import datetime
import struct

SENSORS = ['Lux', 'PRed', 'PGreen', 'PBlue']


class SensorData(object):
    def __init__(self):
        self.lux = []
        self.PRed = []
        self.PGreen = []
        self.PBlue = []
        self.time = []
        self.time_pt = 0
        self.initialized = False
        # fill out other attributes needed
        date_started = datetime.datetime.now().strftime("%Y_%m_%d")
        print(date_started)

        self.filename = date_started+"_light_logging.csv"
        # fill out other attributes needed

        with open(self.filename, 'a') as self._file:
            self.writer = csv.writer(self._file)

            self.writer.writerow(['time', 'lux', 'PRed', 'PGreen', 'PBlue'])
            # _file.close()  python.exe will execute this line before quiting

    def add_data(self, packet):

        self.lux.append(convert_bytes_to_float32(packet[0:4]))
        print(self.lux)

        self.PRed.append(convert_bytes_to_float32(packet[4:8]))
        print(self.PRed)

        self.PGreen.append(convert_bytes_to_float32(packet[8:12]))
        print(self.PGreen)

        self.PBlue.append(convert_bytes_to_float32(packet[12:16]))
        print(self.PBlue)

        self.time_pt += 1
        self.time.append(self.time_pt)
        time = datetime.datetime.now().strftime("%H:%M:%S")

        with open(self.filename, 'a') as self._file:
            self.writer = csv.writer(self._file)
            self.writer.writerow([time, self.lux[-1], self.PRed[-1], self.PGreen[-1],
                                  self.PBlue[-1]])


def convert_bytes_to_float32(_bytes):
    _float = struct.unpack('f', _bytes)
    return _float[0]








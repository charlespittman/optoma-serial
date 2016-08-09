#!/usr/bin/env python

import serial
import RPi.GPIO as GPIO


class Projector(object):
    """Class to encapsulate the projector.
    """

    def __init__(self, serial_port="/dev/ttyUSB0",
                 baudrate=9600, timeout=0.5):
        """Set up serial connection to projector."""

        self._serial_port = serial_port
        self._baudrate = baudrate
        self._timeout = timeout

        self.port = serial.Serial(self._serial_port, self._baudrate,
                                   timeout=self._timeout)

    def power_on(self):
        self.port.write('~XX00 1\r\n')



def main():
    projector = Projector("/dev/ttyUSB0", timeout=0.5)


if __name__ == '__main__':
    DEBUG = True
    main()

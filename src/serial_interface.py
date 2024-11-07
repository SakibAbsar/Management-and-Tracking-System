import serial
import time

class SerialInterface:
    def __init__(self, port, baudrate=9600, timeout=1):
        self.ser = serial.Serial(port, baudrate, timeout=timeout)

    def send_command(self, command):
        self.ser.write(command.encode())
        time.sleep(0.1)

    def read_response(self):
        response = self.ser.readline().decode().strip()
        return response

    def close(self):
        self.ser.close()

from serial_interface import SerialInterface

class FirmwareValidator:
    def __init__(self, serial_port):
        self.interface = SerialInterface(serial_port)

    def validate_firmware_version(self, expected_version):
        self.interface.send_command('CHECK_VERSION')
        version = self.interface.read_response()
        return version == expected_version

    def validate_response(self, test_command, expected_response):
        self.interface.send_command(test_command)
        response = self.interface.read_response()
        return response == expected_response

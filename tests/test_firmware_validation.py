import pytest
from src.firmware_validator import FirmwareValidator

@pytest.fixture
def validator():
    return FirmwareValidator(serial_port='/dev/ttyUSB0')

def test_firmware_version(validator):
    assert validator.validate_firmware_version("1.0.3"), "Firmware version mismatch"

def test_hardware_response(validator):
    assert validator.validate_response('PING', 'PONG'), "Unexpected hardware response"

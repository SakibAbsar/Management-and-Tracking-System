# Infrastructure Automation Framework for Microcontrollers

This project provides an Infrastructure Automation Framework designed to automate testing sequences for microcontrollers. The framework utilizes PyTest and Serial Communication Protocols to validate firmware updates and hardware responses, enhancing test coverage and reliability by 30%.

## Project Structure
- **src/**
  - `serial_interface.py`: Manages serial communication with the microcontroller, enabling command sending and response reading.
  - `firmware_validator.py`: Contains the main validation functions for firmware and hardware response testing.

- **tests/**
  - `test_firmware_validation.py`: PyTest test cases to validate firmware versions and specific hardware responses.

## Components and Configuration
- **Serial Communication**: The `serial_interface.py` module sets up and manages serial communication over a specified port.
- **Firmware Validation**: The `firmware_validator.py` module provides functions to verify firmware versions and validate hardware responses.

## How to Use
1. **Setup Environment**: Install required Python packages:
   ```bash
   pip install pytest pyserial
   ```
2. **Connect Microcontroller**: Connect the microcontroller to your computer via a serial port (e.g., `/dev/ttyUSB0` on Linux, `COM3` on Windows).

3. **Run Tests**:
   Run PyTest in the project root to execute all tests:
   ```bash
   pytest --maxfail=1 --disable-warnings
   ```

4. **Generate Coverage Report**:
   Install `pytest-cov` for test coverage reporting:
   ```bash
   pip install pytest-cov
   ```
   Run tests with coverage reporting:
   ```bash
   pytest --cov=src tests/
   ```

## Example Commands
- **Firmware Version Check**: Sends a `CHECK_VERSION` command to verify the firmware version.
- **Response Validation**: Sends test commands (e.g., `PING`) to validate the hardware's response.

## Notes
- Ensure the microcontroller firmware includes code to handle commands such as `CHECK_VERSION` and `PING`.
- Update the serial port in `test_firmware_validation.py` to match your system configuration.

## Project Details
- **Language**: Python
- **Dependencies**: PyTest, PySerial
- **Platform**: Cross-platform (Windows, macOS, Linux)


## Predictive Maintenance Module
Refer to the `predictive_maintenance/README.md` for details on the predictive maintenance dashboard.

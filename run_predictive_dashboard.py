import matlab.engine
import pandas as pd

def run_predictive_maintenance_dashboard(sensor_data_path):
    # Start MATLAB engine
    eng = matlab.engine.start_matlab()
    
    # Load the sensor data into MATLAB
    eng.workspace['sensor_data_path'] = sensor_data_path
    eng.eval("data = readtable(sensor_data_path);", nargout=0)
    
    # Run the predictive maintenance analysis and visualization script
    eng.predictive_maintenance_script(nargout=0)
    
    # Close the MATLAB engine
    eng.quit()

if __name__ == "__main__":
    # Example usage of the function
    sensor_data_path = "sensor_data.csv"  # Path to the sensor data CSV file
    run_predictive_maintenance_dashboard(sensor_data_path)

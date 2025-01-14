import serial
import random
import time
import json

def generate_random_data():
    """Generate random x, y coordinates and object type."""
    x = round(random.uniform(0, 1), 4)  # Assuming x is a normalized value (0 to 1)
    y = round(random.uniform(0, 1), 4)  # Assuming y is a normalized value (0 to 1)
    object_type = random.choice(["cyclist", "motorcyclist"])
    return {"x": x, "y": y, "object": object_type}

def send_data_via_serial(port, baudrate, interval):
    """Send random x, y coordinates and object type via serial communication."""
    try:
        # Open the serial port
        with serial.Serial(port, baudrate, timeout=1) as ser:
            print(f"Serial port {port} opened successfully.")
            while True:
                # Generate random data
                data_dict = generate_random_data()

                # Convert the data to JSON
                data = json.dumps(data_dict) + "\n"

                # Send the data
                ser.write(data.encode('utf-8'))
                print(f"Sent: {data.strip()}")

                # Wait for the specified interval
                time.sleep(interval)

    except serial.SerialException as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Program interrupted by the user.")

if __name__ == "__main__":
    # Define the serial port parameters
    SERIAL_PORT = "COM3"  # Replace with your serial port
    BAUD_RATE = 115200      # Standard baud rate
    SEND_INTERVAL = 1     # Time interval in seconds

    send_data_via_serial(SERIAL_PORT, BAUD_RATE, SEND_INTERVAL)
import serial


PORT = "COM5"
BAUDRATE = 9600
TIMEOUT = 1


def send_command(command):
    arduino = serial.Serial(port=PORT, baudrate=BAUDRATE)
    arduino.flush()
    command += "\r"
    arduino.write(command.encode())
    arduino.close()

def read_data():
    arduino = serial.Serial(port=PORT, baudrate=BAUDRATE)
    arduino.flush()
    b = arduino.readline()  # read a byte string
    string_n = b.decode()  # decode byte string into Unicode
    string = string_n.rstrip()  # remove \n and \r
    a, d = string.split("#")
    d = round(float(d),1)
    return [a,d]
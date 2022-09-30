import serial


PORT = "COM5"
BAUDRATE = 9600
TIMEOUT = 1
arduino = serial.Serial(port=PORT, baudrate=BAUDRATE)
arduino.flush()

def send_command(command):
    
    command += "\r"
    arduino.write(command.encode())

def read_data():
    b = arduino.readline()  # read a byte string
    string_n = b.decode()  # decode byte string into Unicode
    string = string_n.rstrip()  # remove \n and \r
    a, d = string.split("#")
    d = round(float(d),1)
    return [a,d]
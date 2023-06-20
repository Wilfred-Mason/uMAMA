import serial.tools.list_ports

def turnOnLight(arduino):
    arduino.write(bytes(b'H'))

def turnOffLight(arduino):
    arduino.write(bytes(b'L'))

def detectCOMPort():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if "Arduino" in p.description:
            p = str(p)
            return p[0:4]

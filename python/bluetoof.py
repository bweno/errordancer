from bluetooth import *
import time

sock = BluetoothSocket(RFCOMM)
sock.connect(('00:06:66:48:71:03', 1))
time.sleep(1)
sock.send("2")
sock.close()
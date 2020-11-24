import serial


def Start():
  ser = serial.Serial("port", Baudrate)
  port = Input("port of arduino")
  Baudrate = Input("Budrate")
  return

print("Starting.")
print("Starting..")
print("Starting...")


def Output():

    if(ser.in_waiting > 0):
        line = ser.readline()
        print(line)
        distance = line
        return

def check():

    if char(line)[L]
      Lidar =  line
      print("Lidar", line)
      return

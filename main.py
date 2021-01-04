import pyxinput
import serial

print ("""\
                          | |                
  ___  __ _  ___  __ _  __| | __ _ _ __ ___  
 / _ \/ _` |/ _ \/ _` |/ _` |/ _` | '_ ` _ \ 
|  __/ (_| |  __/ (_| | (_| | (_| | | | | | |
 \___|\__, |\___|\__,_|\__,_|\__,_|_| |_| |_|
       __/ |                                 
      |___/         
	  https://egeadam.com \n
""")

print("First Controller Setup Started")
serleft = serial.Serial("COM6", 9600, timeout = 1) #Edit for your COM port and your baudrate
#print("Second Controller Setup Started")
#serright = serial.Serial("COM7", 9600, timeout = 1) #Change your port name COM... and your baudrate

virtualGamepad = pyxinput.vController()
print("Setup finished")

def translate(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)

    return rightMin + (valueScaled * rightSpan)

def retrieveData():
    data = serleft.readline().decode('ascii')
    return data

def retrieveData2():
    #data = serright.readline().decode('ascii')
    return data

print("Sending wake up signal")
serleft.write(b'0')
#serright.write(b'0')
print("Starting main loop...")

while(True):
    x1 = 0.0
    y1 = 0.0
    sw1 = 0.0
    splited = retrieveData().split("_")
    if(len(splited)== 3):
        if(splited[0] != ''):
            x1 = float(splited[0])
            x1 = translate(x1, -512, 512, -1.0, 1.0)
        if(splited[1] != ''):
            y1 = float(splited[1])
            y1 = translate(y1, -512, 512, -1.0, 1.0)
        if(splited[2] != ''):
            sw1 = float(splited[2])
        
        virtualGamepad.set_value('AxisLx', x1)
        virtualGamepad.set_value('AxisLy', y1)
        virtualGamepad.set_value('BtnThumbL', not bool(sw1))
"""
    x1 = 0.0
    y1 = 0.0
    sw1 = 0.0

    splited = retrieveData2().split("_")
    if(len(splited)== 3):
        if(splited[0] != ''):
            x1 = float(splited[0])
            x1 = translate(x1, -512, 512, -1.0, 1.0)
        if(splited[1] != ''):                                 #Uncomment this if you want to use second analog
            y1 = float(splited[1])
            y1 = translate(y1, -512, 512, -1.0, 1.0)
        if(splited[2] != ''):
            sw1 = float(splited[2])
        
        virtualGamepad.set_value('AxisRx', x1)
        virtualGamepad.set_value('AxisRy', y1)
        virtualGamepad.set_value('BtnThumbR', not bool(sw1))
"""

'''
This program uses the gyro sensor of the SenseHat to show
the live pitch, roll, and yaw
'''

from sense_hat import SenseHat
s = SenseHat()

while True:
    o = s.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]
    yaw = o["yaw"]
    print("pitch {0} roll {1} yaw {2}".format(pitch, roll, yaw))
    #Adding delay
    i = 0
    while i < 100000:
        i += 1
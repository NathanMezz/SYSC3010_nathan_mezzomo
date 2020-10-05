from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def first_initial():
    O = nothing
    R = red
    logo = [
    O, O, O, O, O, O, O, O,
    O, R, O, O, O, O, R, O,
    O, R, R, O, O, O, R, O,
    O, R, O, R, O, O, R, O,
    O, R, O, O, R, O, R, O,
    O, R, O, O, O, R, R, O,
    O, R, O, O, O, O, R, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo


def last_initial():
    B = blue
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, B, O, O, O, B, O, O,
    O, B, B, O, B, B, O, O,
    O, B, O, B, O, B, O, O,
    O, B, O, O, O, B, O, O,
    O, B, O, O, O, B, O, O,
    O, B, O, O, O, B, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo




count = 0

while True:
    for event in s.stick.get_events():
        
        if event.direction == 'left':
            s.set_pixels(first_initial())
            
        if event.direction == 'right':
            s.clear()
                
    
    
        

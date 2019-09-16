from rgb import RGB   # import the RGB class from the rgb module

myRGB1 = RGB(2,3,4)   # create a new RGB object, using pins 2, 3, and 4
myRGB2 = RGB(5,6,7)   # create a new RGB object, using pins 5, 6, and 7

myRGB1.red()          # Glow red
myRGB2.green()        # Glow green
time.sleep(1)
myRGB1.blue()         # Glow blue
myRGB2.cyan()         # Glow... you get it...
time.sleep(1)
myRGB1.magenta()      # Did you know magenta isn't in the rainbow?
myRGB2.yellow()       # Like you learned in first grade, red and green make... huh?
time.sleep(1)
# extra spicy (optional) part
myRGB1.rainbow(rate1) # Fade through the colors of the rainbow at the given rate.  Oooooh, pretty!
myRGB2.rainbow(rate2) # Fade through the colors of the rainbow at the given rate.  Oooooh, pretty!
time.sleep(1)
# NOTE: I wrote this whole thing to find out where did the number 57.29578 come from 🤔
# that I found here unexplained (still learning some basic math things):
# http://desktop.arcgis.com/en/arcmap/10.3/tools/spatial-analyst-toolbox/how-aspect-works.htm

# also found this visualization on the way and it's beautiful and related:
# https://en.wikipedia.org/wiki/User:LucasVB/Gallery#/media/File:Circle_radians.gif

# here's the code
import math

def radians_to_degrees(radians):
  """converts radians to degrees."""
  # pi radians = 180 degrees -> 1 radians = 180/pi degrees
  rads_in_degrees = ( 180 / math.pi ) * radians
  return rads_in_degrees
  
def degrees_to_radians(degrees):
  """converts degrees to radians."""
  # pi radians = 180 degrees -> 1 degree = pi/180 radians
  degs_in_rads = ( math.pi / 180 ) * degrees
  return degs_in_rads
  
#print(radians_to_degrees(math.pi))
#print(degrees_to_radians(180))

# And here comes the drumroll... 🥁
# revealing the mystery:
print(radians_to_degrees(1))
print(degrees_to_radians(57.29578))
# oh yes. ❤️ maths.

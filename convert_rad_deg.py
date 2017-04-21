import math

# beautiful: https://en.wikipedia.org/wiki/User:LucasVB/Gallery#/media/File:Circle_radians.gif
def radians_to_degrees(radians):
  """converts radians to degrees."""
  # pi radians = 180 degrees -> 1 radians = 180/pi degrees
  rads_in_degrees = ( 180 / math.pi ) * radians
  return rads_in_degrees

print(radians_to_degrees(math.pi))

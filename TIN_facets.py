# getting some values for a Triangular Irregular Network (TIN)
import math

# corner points (x,y,z)
pt1 = (10, 20, 30)
pt2 = (30, 20, 25)
pt3 = (15, 30, 30)

# general formula for a facet of a TIN
#z(x,y) = b0 + b1 * x + b2 * y

# factors (calculated by hand)
b0 = 30
b1 = -0.25
b2 = 0.125



# how to calculate slope and aspect of the facet

###### SLOPE ######
slope_degrees = math.atan(math.sqrt(b1**2 + b2**2)) * (180/math.pi)

###### ASPECT #1 ######
aspect = (180/math.pi) * math.atan2(b2, -b1)
# convert aspect to compass direction
if aspect < 0:
	aspect_compass = 90.0 - aspect
elif aspect > 90.0:
	aspect_compass = 360.0 - aspect + 90.0
else:
	aspect_compass = 90.0 - aspect

###### ASPECT #2 ######
# a different (correct?) way to calculate the aspect of a facet
# done by consulting the glorious ASPECT QUADRANT (attention, currently buggy!)
# check this: https://answers.yahoo.com/question/index?qid=20070602085404AAPmPow
aspect_new = math.atan(b1 / b2) + 180

print("slope of facet in degrees: {0}".format(slope_degrees))
print("aspect of facet in compass direction: {0}".format(aspect_compass))
print("aspect of facet in compass direction, new calculation: {0}".format(aspect_new))
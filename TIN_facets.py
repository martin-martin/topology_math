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
slope = math.atan(math.sqrt(b1**2 + b2**2))
aspect = 180 - math.atan(b2 / b1) + 90 * (b1 / abs(b1))

print("slope of facet: {0}".format(slope))
print("aspect of facet: {0}".format(aspect))

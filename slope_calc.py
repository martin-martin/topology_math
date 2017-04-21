# calculating slopes in a Raster GIS
import math

# example slope raster with cell size of 10 meters

# 8 | 7 | 6
# ---------
# 7 | 5 | 3
# ---------
# 5 | 3 | 1

cell_size = 10 # meters

row1 = (8, 7, 6)
row2 = (7, 5, 3)
row3 = (5, 3, 1)

row_raster = [row1, row2, row3]

# this allows for the option to calculate the "normal weighted" x and y slopes
# pass the 'flag' as an argument to 'get_weighted_x_y_slopes()'
flag = "normal"


####### PREPARING THE FUNCTIONS #######

def get_columns(raster):
	"""extracts column values from rows"""

	col1 = (raster[0][0], raster[1][0], raster[2][0])
	col2 = (raster[0][1], raster[1][1], raster[2][1])
	col3 = (raster[0][2], raster[1][2], raster[2][2])
	col_raster = [col1, col2, col3]
	return col_raster


def get_weighted_slope(raster):
	# each farthest distance in the window in the x-direction, the center one weighted twice
	# (because closer to the center - a more accurate version further down)
	# -------------------------(divided by)--------------------------------
	# the distance traveled from the beginning cell to the end cell (here always 2)
	slope = ( (raster[0][0] - raster[0][2]) +
				math.sqrt(2) * (raster[1][0] - raster[1][2]) +
				(raster[2][0] - raster[2][2])
				) / (2 + (2 * math.sqrt(2)) + 2.0) # floating it for accuracy
	return slope


def get_nw_slope(raster):
	# each farthest distance in the window in the x-direction, the center one weighted sqrt(2)
	# (because closer to the center point it receives more weight)
	# -------------------------(divided by)--------------------------------
	# the distance traveled from the beginning cell to the end cell
	slope = ( (raster[0][0] - raster[0][2]) +
				(raster[1][0] - raster[1][2]) +
				(raster[1][0] - raster[1][2]) +
				(raster[2][0] - raster[2][2])
				) / (2 + 2 + 2 + 2.0) # floating it for accuracy
	return slope


def get_weighted_x_y_slopes(row_raster, col_raster, cell_size, *args):
	"""wrapper function to calculate the slope per meter in both x and y direction"""

	if "normal" in args:
		x_slope = get_nw_slope(row_raster)
		y_slope = get_nw_slope(col_raster)
	else:
		x_slope = get_weighted_slope(row_raster)
		y_slope = get_weighted_slope(col_raster)

	# real slopes (slope per meter) need to take the cell size into consideration
	real_x_slope = x_slope / cell_size
	real_y_slope = y_slope / cell_size

	# uncomment here to see them displayed in percentages
	#print(real_x_slope * 100, real_y_slope * 100)
	return real_x_slope, real_y_slope


def get_total_slope(real_x_slope, real_y_slope):
	"""combines x and y slopes."""

	# to get the real total slope we combine x and y slope using pythagoras' theorem
	slope = math.sqrt(real_x_slope**2 + real_y_slope**2)
	return slope


####### CALCULATING THE SLOPES #######

# first we need the columns represented in the same way as the rows
col_raster = get_columns(row_raster)

# calculating the normal weighted slope
nw_real_x_slope, nw_real_y_slope = get_weighted_x_y_slopes(row_raster, col_raster, cell_size, flag) # specifying I want 'normal weighting'
nw_slope = get_total_slope(nw_real_x_slope, nw_real_y_slope)

# calculating the sqrt(2) weighted slope
real_x_slope, real_y_slope = get_weighted_x_y_slopes(row_raster, col_raster, cell_size) # omitting the flag
slope = get_total_slope(real_x_slope, real_y_slope)

print("the (normal weighted) slope at the example point is {} %".format(nw_slope * 100)) # in percentages
print("the slope at the example point is {} %".format(slope * 100)) # in percentages
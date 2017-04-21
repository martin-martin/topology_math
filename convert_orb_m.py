def seconds_in_meter(orbit_in_meters, arc_seconds):
  """converts arc seconds to their equivalent in meters, given a defined orbit."""
  # 1 orbit = 360 degrees = 21600 arc minutes = 1296000 arc seconds
  # arc seconds -> orbit:
  arc_sec_orb = float(arc_seconds) / 60 / 60 / 360
  arc_sec_m = arc_sec_orb * orbit_in_meters
  return arc_sec_m
  
one_orbit = 40000 * 1000 # km to meters
arc_seconds = 3

sec_in_m = seconds_in_meter(one_orbit, arc_seconds)
print('{:.2f} meters'.format(sec_in_m))

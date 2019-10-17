#  2.8.2.py
# lat 40.59, 40.52, 40.621, 40.519, 40.56, 41.265, 40.61, 40.806, 41.259, 41.265, 41.264, 41.264, 41.259, 41.262, 41.263
# lon 69.532, 69.419, 69.354, 69.263, 69.478, 70.805, 69.706, 70.331, 70.815, 70.823, 70.815, 70.81, 70.824, 70.811, 70.811


lat = input("Enter lats: ")
lon = input("Enter lons: ")

lat_list = [float(s) for s in lat.split(',')]
lon_list = [float(s) for s in lon.split(',')]

print(lat_list)
print(lon_list)

print ("Farthest North = " + str(max (lat_list)))
print ("Farthest West = " + str (max(lon_list)))
print ("Farthest South = " + str(min (lat_list)))
print ("Farthest East = " + str (min(lon_list)))

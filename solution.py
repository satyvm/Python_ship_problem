import numpy as np
# A seperate function is needed for poly_area function


def unit_normal(a, b, c):
    x = np.linalg.det([[1, a[1], a[2]],
                       [1, b[1], b[2]],
                       [1, c[1], c[2]]])
    y = np.linalg.det([[a[0], 1, a[2]],
                       [b[0], 1, b[2]],
                       [c[0], 1, c[2]]])
    z = np.linalg.det([[a[0], a[1], 1],
                       [b[0], b[1], 1],
                       [c[0], c[1], 1]])
    magnitude = (x**2 + y**2 + z**2)**.5
    return (x/magnitude, y/magnitude, z/magnitude)


# Area of polygon with x, y, z coordinates


def poly_area(poly):
    if len(poly) < 3:
        return 0
    elif (len(poly) == 3 and np.all(poly[1] == poly[2])):
        return 0
    total = [0, 0, 0]
    N = len(poly)
    for i in range(N):
        vi1 = poly[i]
        vi2 = poly[(i+1) % N]
        prod = np.cross(vi1, vi2)
        total[0] += prod[0]
        total[1] += prod[1]
        total[2] += prod[2]
    result = np.dot(total, unit_normal(poly[0], poly[1], poly[2]))
    return abs(result/2)


final_array = np.zeros([1, 3], dtype=np.float64)
uw_total_area = 0
wp_total_area = 0
# Started to read the file
with open('./Underwater_Ship.GDF') as f:
    for i in range(0, 4):
        line = f.readline()
    for j in range(0, 1847):
        uw_array_bin = np.zeros([1, 3], dtype=np.float64)
        wp_array_bin = uw_array_bin.copy()
        for i in range(0, 4):
            # Reading the file line by line
            line = f.readline()
            # Splitting the string we got into an array
            array_bin = np.array(line.split(' '))
            # Deleting empty data in the numpy array
            array_bin = np.delete(array_bin, np.where(array_bin == ''))
            # Making it a float numpy array
            array_bin = array_bin.astype(np.float64)
            # Array to calculate underwater surface area from
            uw_array_bin = np.concatenate((uw_array_bin, [array_bin]), axis=0)
            # This is to get points coordinates when z=0
            if(array_bin[2] == 0):
                # Array to calculate waterplane area from
                wp_array_bin = np.concatenate(
                    (wp_array_bin, [array_bin]), axis=0)
        # Deleting the zero row from underwater area calculating array
        uw_array_bin = np.delete(uw_array_bin, [0], axis=0)
        # The total underwater surface area
        uw_total_area += poly_area(uw_array_bin)
        # The total waterplane area
        wp_total_area += poly_area(wp_array_bin)

# Total area came as 9483.598669447189 when I calculated
print(f"The underwater surface area is {uw_total_area}")

# Waterplane area came as 3397.189756668803 when I calculated
print(f"The waterplane area of the ship is {wp_total_area}")

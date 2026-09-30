coord1 = int(input()), int(input())
coord2 = int(input()), int(input())
dist_x = coord1[0] - coord2[0] if coord1[0] > coord2[0] else coord2[0] - coord1[0]
dist_y = coord1[1] - coord2[1] if coord1[1] > coord2[1] else coord2[1] - coord1[1]
print(dist_x)
print(dist_y)
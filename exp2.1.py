def Z(x1, x2):
    return 3*x1 + 2*x2
feasible_points = []
for x1 in range(0, 5):
    for x2 in range(0, 5):
        if (x1 + x2 <= 4) and (x1 <= 2) and (x2 <= 3):
            feasible_points.append((x1, x2, Z(x1, x2)))
print("Basic Feasible Solutions (x1, x2, Z):")
for point in feasible_points:
    print(point)
max_Z = -1
optimal_point = None
for point in feasible_points:
    x1, x2, value = point
    if value > max_Z:
        max_Z = value
        optimal_point = (x1, x2)

print("\nOptimal Solution:")
print("x1 =", optimal_point[0])
print("x2 =", optimal_point[1])
print("Maximum Z =", max_Z)

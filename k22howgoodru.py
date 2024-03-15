def better_than_average(class_points, your_points):
    # 1. sum points
    # 2. / points qty
    # 3. return ur points > avg
    avg = sum(class_points) / len(class_points)
    return your_points > avg


print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 55))
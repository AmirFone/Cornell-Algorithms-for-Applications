import math
import random

# Function to calculate distance
def get_distance(point1, point2):
    return math.sqrt(((point1[0]-point2[0])**2) + ((point1[1]-point2[1])**2))

def closest_pair(points):
    # random.seed(1)
    random.shuffle(points)

    p1 = points[0]
    p2 = points[1]
    delta = get_distance(p1, p2)
    pair = {tuple(p1), tuple(p2)}

    buckets = {}
    # Initialize the buckets with p1 and p2
    for point in [p1, p2]:
        x, y = int(point[0] // 1), int(point[1] // 1)
        bucket_coordinates = (x, y)
        if bucket_coordinates not in buckets:
            buckets[bucket_coordinates] = set()
        buckets[bucket_coordinates].add(tuple(point))

    for point in points[2:]:
        x = int(point[0]//1); y = int(point[1]//1)
        indices = [(a, b) for a in [x-1, x, x+1] for b in [y-1, y, y+1]]
        for dx, dy in indices:
            if (dx, dy) in buckets:
                for neighbor in buckets[(dx, dy)]:
                    d = get_distance(list(neighbor), point)
                    if d < delta:
                        delta = d
                        pair = {tuple(neighbor), tuple(point)}
        if (x,y) not in buckets:
            buckets[(x, y)] = set()
        buckets[(x, y)].add(tuple(point))

    return pair

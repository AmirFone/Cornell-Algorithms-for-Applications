import math
import random

# Function to calculate distance
def get_distance(point1, point2):
    return math.sqrt(((point1[0]-point2[0])**2) + ((point1[1]-point2[1])**2))

def closest_pair(points):
    random.seed(1)
    random.shuffle(points)

    p1 = points[0]
    p2 = points[1]
    delta = get_distance(p1, p2)
    pair = {tuple(p1), tuple(p2)}

    # Use a dict to store bucketed points
    buckets = {(p1[0]//1, p1[1]//1): {tuple(p1)}, (p2[0]//1, p2[1]//1): {tuple(p2)}}

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

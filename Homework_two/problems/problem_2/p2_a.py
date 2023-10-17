'''
Problem 2a
'''

import math

def d(point1, point2): return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def closest_pair(points):
    min = float('inf')
    closest = []
    for i in range(len(points) - 1):
        for j in range(i+1, len(points)):
            dis = d(points[i], points[j])
            if dis < min:
                min = dis
                closest = [tuple(points[i]), tuple(points[j])]
    return closest

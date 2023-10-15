import math
import random

def d(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def closest_pair(points):

    # Brute force method
    def brute(points):
        min_distance = float('inf')
        closest = []
        for i in range(len(points) - 1):
            for j in range(i+1, len(points)):
                distance = d(points[i], points[j])
                if distance < min_distance:
                    min_distance = distance
                    closest = [points[i],points[j]]
        return closest

    # Select random pivot for quicksort
    def random_pivot(pts):
        pivot = random.choice(pts)
        below = [point for point in pts if point < pivot]
        above = [point for point in pts if point > pivot]
        return below, pivot, above

    # Quicksort
    def quicksort(pts):
        if len(pts) <= 1:
            return pts
        below, pivot, above = random_pivot(pts)
        return quicksort(below) + [pivot] + quicksort(above)

    # Sort points by x-coord 
    points = quicksort(points)

    def divide_conquer(pts):

        if len(pts) <= 3:
            return brute(pts)

        mid = len(pts) // 2
        mid_point = pts[mid]
        
        left = pts[:mid]
        right = pts[mid:]
        
        closest_pair = min(divide_conquer(left), divide_conquer(right), key = lambda x: d(*x))

        strip = [point for point in pts if abs(point[0] - mid_point[0]) < d(*closest_pair)] 

        strip.sort(key = lambda x: x[1]) # sort by y-coordinate
        
        min_distance_so_far = d(*closest_pair)
        
        for i, point in enumerate(strip):
            for j in range(i+1, min(i+7, len(strip))): # Only check next 7 points
                if strip[j][1] - strip[i][1] < min_distance_so_far:
                    min_distance_so_far = d(strip[i], strip[j])
                    closest_pair = (strip[i], strip[j])

        return closest_pair

    return divide_conquer(points)
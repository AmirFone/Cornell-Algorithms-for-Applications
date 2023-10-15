'''
Problem 2b
'''

import math

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

	# Sort points by x-coord 
    points.sort()
    
    def divide_conquer(pts):
        # using brute force method when size less <= three
        if len(pts) <= 3:
            return brute(pts)
                    
        mid = len(pts) // 2
        mid_point = pts[mid]
        
        left = pts[:mid]
        right = pts[mid:]
        
        # Calculating the closest pairs for the left and right sides
        closest_in_left = divide_conquer(left)
        closest_in_right = divide_conquer(right)

        # Calculating the distances for the closest pairs
        distance_left = d(*closest_in_left)
        distance_right = d(*closest_in_right)

        # the pair with the smaller distance
        if distance_left < distance_right:
            closest_pair = closest_in_left
        else:
            closest_pair = closest_in_right
        
        strip = []
        for point in pts:
            if abs(point[0] - mid_point[0]) < d(closest_pair[0], closest_pair[1]):
                strip.append(point)
        
        strip.sort(key = lambda x: x[1]) # sort by y-coordinate
        
        min_distance_so_far = d(*closest_pair)
        
        for i, point in enumerate(strip):
            for j in range(i+1, min(i+7, len(strip))): # Only check next 7 points
                if strip[j][1] - strip[i][1] < min_distance_so_far:
                    min_distance_so_far = d(strip[i], strip[j])
                    closest_pair = (strip[i], strip[j])
            
        return closest_pair
    
    return divide_conquer(points)
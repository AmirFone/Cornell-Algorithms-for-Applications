'''
Problem 2b
'''

import math

def d(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def closest_pair(points):
    
    # Brute force is used when the size of the input is small
    def brute(points):
        min = float('inf')
        closest = []
        for i in range(len(points) - 1):
            for j in range(i+1, len(points)):
                dis = d(points[i], points[j])
                if dis < min:
                    min = dis
                    closest = [points[i], points[j]]
        return closest
	# Sort points by x-coord 
    points.sort()
    
    def divide_conquer(p):
        # using brute force method when size less <= 3
        if len(p) <= 3:
            return brute(p)
                    
        mid = len(p) // 2
        mid_point = p[mid]
        
        left = p[:mid]
        right = p[mid:]
        
        # Calculating the closest pairs for the left and right sides
        closest_left = divide_conquer(left)
        closest_right = divide_conquer(right)

        # Calculating the distances for the closest pairs
        distance_left = d(*closest_left)
        distance_right = d(*closest_right)

        # swap 
        if distance_left < distance_right:
            closest_pair = closest_left
        else:
            closest_pair = closest_right
        
        strip = []
        for point in p:
            if abs(point[0] - mid_point[0]) < d(closest_pair[0], closest_pair[1]):
                strip.append(point)
        
        # sort by y  ex: p[x,y] 
        strip.sort(key = lambda x: x[1]) 
        
        new_dis = d(*closest_pair)
        
        for i, point in enumerate(strip):
            for j in range(i+1, min(i+7, len(strip))): # Only check next 7 points
                if strip[j][1] - strip[i][1] < new_dis:
                    new_dis = d(strip[i], strip[j])
                    closest_pair = (strip[i], strip[j])
            
        return closest_pair
    
    return divide_conquer(points)
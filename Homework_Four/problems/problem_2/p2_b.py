def find_binary_search(boxes, package):
    left, right = 0, len(boxes) - 1
    best_fit = float('inf')
    
    while left <= right:
        mid = left + (right - left) // 2
        if boxes[mid] >= package:
            best_fit = boxes[mid]
            right = mid - 1
        else:
            left = mid + 1
    
    return best_fit if best_fit != float('inf') else None

# Function to compute the total waste for all packages using one supplier's boxes
def compute_total_waste(packages, boxes):
    total_waste = 0
    for package in packages:
        best_box = find_binary_search(boxes, package)
        if best_box is None:  # If no box can fit the package
            return float('inf')  # This supplier cannot be used
        total_waste += best_box - package
    return total_waste

# Function to find the supplier with the minimum total waste
def binary_search(packages, suppliers):
    min_waste = float('inf')
    best_supplier_index = -1
    
    for index, boxes in enumerate(suppliers):
        # Ensure the boxes are sorted for binary search
        sorted_boxes = sorted(boxes)
        waste = compute_total_waste(packages, sorted_boxes)
        if waste < min_waste:
            min_waste = waste
            best_supplier_index = index
            
    return min_waste if min_waste != float('inf') else -1
def linear_search(packages, suppliers):
    # Initialize the minimum waste to a large number and the best supplier index
    min_waste = float('inf')
    best_supplier = -1
    
    # Iterate through each supplier
    for supplier_index, boxes in enumerate(suppliers):
        # Initialize total waste for this supplier
        total_waste = 0
        
        # For each package, find the best box
        for package in packages:
            # Find the box that fits the package with minimum waste
            waste = float('inf')
            for box in boxes:
                if box >= package:
                    waste = min(waste, box - package)
            
            # If no box can fit the package, this supplier cannot be chosen
            if waste == float('inf'):
                total_waste = float('inf')
                break
            
            # Add the waste for this package to the total waste
            total_waste += waste
        
        # Check if this supplier is the best so far
        if total_waste < min_waste:
            min_waste = total_waste
            best_supplier = supplier_index
    
    if min_waste==float('inf'): min_waste=-1
    return min_waste
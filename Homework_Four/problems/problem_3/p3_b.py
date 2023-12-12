def calculate_cost(cost_matrix, sequence):
    cost = 0
    for i in range(len(sequence) - 1):
        # Convert 1-based indices to 0-based indices
        cost += cost_matrix[sequence[i] - 1][sequence[i + 1] - 1]
    return cost

def local_search_2opt(cost_matrix, candidate):
    candidate = list(candidate)  # Convert tuple to list for mutability
    improved = True
    while improved:
        improved = False
        best_cost = calculate_cost(cost_matrix, candidate)

        for i in range(len(candidate) - 1):
            for j in range(i + 1, len(candidate)):
                new_candidate = candidate[:]
                # Reversed returns an iterator, convert it to a list
                new_candidate[i:j + 1] = list(reversed(new_candidate[i:j + 1]))
                new_cost = calculate_cost(cost_matrix, new_candidate)

                if new_cost < best_cost:
                    candidate = new_candidate
                    best_cost = new_cost
                    improved = True

    return tuple(candidate[::-1])  # Convert back to tuple to match test expectation

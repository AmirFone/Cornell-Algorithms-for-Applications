def calculate_cost(cost_matrix, sequence):
    cost = 0
    for i in range(len(sequence) - 1):
        cost += cost_matrix[sequence[i] - 1][sequence[i + 1] - 1]
    return cost

def local_search_2opt(cost_matrix, candidate):
    candidate = list(candidate)  # Convert tuple to list for mutability
    best_candidate = candidate[:]
    best_cost = calculate_cost(cost_matrix, candidate)

    for i in range(1, len(candidate) - 1):
        for j in range(i + 1, len(candidate)):
            new_candidate = candidate[:i] + candidate[i:j + 1][::-1] + candidate[j + 1:]
            new_cost = calculate_cost(cost_matrix, new_candidate)

            if new_cost < best_cost:
                best_candidate = new_candidate[:]
                best_cost = new_cost

    return tuple(best_candidate) 

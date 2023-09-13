def manage_queue(operations):
    """
    Manage a queue system for a customer service desk.
    
    The queue is represented as a list where the first element is the first person in line. 
    Implement the following operations:
    - Enqueue: Add a person to the end of the queue.
    - Dequeue: Remove and return the name of the first person in line.
    - Remove Person: Given a person's name, remove them from the queue.
    - Jump the Queue: A person has a quick question and is allowed to jump to the front of the queue, 
      but not in front of the very first person.
    
    Parameters:
    - operations (list): A list of tuples where the first element of each tuple is the operation 
      (either "enqueue", "dequeue", "remove", or "jump") and the second element (if applicable) is the person's name.
    
    Returns:
    - list: The state of the queue after performing all the operations.
    
    Example:
    
    Input: 
    [("enqueue", "Alice"), ("enqueue", "Bob"), ("enqueue", "Charlie"), ("dequeue",), ("jump", "Eve"), ("remove", "Bob")]
    
    Output:
    ["Eve", "Charlie"]
    """
    queue = []
    while operations:
        curr = operations.pop(0)
        if curr[0] == "enqueue":
            queue.append(curr[1])
        elif curr[0] == "dequeue":
            if queue:
                queue.pop(0)
        elif curr[0] == "remove":
            name_to_remove = curr[1]
            queue = [name for name in queue if name != name_to_remove]
        elif curr[0] == "jump":
            if queue:
                first = queue.pop(0)
                jump_name = curr[1]
                queue.insert(1, jump_name)
                queue.insert(0, first)
    return queue

def factorial_dp(n, memo={}):
    """
    Returns the factorial of n using dynamic programming (memoization).
    """
    def helper(n):
        if n == 0:
            return 1
        elif n in memo:
            return memo[n]
        else:
            memo[n] = n * helper(n-1)
            return memo[n]
    return helper(n)

def linear_search(lst, target):
    """
    Perform a linear search on the list to find the index of the target element.

    Parameters:
    - lst (list): A list of elements.
    - target: The element to search for.

    Returns:
    - int: The index of the target element if found, otherwise -1.
    """

    for indx, elem in enumerate(lst):
        if elem == target:
            return indx
    else:
        return -1

def binary_search(lst, target):
    """
    Perform a binary search on the sorted list to find the index of the target element.

    Parameters:
    - lst (list): A sorted list of elements.
    - target: The element to search for.

    Returns:
    - int: The index of the target element if found, otherwise -1.
    """
    def helper(lst, target, start, end):
        if start > end:
            return -1
        mid = (start + end) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            return helper(lst, target, start, mid-1)
        else:
            return helper(lst, target, mid+1, end)
    return helper(lst, target, 0, len(lst)-1)
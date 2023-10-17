import random
import time
import matplotlib.pyplot as plt
from p3_a import LinkedList  # Import your LinkedList implementation
from p3_b import SkipList    # Import your SkipList implementation

def generate_random_coordinates_list(size):
    coordinates_list = [random.uniform(0, 100) for _ in range(size)]
    return coordinates_list

def test_insertion_runtimes():
    test_case_n = [10, 50, 100, 250, 500, 1000, 2500, 5000, 10000, 15000]
    
    insertion_times_linked_list = []
    insertion_times_skip_list = []
    
    for n in test_case_n:
        coordinates = generate_random_coordinates_list(n)
        
        # Measure insertion time for LinkedList
        start_time = time.time()
        linked_list = LinkedList()
        for coordinate in coordinates:
            linked_list.insert(coordinate)
        end_time = time.time()
        insertion_times_linked_list.append(end_time - start_time)
        
        # Measure insertion time for SkipList
        start_time = time.time()
        skip_list =SkipList(8, 0.5)
        for coordinate in coordinates:
            skip_list.insert(coordinate)
        end_time = time.time()
        insertion_times_skip_list.append(end_time - start_time)
    
    # Plot the results
    plt.plot(test_case_n, insertion_times_linked_list, label='LinkedList')
    plt.plot(test_case_n, insertion_times_skip_list, label='SkipList')
    plt.xlabel('Number of Insertions (n)')
    plt.ylabel('Insertion Time (seconds)')
    plt.legend()
    plt.title('Empirical Analysis of Insertion in Skip Lists vs. LinkedList')
    plt.show()

if __name__ == "__main__":
    test_insertion_runtimes()

import random
import time
import matplotlib.pyplot as plt
from p3_a import LinkedList  # Import your LinkedList implementation
from p3_b import SkipList    # Import your SkipList implementation

def generate_random_coordinates_list(size):
    coordinates_list = [random.uniform(0, 100) for _ in range(size)]
    return coordinates_list

def test_search_runtimes():
    test_case_n = [10, 50, 100, 250, 500, 1000, 2500, 5000, 10000, 15000]
    
    search_times_linked_list = []
    search_times_skip_list = []
    
    for n in test_case_n:
        # Generate a list of random coordinates for searching
        coordinates = generate_random_coordinates_list(n)
        
        # Create a LinkedList and insert the coordinates
        linked_list = LinkedList()
        for coordinate in coordinates:
            linked_list.insert(coordinate)
        
        # Create a SkipList and insert the coordinates
        skip_list = SkipList(8, 0.5)
        for coordinate in coordinates:
            skip_list.insert(coordinate)
        
        # Measure search time for LinkedList
        start_time = time.time()
        for coordinate in coordinates:
            linked_list.search(coordinate)
        end_time = time.time()
        search_times_linked_list.append(end_time - start_time)
        
        # Measure search time for SkipList
        start_time = time.time()
        for coordinate in coordinates:
            skip_list.search(coordinate)
        end_time = time.time()
        search_times_skip_list.append(end_time - start_time)
    
    # Plot the results
    plt.plot(test_case_n, search_times_linked_list, label='LinkedList')
    plt.plot(test_case_n, search_times_skip_list, label='SkipList')
    plt.xlabel('Number of Searches (n)')
    plt.ylabel('Search Time (seconds)')
    plt.legend()
    plt.title('Search Runtimes for LinkedList and SkipList')
    plt.show()

if __name__ == "__main__":
    test_search_runtimes()

import random
import time
import matplotlib.pyplot as plt
from p3_a import LinkedList  # Import your LinkedList implementation
from p3_b import SkipList    # Import your SkipList implementation

def generate_random_coordinates_list(size):
    coordinates_list = [random.uniform(0, 100) for _ in range(size)]
    return coordinates_list

def test_deletion_runtimes():
    test_case_n = [10, 50, 100, 250, 500, 1000, 2500, 5000, 10000, 15000]
    
    deletion_times_linked_list = []
    deletion_times_skip_list = []
    
    for n in test_case_n:
        # Generate a list of random coordinates for deletion
        coordinates = generate_random_coordinates_list(n)
        
        # Create a LinkedList and insert the coordinates
        linked_list = LinkedList()
        for coordinate in coordinates:
            linked_list.insert(coordinate)
        
        # Create a SkipList and insert the coordinates
        skip_list = SkipList(70, 0.5)
        for coordinate in coordinates:
            skip_list.insert(coordinate)
        
        # Measure deletion time for LinkedList
        start_time = time.time()
        for coordinate in coordinates:
            linked_list.delete(coordinate)
        end_time = time.time()
        deletion_times_linked_list.append(end_time - start_time)
        
        # Measure deletion time for SkipList
        start_time = time.time()
        for coordinate in coordinates:
            skip_list.delete(coordinate)
        end_time = time.time()
        deletion_times_skip_list.append(end_time - start_time)
    
    # Plot the results
    plt.plot(test_case_n, deletion_times_linked_list, label='LinkedList')
    plt.plot(test_case_n, deletion_times_skip_list, label='SkipList')
    plt.xlabel('Number of Deletions (n)')
    plt.ylabel('Deletion Time (seconds)')
    plt.legend()
    plt.title('Deletion Runtimes for LinkedList and SkipList')
    plt.show()

if __name__ == "__main__":
    test_deletion_runtimes()



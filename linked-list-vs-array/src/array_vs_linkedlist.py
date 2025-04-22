import time
import sys
import random
from linked_list import LinkedList

def measure_insertion_array(size):
    arr = []
    start_time = time.time()
    for i in range(size):
        arr.append(i)
    elapsed_time = time.time() - start_time
    memory_usage = sys.getsizeof(arr)
    return elapsed_time, memory_usage

def measure_insertion_linked_list(size, LinkedList):
    linked_list = LinkedList()
    start_time = time.time()
    for i in range(size):
        linked_list.append(i)
    elapsed_time = time.time() - start_time
    memory_usage = sys.getsizeof(linked_list)
    return elapsed_time, memory_usage

def measure_deletion_array(arr):
    start_time = time.time()
    if arr:
        arr.pop()
    elapsed_time = time.time() - start_time
    memory_usage = sys.getsizeof(arr)
    return elapsed_time, memory_usage

def measure_deletion_linked_list(linked_list):
    start_time = time.time()
    linked_list.pop()
    elapsed_time = time.time() - start_time
    memory_usage = sys.getsizeof(linked_list)
    return elapsed_time, memory_usage

def measure_traversal_array(arr):
    start_time = time.time()
    for item in arr:
        pass
    elapsed_time = time.time() - start_time
    return elapsed_time

def measure_traversal_linked_list(linked_list):
    start_time = time.time()
    current = linked_list.head
    while current:
        current = current.next
    elapsed_time = time.time() - start_time
    return elapsed_time

def compare_performance(size, LinkedList):
    print(f"Comparing performance for size: {size}")

    # Measure insertion
    array_insertion_time, array_memory = measure_insertion_array(size)
    linked_list_insertion_time, linked_list_memory = measure_insertion_linked_list(size, LinkedList)

    print(f"Array Insertion Time: {array_insertion_time:.6f}s, Memory Usage: {array_memory} bytes")
    print(f"Linked List Insertion Time: {linked_list_insertion_time:.6f}s, Memory Usage: {linked_list_memory} bytes")

    # Measure deletion
    arr = list(range(size))
    linked_list = LinkedList()
    for i in range(size):
        linked_list.append(i)

    array_deletion_time, array_memory = measure_deletion_array(arr)
    linked_list_deletion_time, linked_list_memory = measure_deletion_linked_list(linked_list)

    print(f"Array Deletion Time: {array_deletion_time:.6f}s, Memory Usage: {array_memory} bytes")
    print(f"Linked List Deletion Time: {linked_list_deletion_time:.6f}s, Memory Usage: {linked_list_memory} bytes")

    # Measure traversal
    array_traversal_time = measure_traversal_array(arr)
    linked_list_traversal_time = measure_traversal_linked_list(linked_list)

    print(f"Array Traversal Time: {array_traversal_time:.6f}s")
    print(f"Linked List Traversal Time: {linked_list_traversal_time:.6f}s")

    return array_traversal_time, linked_list_traversal_time


if __name__ == "__main__":
    size = 100000  # Adjust the size as needed
    from linked_list import LinkedList
    array_traversal_time, linked_list_traversal_time = compare_performance(size, LinkedList)
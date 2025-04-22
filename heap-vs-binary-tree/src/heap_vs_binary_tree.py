import time
import sys
import random
from binary_tree import BinaryTree
from heap import Heap

def measure_insertion_binary_tree(size):
    tree = BinaryTree()
    values = list(range(size))
    random.shuffle(values)  # 👈 Shuffle to prevent unbalanced tree
    start_time = time.time()
    for i in values:
        tree.insert(i)
    elapsed_time = time.time() - start_time
    memory_usage = sys.getsizeof(tree)
    return elapsed_time, memory_usage

def measure_insertion_heap(size):
    heap = Heap()
    start_time = time.time()
    for i in range(size):
        heap.insert(i)
    elapsed_time = time.time() - start_time
    memory_usage = sys.getsizeof(heap)
    return elapsed_time, memory_usage

def measure_deletion_binary_tree(tree, key):
    start_time = time.time()
    tree.delete(key)
    elapsed_time = time.time() - start_time
    memory_usage = sys.getsizeof(tree)
    return elapsed_time, memory_usage

def measure_deletion_heap(heap):
    start_time = time.time()
    heap.delete()
    elapsed_time = time.time() - start_time
    memory_usage = sys.getsizeof(heap)
    return elapsed_time, memory_usage

def measure_traversal_binary_tree(tree):
    start_time = time.time()
    tree.traverse_in_order(tree.root)
    elapsed_time = time.time() - start_time
    return elapsed_time

def measure_traversal_heap(heap):
    start_time = time.time()
    heap.traverse()
    elapsed_time = time.time() - start_time
    return elapsed_time

def compare_performance(size):
    print(f"\nComparing Heap vs Binary Tree for size: {size}")

    # Insertion
    heap_insertion_time, heap_mem = measure_insertion_heap(size)
    tree_insertion_time, tree_mem = measure_insertion_binary_tree(size)

    print(f"Heap Insertion Time: {heap_insertion_time:.6f}s, Memory: {heap_mem} bytes")
    print(f"Tree Insertion Time: {tree_insertion_time:.6f}s, Memory: {tree_mem} bytes")

    # Prepare structures for deletion and traversal
    heap = Heap()
    tree = BinaryTree()
    values = list(range(size))
    random.shuffle(values)  # 👈 Shuffle again for realistic tree structure
    for i in values:
        tree.insert(i)
        heap.insert(i)

    # Deletion
    heap_deletion_time, heap_mem = measure_deletion_heap(heap)
    tree_deletion_time, tree_mem = measure_deletion_binary_tree(tree, values[size // 2])  # Delete middle value

    print(f"Heap Deletion Time: {heap_deletion_time:.6f}s, Memory: {heap_mem} bytes")
    print(f"Tree Deletion Time: {tree_deletion_time:.6f}s, Memory: {tree_mem} bytes")

    # Traversal
    heap_traversal_time = measure_traversal_heap(heap)
    tree_traversal_time = measure_traversal_binary_tree(tree)

    print(f"Heap Traversal Time: {heap_traversal_time:.6f}s")
    print(f"Tree Traversal Time: {tree_traversal_time:.6f}s")

if __name__ == "__main__":
    compare_performance(10000000)

import unittest
import time
import sys
from src.array_vs_linkedlist import compare_performance
from src.linked_list import LinkedList

class TestArrayVsLinkedList(unittest.TestCase):

    def setUp(self):
        self.array_size = 1000
        self.linked_list = LinkedList()
        for i in range(self.array_size):
            self.linked_list.append(i)
        self.array = list(range(self.array_size))

    def test_array_insertion_time(self):
        start_time = time.time()
        self.array.append(self.array_size)
        elapsed_time = time.time() - start_time
        print(f"Array insertion time: {elapsed_time:.6f} seconds")

    def test_linked_list_insertion_time(self):
        start_time = time.time()
        self.linked_list.append(self.array_size)
        elapsed_time = time.time() - start_time
        print(f"Linked List insertion time: {elapsed_time:.6f} seconds")

    def test_array_deletion_time(self):
        start_time = time.time()
        self.array.pop()
        elapsed_time = time.time() - start_time
        print(f"Array deletion time: {elapsed_time:.6f} seconds")

    def test_linked_list_deletion_time(self):
        start_time = time.time()
        self.linked_list.delete(self.array_size - 1)
        elapsed_time = time.time() - start_time
        print(f"Linked List deletion time: {elapsed_time:.6f} seconds")

    def test_memory_usage(self):
        array_memory = sys.getsizeof(self.array)
        linked_list_memory = self.linked_list.memory_usage()
        print(f"Array memory usage: {array_memory} bytes")
        print(f"Linked List memory usage: {linked_list_memory} bytes")

if __name__ == '__main__':
    unittest.main()
import unittest
from binary_tree import BinaryTree
from heap import Heap

class TestBinaryTree(unittest.TestCase):
    def test_insertion(self):
        tree = BinaryTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        self.assertEqual(list(tree.traverse_in_order()), [5, 10, 15])

class TestHeap(unittest.TestCase):
    def test_insertion(self):
        heap = Heap()
        heap.insert(10)
        heap.insert(5)
        heap.insert(15)
        self.assertEqual(heap.traverse(), [5, 10, 15])

if __name__ == "__main__":
    unittest.main()
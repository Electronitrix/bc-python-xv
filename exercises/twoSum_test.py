import unittest
from twoSum import twoSum

class TwoSumTestSuite(unittest.TestCase):
	def test_list_range_4(self):
		result = twoSum([2,5,1,7], 8)
		self.assertEqual(result, [2,3])
	def test_list_range_10(self):
		result = twoSum([4,6,5,13,32,30,2,7,10], 43)
		self.assertEqual(result, [3,5])
	def test_list_range_same(self):
		result = twoSum([4,6,6,6,32,8], 12)
		self.assertEqual(result, [0,5])
	def test_list_range_8(self):
		result = twoSum([3,2,23,43,12,12,54,34], 77)
		self.assertEqual(result, [2,6])
	def test_list_range_7(self):
		result = twoSum([2,1,1,0,7,3,5], 7)
		self.assertEqual(result, [0,6])
	def test_list_range_15(self):
		result = twoSum([32,12,23,12,23,56,45,6534,65,23,23,12,55,12,23], 6557)
		self.assertEqual(result, [2,7])
	def test_list_range_20(self):
	    result = twoSum([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], 37)
	    self.assertEqual(result, [18,19])
	def test_list_range_12(self):
	    result = twoSum([3,6,2,0,23,1,64,32,12,10,19,18], 2)
	    self.assertEqual(result, [2,3])
	def test_list_range_17(self):
		result = twoSum([12,13,14,15,16,17,18,19,34,65,23,23,12,55,12,23,93], 46)
		self.assertEqual(result, [0,8])
	def test_list_range_19(self):
		result = twoSum([2,5,1,7,32,12,23,12,23,56,45,6534,65,23,23,12,55,12,23], 77)
		self.assertEqual(result, [4,10])

# the code helps initialize the program when you are calling from command
# so you do not have to initialize the code
if __name__== "__main__":
	unittest.main()
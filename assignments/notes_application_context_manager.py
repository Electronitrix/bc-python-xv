import sys
from io import StringIO
from contextlib import contextmanager
#import unittest

@contextmanager
def capture(command, *args, **kwargs):
	out, sys.stdout = sys.stdout, StringIO()
	command(*args, **kwargs)
	sys.stdout.seek(0)
	yield sys.stdout.read()
	sys.stdout = out

"""
    The code below was used to test that my contextmanager was working fine
"""


# def printList():
# 	alist = ["Black Justice"]
# 	print ("Note ID: 0")
# 	print (alist[0])

# 	print ("\n\nBy Author Erika")

# class BarTest(unittest.TestCase):
# 	def testAndCapture(self):
# 		with capture(printList) as output:
# 			self.assertEqual("Note ID: 0\nBlack Justice\n\n\nBy Author Erika\n", output)

# test = BarTest()
# test.testAndCapture()
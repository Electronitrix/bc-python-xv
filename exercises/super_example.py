class A(objects):
	def __init__(self):
		pass

	def save(self, param):
		return param

class B(A):
	def save(self, param):
		super(B, self).save(param)
		return param / 2
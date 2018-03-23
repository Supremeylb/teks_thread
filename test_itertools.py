"""
This file is to test itertools module
[description]
"""
import itertools,logging
from functools import cmp_to_key
#from pipe import *
# Amortize a 5% loan of 1000 with 4 annual payments of 90
#get the annual cash flow
cash_flow = [1000,-90,-90,-90,-90]
#print(list(itertools.accumulate(cash_flow,lambda pri,inti:pri*(1+0.05)+inti)))

#-------------------This is known
logistic_map = lambda x,_:  r * x * (1 - x)
#func(total,element) after next the iterable object is incomplete
x0 = 0.4
r = 3.8
x = itertools.repeat(x0,6)

#print(list(itertools.accumulate(x,logistic_map)))
class test_Iter(object):
	"""docstring for test_Iter"""
	def __init__(self):
		super(test_Iter, self).__init__()
		
		
#=====I do not think it can done this task
	def combinations(self,iterable, r):
		pool = tuple(iterable)
		n = len(pool)
		if r > n:
			return
		indices = list(range(r))
		logging.info(tuple(pool[i] for i in indices))
		while True:
			for i in reversed(range(r)):
				if indices[i] != i + n - r:
					break
				else:
					return
				indices[i] += 1
				for j in range(i+1, r):
					indices[j] = indices[j-1] + 1
			logging.info(tuple(pool[i] for i in indices))

	def test_cmp(self,value):
		return sorted(value,key = cmp_to_key(lambda x,y:x-y))
class Fib(object):
	"""doc string for Fib"""
	def __init__(self, a,b):
		self.a = a
		self.b = b
		
	def __iter__(self):
		return self
	def __next__(self):
		self.a,self.b = self.b,self.a + self.b
		if self.b > 100:
			raise StopIteration()
		return self.b
	def __getitem__(self):
		self.a,self.b = self.b,self.a + self.b
		if self.b > 100:
			
		return self.b
if __name__ == '__main__':
	a = test_Iter()
	#a.combinations('ABCD',2)
	#print(a.test_cmp(range(0,4)))
	a = Fib(1,2)
	print(a[1])
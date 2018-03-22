#coding:utf8
"""
This is magic methods about python
"""

#for __init__ and __del__
import os
class test_Del(object):
	"""docstring for test_Magic"""
	"""给文件对象进行包装从而确认在删除时文件流关闭"""
	def __init__(self, filename):
		super(test_Magic, self).__init__()
		self.filename = filename
		self.handler = open(os.path.join(self.getCurPath(),self.filename),"r+")

	def getCurPath(self):    
		cur_path = os.path.dirname(os.path.realpath(__file__))    
		return cur_path
	def _print(self):
		print(self.handler.read())
	def __del__(self):
		self.handler.close()
		del self.handler
	"""相同的操作因为不同的库会使用不同的名字，这样会产生不必要的工作"""
class test_cmp(str):
	"""docstring for test_cmp"""
	"""for str is unchangable so I use __new__"""
	def __new__(self, word):
		if ' ' in word:
			print("Word contains blank space and I will slice the word")
			word = word[:word.index('')]
		return str.__new__(test_cmp,word)
	def __gt__(self,other):
		return (len(self) > len(other))
class test_Bool(object):
	"""docstring for test_Bool"""
	#how to do this?
	def __init__(self,value):
		self.value = value
	def __nonzero__(self):
		if self:
			return "yes"
		else:
			return "no"
"""attr call control """
class Access(object):
	"""docstring for Access"""
	def __init__(self,val):
		super(Access, self).__setattr__('count',0)
		super(Access,self).__setattr__('value',val)

	def __setattr__(self,name,value):
		if name == 'value':
			super(Access,self).__setattr__('count',self.count + 1)
		super(Access,self).__setattr__(name,value)
	def __delattr__(self):
		if name == 'value':
			super(Access,self).__setattr__('count',self.count + 1)
		super(Access,self).__delattr__(name)

		
#============================================
if __name__ == '__main__':
	#test = test_Magic("new.txt")
	#test._print()
	#word1 = test_cmp("fool")
	#word2 = test_cmp("zz")
	#print(word1 > word2)
	a = Access(5)
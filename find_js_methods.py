import urllib,requests
"""search for html/js methods"""
BASE_URL = "http://www.w3school.com.cn/htmldom/met_win_"
class findMethod(object):
	"""docstring for findMethod"""
	def __init__(self, method):
		super(findMethod, self).__init__()
		self.method = method

	def download(self):

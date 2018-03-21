"""
This is recognize .py
"""
import Queue,threading,time
class Recognizer(object):
	"""docstring for Recognizer"""
	def __init__(self):
		super(Recognizer, self).__init__()
		self.result = ""
		self.library = {"teks":1,"go":2,"stay":3}
		self.SHARE = Queue.Queue()

		
	def recognize_google(self,audio,lang='zh'):
		"""
		
		[recognize the words and produce the result]
		
		Arguments:
			audio {[str]} -- [words]
		
		Keyword Arguments:
			lang {str} -- [description] (default: {'zh'})
		"""
		while True:
			message = self.SHARE.get()
			self.result = self.library.get(message,"bye")
			time.sleep(1)
			self.SHARE.task_done()
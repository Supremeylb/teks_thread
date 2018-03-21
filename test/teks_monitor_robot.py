import threading,Queue
from teks_monitor_recognize import Recognizer
class Listener(object):
	def __init__(self,func):
		super(teks_monitor_record,self).__init__()
		self.func = func
		self.sr = Recognizer()
		self.SHARE = Queue.Queue()

	def run(self):
		self.text = raw_input("Please input the index:")
		self.SHARE.put(self.text)
		"""
		thread = threading.Thread(target=self.sr.recognize_google,args=(self.text,))
		thread.start()
		thread.join()
		"""
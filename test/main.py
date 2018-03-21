"""
There are three men——Main、Listener and Recognizer
Main is boss,he has the power to command the other two men work for him.
When the responses returned from the Recognizer are enough,he will say:"Ok, little boys, these are your awards,go home and I will get some sleep"
Listener——he can listen the surroundings and return some messages
Recognizer——he is in charge of handling the messages and return some responses to Main
"""
import threading,Queue
from teks_monitor_robot  import Listener
from teks_monitor_recognize import Recognizer
class Main(object):
	"""docstring for Main"""
	def __init__(self):
		super(Main, self).__init__()
		self.listen = Listener()
		self.recognizer = Recognizer()

	def suspend(self):
		self.suspend_flag = True
	def is_suspend(self):
		return self.suspend_flag
	def main(self):
		self.listen_thread.start()
		self.listen_thread.join()
	def wake_up(self):
		"""		
		[ensure the Listener and Recognizer already to work ]
		"""
		self.listen_thread = threading.Thread(target=self.listen.run,name="listen_thread")
		#after the listener get the message,recognizer go to the table to work
		#after the recognizer has done,the boss says ok,and the listener works again
if __name__ == '__main__':

		
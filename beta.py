import threading

class Set_flag(object):
	def __init__(self):
		threading.Thread.__init__(self)

	def set_flag(self):
		
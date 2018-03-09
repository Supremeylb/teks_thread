#!/usr/bin/env python
#  -*- coding:utf-8 -*-

import time
import threading
import beta

class test_thread(object):
	def __init__(self):
		threading.Thread.__init__(self,rlock)
		self.suspend_flag = False
 		self.thread_rlock = rlock

 	def suspend(self):
 		with self.thread_rlock:
            self.suspend_flag = True

    def resume(self):
        with self.thread_rlock:
            #print('resume google beta')
            self.suspend_flag = False

    def is_suspend(self):
    	return self.suspend_flag

################################################################################
if __name__ == '__main__':
    rlock = threading.RLock()
	record = test_thread(rlock)
    with self.thread_rlock:
        print("now I put 1")
    


	
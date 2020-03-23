#!/usr/bin/python

import threading
import time
 

exitFlag = 0

class myThread (threading.Thread):
   def _init_(self, threadID, name, counter):
      threading.Thread._init_(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print "Starting " + self.name
      print_time(self.name, 5, 500)
      print "Exiting " + self.name

def print_time(threadName, counter, delay):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print "%s: %s" % (threadName, time.ctime(time.time()))
      counter -= 1

# Create new threads
total = 1
thread = [0 for x in range(1000)]
while total<1000:
   thread[total] = myThread(1, "{} and {}".format("Thread - ", total), 1)
   thread[total].start()
   total += 1


print "Exiting Main Thread"

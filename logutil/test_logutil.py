from log_util import Logger
import os
import sys
import pdb
'''
    For test evlogging modules
'''
logName = __file__ + ".log"
def testfunc1():
    loggers = Logger(logName) 
    loggers.info("this is testfunc1")

def testfunc2():
    loggerz = Logger(logName) 
    loggerz.error("this is testfunc2")

if __name__  == '__main__':
   loggers = Logger(logName) 
   loggers.info("This is a %s log"%('info'))
   loggers.debug("This is a %s log"%('debug'))
   loggers.warn("This is a %s log"%('warn'))
   loggers.error("This is a %s log"%('error'))
   #pdb.set_trace()
   testfunc2()
   testfunc1()

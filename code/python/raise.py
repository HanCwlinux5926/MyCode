#! /usr/bin/python
# -*- coding:utf-8 -*-


class WorkerException(RuntimeError):
    def __init__(self, arg):
        self.args = arg

def worker():
    try:
        raise WorkerException("Bad Worker")
    except WorkerException,e:
        print e.args

if __name__ == '__main__':
    worker()

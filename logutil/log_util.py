#! /usr/bin/python
# -*- coding:utf-8 -*-
import os
import logging.handlers
LOGLEVEL=40
class Logger(logging.Logger):
    
    def __init__(self, filename="test.log"):
        self.filename = filename
        super(Logger, self).__init__(self)
        self.mkdirs('./logs')
        self.do_log()

    def mkdirs(self, name):
        '''
        create log path
        '''
        if not os.path.exists(name):
            os.makedirs(name)

    def do_log(self):
        log_path = os.path.join('./logs',self.filename)
        #创建文件handler
        fh = logging.handlers.RotatingFileHandler(log_path, mode='a', maxBytes=1024*1024*10, backupCount=5)  
        fh.setLevel(LOGLEVEL)
        
        ##创建控制台handler
        ch = logging.StreamHandler()
        ch.setLevel(LOGLEVEL)

        ##定义handler的输出格式
        #formatter = logging.Formatter('[%(asctime)s] - %(filename)s [Line:%(lineno)d] - [%(levelname)s]-[thread:%(thread)s]-[process:%(process)s] - %(message)s')
        formatter = logging.Formatter('%(filename)s %(asctime)s %(levelname)s %(funcName)s: [%(lineno)d] %(message)s') 
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        #给logger 添加handler
        self.addHandler(fh)
        self.addHandler(ch)

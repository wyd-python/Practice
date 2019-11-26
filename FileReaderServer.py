# -*- coding: utf-8 -*-

from autobahn.twisted.websocket import WebSocketServerProtocol, \
                                                    WebSocketServerFactory
from autobahn.websocket.protocol import WebSocketProtocol

import sys

from twisted.python import log
from twisted.internet import reactor,task
import io
import os
import json
import psutil
import time
import logging
import fcntl

def lockFile(lockfile):
    fd = os.open(lockfile, os.O_CREAT| os.O_TRUNC | os.O_WRONLY)
    try:
        fcntl.lockf(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except IOError:
        return False

    return True

# http://stackoverflow.com/questions/17757384/call-a-twisted-protocol-method-from-another-thread
class MyServerProtocol(WebSocketServerProtocol):

    def onConnect(self, request):
        print("Client connecting: {0}".format(request.peer))

    def onOpen(self):
        print("WebSocket connection open.")

    def onMessage(self, payload, isBinary):
        if isBinary:
            print("Binary message received: {0} bytes".format(len(payload)))
        else:
            print("Text message received: {0}".format(payload.decode('utf8')))
        try:
            d = json.loads(str(payload))
            
            if d.has_key('pid') and d.has_key('filename'):
                pid = d['pid']
                filename = d['filename']
                if pid < 0 :
                    self.sendClose(3002,u"invalid pid {0}".format(pid))
                    return

            #根据web第一次通讯是否带有read_append字段来决定是否要以append方式来读取 updated by fucan 20150907
            read_all = True
            if d.has_key('read_append'):
                read_all = False
            self.readFile(pid,filename, read_all)

        except ValueError,err:
            self.sendClose(3000,u"failed to json decode [%s]"%str(payload))

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {0}".format(reason))

    #添加read_all参数决定是否要读取整个文件，防止文件过大，updated by fucan 20150907
    def readFile(self,pid,filename,read_all=True):
        if not os.path.exists(filename):
            self.sendClose(3001,u"log file not exits[%s]"%filename)
            return
        f = io.open(filename,'rt',1,'utf-8', 'replace')

        if not read_all:
            f.seek(0, 2) 

        self.loop_reader = task.LoopingCall(self.readLoop,pid,f)
        self.loop_reader.start(0.1)
        
    def readLoop(self,pid,f):

        pid_exists = pid == 0 or psutil.pid_exists(pid)

        #print("pid_exists: {pid_exists}".format(pid_exists=pid_exists))
        s = f.read()
        #print("read text size: {size}".format(size=len(s)))
        if len(s):
            #print("sending text: {text}".format(text=s))
            self.sendMessage(s.encode('utf8'),sync=True,doNotCompress=True)
        elif pid_exists==False:
            # 进程结束了，而且日志也读出不内容了
            #print("stop loop=========================================================================")
            self.loop_reader.stop()
            self.sendClose(1000,u"finished")


if __name__ == '__main__':

    if len(sys.argv) == 2:
        port=int(sys.argv[1])
    else:
        port=9003

    if not lockFile('.filereaderserver.lock.{}'.format(port)):
        exit()

    log.startLogging(sys.stdout)

    factory = WebSocketServerFactory("ws://localhost:{}".format(port), debug = False)
    factory.protocol = MyServerProtocol

    reactor.listenTCP(port, factory)
    reactor.run()

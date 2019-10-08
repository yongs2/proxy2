#!/usr/bin/python
# -*- coding: utf-8 -*-
from proxy2 import *
import datetime

timeout_sec=4

class BilRequestHandler(ProxyRequestHandler):
        def request_handler(self, req, req_body):
                print "1..PATH=" + self.path;
                self.path = self.path.replace('http://10.100.39.113:8080', 'http://192.168.0.198');
                print "2..PATH=" + self.path;
                print "ORG.HOST=" + req.headers['Host']
                print "-------------------------------------------------"
                if self.path.find("getNacdMsgRecvMyDateJson") >= 0 :
                        print "------------------------------------------------- getNacdMsgRecvMyDateJson"
                        now = str(datetime.datetime.now())
                        print "[" + now + "] ----- DELAY : " + str(timeout_sec) + " sec"
                        time.sleep(timeout_sec)
                        now = str(datetime.datetime.now())
                        print "[" + now + "] ----- return"
                        return True;    # Error
                elif self.path.find("getNacdGetNoticeMsgJson") >= 0 :
                        print "------------------------------------------------- getNacdGetNoticeMsgJson"
                        now = str(datetime.datetime.now())
                        print "[" + now + "] ----- DROP : " + str(timeout_sec) + " sec"
                        self.path = ""
                        time.sleep(timeout_sec)
                        now = str(datetime.datetime.now())
                        print "[" + now + "] ----- return"
                        return; # Error
                elif self.path.find("Reject") >= 0:
                        print "------------------------------------------------- Reject"
                        return False;   # 403

if __name__ == '__main__':
        test(HandlerClass=BilRequestHandler)
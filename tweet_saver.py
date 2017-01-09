# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 19:31:28 2016

@author: Shannon
"""
from tweepy import StreamListener
import time

class Tweet_Saver(StreamListener):
    
    def __init__(self, file, end_time):
        self.file = file
        #self.start_time = time.time()
        self.end_time = end_time + time.time()
        open(file, 'w')
        
    def on_data(self, data):
        f = open(self.file, 'a')
        f.write(data.replace('\n', ''))
        if self.end_time > time.time():
            return True
        else:
            return False
        
    def on_error(self, status):
        print(status)
        
    def on_timeout(self):
        print("WE TIMED OUT!")
        return
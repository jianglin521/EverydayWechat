# -*- coding: utf-8 -*-
import sys
import os
 
def app_path(name):
    if getattr(sys, 'frozen', False): #是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, name)

if __name__ == '__main__':
  app_path('test.txt')

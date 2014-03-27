'''
Created on Mar 27, 2014

@author: chanpod
'''

import Command
import Data
import Status

class Bus(object):
    FIRSTINDEX = 0
    bus = []    
    
    def writeBus(self, wordIn = None):        
        try:
            if(wordIn == None):
                raise ValueError
            else:
                if(isinstance(wordIn, (Command, Data, Status))):
                    self.bus.append(wordIn)
                else:
                    raise ValueError
        except ValueError:
            print("Bus.writeBus:  word invalid or ommited.")
    
    def readBus(self):
        word = self.bus.index(self.FIRSTINDEX);
        self.bus.remove(self.FIRSTINDEX)
        return word
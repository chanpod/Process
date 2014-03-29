'''
Created on Mar 27, 2014
LOC: 18
@author: chanpod
'''

from command import Command
from data import Data
from status import Status

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
                    return len(self.bus)
                else:
                    raise ValueError
        except ValueError:
            print("Bus.writeBus:  word invalid or ommited.")
    
    def readBus(self):
        word = self.bus.pop()      
        return word
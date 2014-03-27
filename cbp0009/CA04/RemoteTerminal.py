'''
Created on Mar 27, 2014

@author: chanpod
'''

import Bus

class RemoteTerminal(object):
    
    address = None
    
    def __init__(self, addressIn=None):
        try:
            if(addressIn == None):
                raise ValueError
            else:
                self.address = addressIn
        except ValueError:
            print("RemoteTerminal.init:  Address must be given.")
    
    def readBus(self, busIn = None):
            try:
                if(busIn == None):
                    raise ValueError
                else:
                    if(isinstance(busIn, Bus)):
                        data = busIn.readBus()
                return data
            except ValueError:
                print("RemoteTerminal.readBus:"  
                    "  Bus object not give or not an instance of Bus.")
    def getAddress(self):
        return self.address
        

                     

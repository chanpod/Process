'''
Created on Mar 30, 2014

@author: chanpod
'''
import unittest
from bus import Bus
from status import Status
from data import Data
from command import Command
from remoteterminal import RemoteTerminal

class Test(unittest.TestCase):
    
    

    def test_init(self):
        rt = RemoteTerminal(4)
        self.assertTrue(isinstance(rt, RemoteTerminal),
                        "Object is not of instance RemoteTerminal")
    
    def test_getAddress(self):
        rt = RemoteTerminal(4)
        self.assertEqual(rt.getAddress(), 4,
                         "Not Assigning address correctly.")
    
    def test_readBus(self):
        rt = RemoteTerminal(4)
        data = Data(1)
        bus = Bus()
        bus.writeBus(data)
        bus2 = rt.readBus(bus)
        self.assertTrue(isinstance(bus2, Bus), 
                        "Not assigning")
        
        



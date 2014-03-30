'''
Created on Mar 27, 2014

@author: chanpod
'''
import unittest
from bus import Bus
from status import Status
from data import Data
from command import Command

class BusTest(unittest.TestCase):

    def test_bus(self):
        bus = Bus()
        self.assertTrue(isinstance(bus, Bus), "bus is not an instance of Bus")
        
    def test_writeBus(self):
        bus = Bus()
        status = Status(5)
        self.assertEquals(bus.writeBus(status), 1, 
                          "Not returning the correct number of items in bus.") 
        
    
    def test_readBus(self):
        bus = Bus()
        status = Status(5)
        bus.writeBus(status)
        word = bus.readBus()
        
        self.assertTrue(isinstance(word, (Status, Command, Data)), 
                        "Word is not an instance of Bus, Command, or Data.")



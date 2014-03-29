'''
Created on Mar 29, 2014

@author: chanpod
'''
import unittest
from bus import Bus
from status import Status
from data import Data
from command import Command

class Test(unittest.TestCase):


    def test_init(self):
        data = Data(1)
        self.assertEqual(data.getContent(), 1, 
                         "Payload not being assigned properly.")
        data = Data()
        self.assertEqual(data.getContent(), None,
                         "Payload not being assigned properly.")
    
    def test_setContent(self):
        data = Data()
        
        self.assertEqual(data.setContent(3), 3, 
                         "setContent is not returning the correct number.")
    
    def test_getContent(self):
        data = Data(1)
        self.assertEqual(data.getContent(), 1, 
                         "payload isn't being assigned properly.")
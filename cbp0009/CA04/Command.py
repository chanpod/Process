'''
Created on Mar 27, 2014

@author: chanpod
'''
import re
import math
import os.path

class Command(object):
    
    address = None
    COMMANDWORD = 1
    MODECOMMAND = 2
    TRANSMIT = 1
    RECEIVE = 2
    
    #Mode Codes
    TRANSMITSTATUS = 2
    SHUTDOWN = 4
    RESET = 8
    TRANSMITVECTOR = 12
    TRANSMITLASTCOMMAND = 14
    
    commandType = 1
    modeCommand = 0
    count = 0
    tran_receiveFlag = RECEIVE
    subaddress = 0
    
    def __init__(self, addressIn = None):
        self.commandType = self.MODECOMMAND
        self.tran_receiveFlag = self.RECEIVE
        self.modeCommand = self.TRANSMITSTATUS
        try:
            if(addressIn == None):
                raise ValueError
            else:
                if(isinstance(addressIn, int)):
                    self.address = addressIn
                else:
                    raise ValueError
        except:
            print("Command.init: Address is invalid or missing.")
    
    def getTerminal(self):
        return self.address
    
    def setToCommandWord(self):
        self.commandType = self.COMMANDWORD
    
    def setToModeCommand(self, modeIn = None):
        MODEMIN = 0
        MODEMAX = 14
        if(modeIn != None):
            try:
                if(isinstance(modeIn, int)):
                    
                    if(modeIn >= MODEMIN and modeIn <= MODEMAX):
                        
                        if(modeIn == self.TRANSMITSTATUS):
                            self.modeCommand = self.TRANSMITSTATUS
                        elif(modeIn == self.SHUTDOWN):
                            self.modeCommand = self.SHUTDOWN
                        elif(modeIn == self.RESET):
                            self.modeCommand = self.RESET
                        elif(modeIn == self.TRANSMITVECTOR):
                            self.modeCommand = self.TRANSMITVECTOR
                        elif(modeIn == self.TRANSMITLASTCOMMAND):
                            self.modeCommand = self.TRANSMITLASTCOMMAND
                            
                    else:
                        raise ValueError
                else:
                    raise ValueError
                
            except ValueError:
                print("Command.setToModeComand: mode is invalid. Must be 2, 4, 8, 12, or 14.")
        else:
            self.modeCommand = self.TRANSMITSTATUS
    
    def getModeCode(self):
        try:
            if(self.commandType == self.MODECOMMAND):
                return self.modeCommand
            else:
                raise ValueError
        except ValueError:
            print("Command.getModeCode:  Current state is command word.")
    
    def isModeCommand(self):
        if(self.commandType == self.MODECOMMAND):
            return True
        else:
            return False
    
    def setSubAddress(self, address = None):
        ADDRESSMIN = 0
        ADDRESSMAX = 31
        try:
            if(address == None):
                raise ValueError
            else:
                if(isinstance(address, int)):
                    if(address >= ADDRESSMIN and address <= ADDRESSMAX):
                        self.subaddress = address
                else:
                    raise ValueError
        except ValueError:
            print("Command.setSubAddress:  ")
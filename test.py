# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 13:10:15 2016
@author: Aidan Hindmarch
Example script to run low temperature conductivity experiment.
Controls: 
    Keithley 2000 series DMM
    Oxford Instruments Mercury iTC temperature controller
    Tenma 72-2550 PSU
"""
from __future__ import print_function, division
from level2labs.lowtemperature import K2000, MercuryITC, TenmaPSU
from time import sleep, time
from datetime import datetime

import sys
import pylab

print('hello')
# Connect to devices
ITC = MercuryITC('COM6')  # PI USB-to-serial connection COM3

t = ITC.modules[0]  # module 0 is temperature board
# h = ITC.modules[1] # module 1 is heater power board
print(t.tset)
t.tset = 20
ITC.close()

Rdmm = K2000(16, 0)  # GPIB adaptor gpib0, device address 16
print(Rdmm.reading)


PSU = TenmaPSU('COM8') # USK-K-R-COM USB-to-serial connection COM4, must be connected via USB hub

print(PSU.GetIdentity())
PSU.SetVoltage = 12

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 09:18:17 2020

@author: USER
"""

import time
import random
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
#time.sleep(5)

x,y,z=mc.player.getTilePos()
while True:
    color=random.randrange(0,16)
    time.sleep(3)
    mc.setBlocks(x+25,y-1,z+25,x-25,y-1,z-25,95,color)
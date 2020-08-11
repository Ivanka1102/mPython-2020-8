# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 11:02:09 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
import random
mc=Minecraft.create()

while True:
    x,y,z=mc.player.getPos()
    color=random.randrange(0,9)
    mc.setBlock(x,y,z,38,color)
    time.sleep(0.2)
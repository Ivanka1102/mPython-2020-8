# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:38:07 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
while True:
        x,y,z=mc.player.getTilePos()
        mc.postToChat("我正在看著你x:"+str(x)+"y"+str(y)+"z:"+str(z))
        time.sleep(0.5)
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 14:35:42 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getPos()

a=0
while a<20:
    mc.setBlocks(x,y-1,z+30,x,y-10,z-30,5,1)
    x=x-5
    a=a+1
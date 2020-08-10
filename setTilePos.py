# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 14:37:58 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x=200
y=100
z=200
mc.player.setTilePos(x,y,z)
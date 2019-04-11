#!/usr/bin/python3
# -*- coding: utf-8 -*-

import lifeRule
import lifeMap
import time

if __name__ == '__main__':
    map = lifeMap.Map(66, 66)
    map.random(0.1)
    for i in range(100):
        lifeRule.game_cycle(map)
        time.sleep(0.01)
        map.show(10)
    #map.showloop(10)
    
    
        
    
    

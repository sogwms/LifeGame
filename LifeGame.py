#!/usr/bin/python3
# -*- coding: utf-8 -*-

import lifeRule
import lifeMap


if __name__ == '__main__':
    map = lifeMap.Map()
    map.random(0.1)
    for i in range(100):
        lifeRule.game_cycle(map)
    map.showloop(10)
    
    
        
    
    

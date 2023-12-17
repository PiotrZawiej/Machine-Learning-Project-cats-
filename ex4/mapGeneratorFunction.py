# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 13:24:09 2023

@author: Dell
"""
import numpy as np


def map_generator(map_size, objects):

# Generating map
    arr = np.array([["0" for _ in range(map_size)] for _ in range(map_size)])
    center_x, center_y = (len(arr[0]) // 2, len(arr[0]) // 2)
    arr[center_x,center_y] = 'H'
    
# Insert objects in the map
    for item, quantity in objects.items():
        for _ in range(quantity):
            rand_x, rand_y = np.random.randint(map_size), np.random.randint(map_size)

            while arr[rand_x, rand_y] != "0":
                rand_x, rand_y = np.random.randint(map_size), np.random.randint(map_size)
            
            arr[rand_x, rand_y] = item
            
    return arr

def calculate_distance(point1, point2):
    return np.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

def Hunting(cat_name, fav_objects, arr):
    center_x, center_y = (len(arr[0]) // 2, len(arr[0]) // 2)
    arr[center_x,center_y] = cat_name
    
    item_location = np.argwhere(arr == fav_objects[0])
    
    distance = calculate_distance(arr[center_x,center_y], item_location[0])
                
    return distance
    
    
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:25:52 2019

@author: swilson5
"""  
#.add_data() - which can take in  a list of values and extend the .data attribute
#.remove_data() accept a list of numbers and remove any of the numbers in that list from your object data

import math
import statistics 


class Calculator():
    def __init__ (self, data): 
        self.data = sorted(data)  
        self.calc_stats() 
    def calc_stats(self): 
        self.length = self.calc_len() 
        self.mean = self.calc_mean()  
        self.variance = self.calc_variance()
        self.stand_dev = self.calc_std()
        self.median = self.calc_med() 
    def calc_len(self): 
        length = len(self.data) 
        return length
    def calc_mean(self): 
        mean = sum(self.data)/len(self.data) 
        return mean 
    def calc_variance(self): 
        variance = statistics.variance(self.data)
        return variance
    def calc_std(self):
        std = math.sqrt(statistics.variance(self.data))
        return std 
    def calc_med(self): 
        sorted_data = sorted(self.data)  
        if len(sorted_data)%2: 
            return sorted_data[len(sorted_data)//2] 
        else: 
            upper = sorted_data[len(sorted_data)//2] 
            lower = sorted_data[(len(sorted_data)//2)-1] 
            return (upper+lower)//2 
    def add_data(self, new_data): 
        self.data.extend(new_data) 
        self.data = sorted(self.data) 
        self.calc_stats()  
    def remove_data(self, new_data): 
        self.data = [x for x in self.data if x not in new_data]
        self.calc_stats()       

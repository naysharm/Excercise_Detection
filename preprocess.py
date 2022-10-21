#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 12:40:03 2022

@author: nayaabsharma
"""

import pandas as pd


# make_list():
#     Applied on data for 1 exercise
#     takes each cell of the Series (which is in string format).
#     extracts the cordinates and returns them in float format list
def make_df(x):
    
    t = x.replace("[", "").replace("]", "").split(', ')
    t = pd.Series(t)
    t = t.apply(float)

    return t

    
   
def makeTuple(arr):
    #print(arr[0])
    a = [arr[0], arr[1], arr[2]]
    return a
   

def get_cordinates(exer):
    global joints
    
    #Appling the make_list function
    exer = exer.apply(make_df)
    
    #Transpose the return dataframe, 
    #to get the joint names as columns
    exer = exer.T
    
    #Extracting all the joint names.
    joints = list(exer.columns)
    
    #Creating an empty dataframe
    #to store the (x,y,z) cordinates 
    #for each joint as a tuple/list.
    cordinates = pd.DataFrame()

    for i in range(0, len(joints), 3):
        
        #taking the x,y,z for each joint 
        #for all movements
        arr = exer.iloc[:, i:i+3]

        #Converting the arr to single tuple 
        xyz = pd.Series(dtype=float)
        xyz = arr.apply(makeTuple, axis=1)

        #Storing the Series of tuples into
        #the dataframe, joint-wise
        col = joints[i].split('_', 1)[1]
        cordinates[col] = xyz
        
    
    return cordinates 

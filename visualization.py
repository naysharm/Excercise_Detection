#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 12:34:06 2022

@author: nayaabsharma
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Get angles using the dot product of 2 vectors
def get_angles(x, y, z, ax):
    
    #List of vectors.
    u, v = [], []
    
    #Left Elbow
    u.append([x[0]-x[2], y[0]-y[2], z[0]-z[2]])
    v.append([x[4]-x[2], y[4]-y[2], z[4]-z[2]])

    
    #Left Shoulder
    u.append([x[0]-x[2], y[0]-y[2], z[0]-z[2]])
    v.append([x[0]-x[12], y[0]-y[12], z[0]-z[12]])


    #Right Elbow
    u.append([x[1]-x[3], y[1]-y[3], z[1]-z[3]])
    v.append([x[3]-x[5], y[3]-y[5], z[3]-z[5]])

    
    #Right Shoulder
    u.append([x[1]-x[12], y[1]-y[12], z[1]-z[12]])
    v.append([x[1]-x[3], y[1]-y[3], z[1]-z[3]])
    

    #Left Hip
    u.append([x[8]-x[13], y[8]-y[13], z[8]-z[13]])
    v.append([x[6]-x[13], y[6]-y[13], z[6]-z[13]])

    
    #Left Knee
    u.append([x[10]-x[8], y[10]-y[8], z[10]-z[8]])
    v.append([x[8]-x[6], y[8]-y[6], z[8]-z[6]])

    
    #Right Hip
    u.append([x[13]-x[7], y[13]-y[7], z[13]-z[7]])
    v.append([x[7]-x[9], y[7]-y[9], z[7]-z[9]])
    

    #Right Knee
    u.append([x[7]-x[9], y[7]-y[9], z[7]-z[9]])
    v.append([x[9]-x[11], y[9]-y[11], z[9]-z[11]])
    

    # using the dot product formula,
    # calculating the angles between the 2 vectors
    # and storing the calculated angles in a list
    angle = []
    for a, b in zip(u, v):
        dotProd = np.dot(a, b)
        magProd = (np.linalg.norm(a) * np.linalg.norm(b))
        theta = np.degrees(np.arccos(dotProd/magProd))
        angle.append(np.around(theta, 2))
    
    # Displaying the angles on the joints
    
    ax.text(x[2], y[2], z[2], angle[0])
    ax.text(x[0], y[0], z[0], angle[1])
    ax.text(x[3], y[3], z[3], angle[2])
    ax.text(x[1], y[1], z[1], angle[3])
    ax.text(x[6], y[6], z[6], angle[4])
    ax.text(x[8], y[8], z[8], angle[5])
    ax.text(x[7], y[7], z[7], angle[6])
    ax.text(x[9], y[9], z[9], angle[7])
    ax.text(x[12], y[12], z[12], 'Neck', color='navy')
    ax.text(x[13], y[13], z[13], 'Hip', color='navy')


    return angle



def get_frames(x, y, z, ax, name):

    ax.clear()

    # Creating plot
    plt.title("This is how you do {}".format(name))
    
    #Joining Left and Right Shoulder
    k=[x[0], x[1]]
    l=[y[0], y[1]]
    m=[z[0], z[1]]
    ax.plot(k, l, m, 'ro-')

    
    #Joining Left Elbow and Shoulder
    k=[x[0], x[2]]
    l=[y[0], y[2]]
    m=[z[0], z[2]]
    ax.plot(k, l, m, 'ro-')

    
    #Joining Left Elbow and Wrist
    k=[x[4], x[2]]
    l=[y[4], y[2]]
    m=[z[4], z[2]]
    ax.plot(k, l, m, 'ro-')

    
    #Joining Right Elbow and Shoulder
    k=[x[3], x[1]]
    l=[y[3], y[1]]
    m=[z[3], z[1]]
    ax.plot(k, l, m, 'ro-')

    
    #Joining Right Elbow and Wrist
    k=[x[3], x[5]]
    l=[y[3], y[5]]
    m=[z[3], z[5]]
    ax.plot(k, l, m, 'ro-')

    
    #Joining Left and Right Hip
    k=[x[6], x[7]]
    l=[y[6], y[7]]
    m=[z[6], z[7]]
    ax.plot(k, l, m, 'ro-')

    
    #Joining Left Hip and Knee 
    k=[x[6], x[8]]
    l=[y[6], y[8]]
    m=[z[6], z[8]]
    ax.plot(k, l, m, 'ro-')

    
    #Joining Left Ankle and Knee 
    k=[x[10], x[8]]
    l=[y[10], y[8]]
    m=[z[10], z[8]]
    ax.plot(k, l, m, 'ro-')

    
    #Joining Right Hip and Knee 
    k=[x[9], x[7]]
    l=[y[9], y[7]]
    m=[z[9], z[7]]
    ax.plot(k, l, m, 'ro-')

    
    #Joining Right Ankle and Knee 
    k=[x[9], x[11]]
    l=[y[9], y[11]]
    m=[z[9], z[11]]
    ax.plot(k, l, m, 'ro-')

    
    #Joining Hip and Neck
    k=[x[12], x[13]]
    l=[y[12], y[13]]
    m=[z[12], z[13]]
    ax.plot(k, l, m, 'ro-')
    
    ax.scatter(x, y, z, color = "green")
  
    return 


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 13:24:06 2022

@author: nayaabsharma
"""

########Importing Libraries
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
import imageio
from visualization import get_frames, get_angles
from preprocess import get_cordinates
from sklearn.cluster import AgglomerativeClustering
# from make_cluster import clustering

###########################Pre-Processing###########################

#####Importing dataframe    
df = pd.read_csv('df.csv')

#####ramdomly picking an excercise
#np.random.seed(23)
i=np.random.randint(len(df))
exercise = df.loc[i, :]

# Getting the name of the selected exercise 
name = exercise.pop('name')
print('Exercise Chosen:', name)

# Getting cordinates for the chosen excercise
cordinates = get_cordinates(exercise)
joints = np.asarray(cordinates.columns)
# print(cordinates.columns)

##Creating path for the frames
dir_path = r'frames/{}/'.format(name)
if not os.path.exists(dir_path):
    os.makedirs(dir_path)


cordinates.to_csv('frames/{}/{}_cordinates.csv'.format(name, name))

###########################Visualising Excercise#####################
fig = plt.figure()  

plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")


# Generating plots for each point and
# Downloading them locally.
s=10
jnt_angles = pd.DataFrame()
cols = ['Left Elbow', 'Left Shoulder', 'Right Elbow', 'Right Shoulder',
        'Left Hip', 'Left Knee', 'Right Hip', 'Right Knee']

print('Downloading Frames in...')
# Taking one frame at a time
for i in range(len(cordinates)):
    
    ax = plt.axes(projection ="3d")
    # ax.view_init()
    a=cordinates.iloc[i,:]
    x, y, z = [], [], []
    # Storing the x, y, z cordinates for
    # each joint in a single list
    for j in range(len(a)):
        x.append(a[j][0])
        y.append(a[j][1])
        z.append(a[j][2])
    x.append((x[0]+x[1])/2)
    x.append((x[6]+x[7])/2)
    y.append((y[0]+y[1])/2)
    y.append((y[6]+y[7])/2)
    z.append((z[0]+z[1])/2)
    z.append((z[6]+z[7])/2)
    
    # Calling functions to get frames and angles.
    get_frames(x, y, z, ax, name)
    angles  = get_angles(x, y, z, ax)
    
    # Store the angles in a dataframe.
    jnt_angles = jnt_angles.append(dict(zip(cols, angles)), ignore_index=True)
    
    # Saving the frames/figures in the given location.
    plt.savefig(dir_path+'exer_{0}.jpg'.format(i))
    if s>0 and i%25==0:
        print(s)
        s-=1
        

print('Download Complete\n')


# Upload the downloaded frames in a list
# Read the frames one by one with imageio library
# and finally save them as a gif
frames = []
s='-'
print('Let\'s make the Gif!')
for i in range(len(cordinates)):
    
    frames.append(imageio.imread("frames/{}/exer_{}.jpg".format(name, i)))
    if i%50==0:
        print(s)
        s+='-'
print('Wait for it.....')
imageio.mimsave('frames/{}/BulkUp.gif'.format(name), frames)

print('Gif is ready!, Check it out :-)')

print('######################################################')


###########################Moving-Joints###########################
print('\nNow let\'s see what all joints are moving:\n')

mvg = []
n_mvg = []
std_lst = []
chg_angles = jnt_angles.diff().abs().dropna(axis=0)
for col in chg_angles.columns:

    std_lst.append(np.std(chg_angles[col]))
    
cluster_algorithm = AgglomerativeClustering(n_clusters=2)
labels = cluster_algorithm.fit_predict(np.expand_dims(std_lst, axis=-1))

for i in range(len(labels)):
    if labels[i]==1:
        mvg.append(cols[i])
    else:
        n_mvg.append(cols[i])


print('Moving Joints', mvg)
print('Non Moving Joints:', n_mvg)


###########################Clustering###########################
label_df = pd.DataFrame()
label_df = label_df.append(dict(zip(cols, labels)),
                           ignore_index=True)

label_df['exercise'] = name

path = os.path.exists("MovingJoints.csv")
if path:
    mj = pd.read_csv('MovingJoints.csv')
    if name not in mj['exercise'].tolist():
        label_df.to_csv('MovingJoints.csv', mode='a', 
                    index=False, header=False)
else:
    label_df.to_csv('MovingJoints.csv', mode='a', 
                    index=False, header=True)
  









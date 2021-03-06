# -*- coding: utf-8 -*-
"""VERI1COLOR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KOkyV88gtJLewdhT6h9_9mqadTI7JFUR
"""

import numpy as np
from skimage import io
import cv2
import matplotlib.pyplot as plt
import sys
import os
from keras.preprocessing import image
from skimage.color import rgb2gray
from PIL import Image

def show(img, figsize=(6, 6), title="Image"):
    figure=plt.figure(figsize=figsize)
    
    plt.imshow(img)
    plt.show()

img = cv2.imread("renkli.bmp")



# ============------------=============
redlist = []
redlist2 = []
greenlist = []
greenlist2 = []
bluelist = []
bluelist2 = []
# ============------------=============

for x in range(len(img)):
  for y in range(len(img[x])):
    redlist.append(img[x][y][0])
  redlist2.append(redlist)
  redlist = []

for x in range(len(img)):
  for y in range(len(img[x])):
    greenlist.append(img[x][y][1])
  greenlist2.append(greenlist)
  greenlist = []

for x in range(len(img)):
  for y in range(len(img[x])):
    bluelist.append(img[x][y][2])
  bluelist2.append(bluelist)
  bluelist = []


red = np.array([np.array(xi) for xi in redlist2]) 
print(red.shape)
green = np.array([np.array(xi) for xi in greenlist2])
print(green.shape)
blue = np.array([np.array(xi) for xi in bluelist2])
print(blue.shape)

redT = np.transpose(red)
greenT = np.transpose(green)
blueT = np.transpose(blue)

print(red)

# 398466 bytes

def encode(s):
 
    encoding_row = [] 
    i = 0
    while i < len(s):
        # count occurrences of character at index `i`
        count = 1
 
        while i + 1 < len(s) and s[i] == s[i + 1]:

            count = count + 1
            i = i + 1
 
        # append current character and its count to the result
        if count > 1:
            encoding_row.append(255)
            encoding_row.append(count)
            encoding_row.append(s[i])
            i = i + 1
        else :
            encoding_row.append(s[i])
            i = i + 1
 
    return encoding_row

def compress(a):
  encoding_column = []
  cnt = 0
  for x in range(len(a)):
    new_row = encode(a[x])
    cnt = cnt + len(new_row)
    encoding_column.append(new_row)
    new_row = []


  y=np.array([np.array(xi) for xi in encoding_column])

  return print(cnt, " bytes","\n")

compress(red)

compress(blue)

compress(green)

"""**80109 bytes after the compression row by row  - nearly 80 per cent compression(79.8 compression)**"""

compress(redT)

compress(greenT)

compress(blueT)

"""**COMPRESSION COLOR BY COLUMN 83944 again 78.9 per cent compression ratio**"""

rows = red.shape[0]
columns = red.shape[1]



solution = [[] for i in range(0, (rows+columns)-1)]

for i in range(rows):
  for j in range(columns):
    summ = i + j
    if summ % 2 == 0:
      solution[summ].insert(0, red[i][j])
    else:
      solution[summ].append(red[i][j])

compress(solution)
print("\n")

# =========================

rows = green.shape[0]
columns = green.shape[1]



solution = [[] for i in range(0, (rows+columns)-1)]

for i in range(rows):
  for j in range(columns):
    summ = i + j
    if summ % 2 == 0:
      solution[summ].insert(0, green[i][j])
    else:
      solution[summ].append(green[i][j])

compress(solution)

print("\n")

# ==============================
rows = blue.shape[0]
columns = blue.shape[1]



solution = [[] for i in range(0, (rows+columns)-1)]

for i in range(rows):
  for j in range(columns):
    summ = i + j
    if summ % 2 == 0:
      solution[summ].insert(0, blue[i][j])
    else:
      solution[summ].append(blue[i][j])

compress(solution)

"""**77.8 per cent compression zig zag scanning**"""
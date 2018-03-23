from collections import deque
import numpy as np
import argparse
import imutils
import cv2
from tkinter import *
from PIL import Image, ImageTk, Image, ImageDraw, ImageFont
import math
import sys
import os

class vecteur:



	def __init__(self, x1, y1, x2, y2):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2

xl = list()
yl = list()

vectors = dict()
id_ = 0

master = Tk()
master.geometry("1000x600")

can = Frame(master, bg="green")
can.pack()

footCan = Canvas(can, width=600, height=700, bg="green")
footCan.pack()

with open('terrain.svg', 'r') as content_file:
    content = content_file.read()
    

for s in content.split("<g>")[2].split("</title>")[1].split("</g>")[0].split("<line"):
    if(not s == "\n  "):
        #print(s.split("y1=\"")[1].split("\" x1")[0])
        y2 = int(s.split("y2=\"")[1].split("\" x2")[0])
        x2 = int(s.split("x2=\"")[1].split("\" y1")[0])
        y1 = int(s.split("y1=\"")[1].split("\" x1")[0])
        x1 = int(s.split("x1=\"")[1].split("\" stroke-width")[0])

        v = vecteur(x1, y1, x2, y2)
        vectors[id_] = v
        xl.append(x2)
        xl.append(x1)
        yl.append(y2)
        yl.append(y1)
        id_ += 1

#get the most extreme y coords

print(xl)
print(yl)

xmax = int(max(xl))
ymax = int(max(yl))
xmin = int(min(xl))
ymin = int(min(yl))

print(x1, y1, x2, y2)
print(xmax, ymax, xmin, ymin)

#print(int(xmax) - int(xmin), int(ymax) - int(ymin))
#calculate coords of the center

cmx = xmin + (xmax - xmin)/2
cmy = ymin + (ymax - ymin)/2

distancea = dict()
distanceb = dict()
#determine the closest vector and its point (1 or 2)
idd = 0
for i in range(len(vectors)):
	d1 = math.sqrt((math.fabs(vectors[idd].x1 - cmx))**2 + (math.fabs(vectors[idd].y1 -cmy))**2)
	d2 = math.sqrt((math.fabs(vectors[idd].x2 - cmx))**2 + (math.fabs(vectors[idd].y2 -cmy))**2)

	distancea[idd] = d1
	distanceb[idd] = d2
	idd += 1

lowestDist = 10000000
indexLowest = 1
iddLowest = 0
for i in range(len(vectors)):
	if distancea[idd] < lowestDist:
		lowestDist = distancea[idd]
		iddLowest = i
		indexLowest = 1
	if distanceb[idd] < lowestDist:
		lowestDist = distanceb[idd]
		iddLowest = i 
		indexLowest = 2



footCan.create_rectangle(xmin, ymin, xmax, ymax)

print("center", cmx, cmy)

file = open("result.alba", "w") 
idd = 0
for i in range(len(vectors)):
    file.write(str(i) + ":[" + str(vectors[i].x1) + ";" + str(vectors[i].y1) + ";" + str(vectors[i].x2) + ";" + str(vectors[i].y2) + "]" + "\n")
    footCan.create_line(vectors[i].x1, vectors[i].y1, vectors[i].x2, vectors[i].y2, fill="#000")

   
file.close()

footCan.create_oval(cmx-int(20), cmy-int(20), cmx+int(20), cmy+int(20), fill="red")
    
master.mainloop()

class vecteur:

	def __init__(self, x1, y1, x2, y2):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
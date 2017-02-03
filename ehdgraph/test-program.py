from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
import serial
import string
import sys
import subprocess
import os
import time
import math

#THIS INITIALIZES THE GRAPHICAL USER INTERFACE (GUI)
app = QtGui.QApplication([])
win = pg.GraphicsWindow(title="Electro-Hydro-Dynamic Graphing Tool")
win.resize(1000,600)
win.setWindowTitle('Graph Utility')
pg.setConfigOptions(antialias=True)

#THIS INITIALIZES ALL GRAPH WINDOWS TO BE ADDED TO THE GUI
graph2 = win.addPlot(title="Angular Velocity", row=2, col=1)
graph3 = win.addPlot(title="Total Angle", row=2, col=3)

#THIS IS WHERE THE GRAPHS ARE PLOTTED IN REAL TIME
ser = serial.Serial('COM5', 57600, timeout = 5)	# open serial port

direction = 0
total_time = 0
total_angle = 0
count = 0
n = 6			#chosen constant (CHANGE AS NEEDED) number of lines/arms in the encoder
k = 1			#chosen constant (CHANGE AS NEEDED) k = Inertia / Radius

timeX = []
angleY = []
velocity = []

while(ser.isOpen):
	if (count == 0):
		pass
	else:
		line = '{}'.format(ser.readline())
		if len(line) < 9:
			break
		
		#calculations should come after the checks that catch the specific errors (HERE)
		args = ("'bnr\\ ")
		temp = line.strip(args)
		value = float(temp.split(",")[1])	# return the time difference between rotations
		direction_bit = int(temp.split(",")[2])
		if direction_bit == 0:	# return the direction of the spinning encoder "0 for positive" & "1 for negative"
			direction = float(1)
		else:
			direction = float(-1)
		
		#calculations go here:
		angle_change = (math.pi)/(n)	#change in the angle
		total_angle += k*angle_change*count			#total angle passed
		total_time += value		#total time passed
		angular_velocity = (angle_change/value)*direction		#angular velocity
		
		#add the values to the arrays
		angleY.append(total_angle)		#set the angle values
		timeX.append(total_time)	#set the time values
		velocity.append(angular_velocity)
		
		###PLOT THE VELOCITY
		graph2.plot(timeX,velocity, pen=(0,0,255), name="Angular Velocity")
		pg.QtGui.QApplication.processEvents()
		graph2.showGrid(x=True, y=True)
		
		####PLOT TOTAL ANGLE VS. TIME
		graph3.plot(timeX,angleY, pen=(255,0,0), name="Total Angle")
		pg.QtGui.QApplication.processEvents()
		graph3.showGrid(x=True, y=True)
		
	count += 1
ser.close()             # close port
print("port closed")

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

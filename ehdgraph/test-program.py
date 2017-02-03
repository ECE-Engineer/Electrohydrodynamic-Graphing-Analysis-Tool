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
'''graphAll = win.addPlot(title="Superimposed Graphs", row=1, col=1, colspan=3)'''
'''win.nextRow()'''
graph2 = win.addPlot(title="Angular Velocity", row=2, col=1)
'''graph1 = win.addPlot(title="Angular Acceleration", row=2, col=2)'''
graph3 = win.addPlot(title="Total Angle", row=2, col=3)

#THIS IS WHERE THE GRAPHS ARE PLOTTED IN REAL TIME
ser = serial.Serial('COM5', 57600, timeout = 5)	# open serial port

direction = 0
total_time = 0
temp3_anglular_velocity = 0
temp1_anglular_velocity = 0
temp2_angular_velocity = 0
total_angle = 0
count = 0
n = 12			#constant (FIX THIS LATER) number of lines/arms in the encoder
k = 1			#chosen constant (k = Inertia / Radius)

timeX1 = []
angleY = []
timeX2 = []
averageY = []
timeX3 = []
'''forceY = []'''

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
		total_angle += angle_change			#total angle passed
		angleY.append(total_angle)		#set the angle values
		total_time += value		#total time passed
		timeX1.append(total_time)	#set the time values
		angular_velocity = (angle_change/value)*direction		#angular velocity
		
		if count%3 == 1:
			temp1_anglular_velocity = angular_velocity
			
		if count%3 == 2:
			temp2_angular_velocity = angular_velocity
		
		if count > 3 & count%3 == 0:
			timeX3.append(total_time)
			'''angular_acceleration = (angular_velocity - temp3_anglular_velocity)/value		#angular acceleration'''
			'''EHD_force = angular_acceleration*1'''
			'''forceY.append(EHD_force)'''
			####PLOT ANGULAR ACCELERATION VS. TIME
			'''graphAll.plot(timeX3,forceY, pen=(0,255,0), name="Angular Acceleration")'''
			'''pg.QtGui.QApplication.processEvents()'''
			'''graph1.plot(timeX3,forceY, pen=(0,255,0), name="Angular Acceleration")'''
			'''pg.QtGui.QApplication.processEvents()'''
			'''graphAll.showGrid(x=True, y=True)'''
			'''graph1.showGrid(x=True, y=True)'''
		if count > 1 & count%3 == 0:	#implement the smoothing function "moving average"
			timeX2.append(total_time)
			temp3_anglular_velocity = angular_velocity	#this is the previous angular velocity
			####PLOT ANGULAR velocity VS. TIME
			average = (temp1_anglular_velocity + temp2_angular_velocity + temp3_anglular_velocity) / 3
			averageY.append(average)		#set the average values
			'''graphAll.plot(timeX2,averageY, pen=(0,0,255), name="Angular Velocity")'''
			'''pg.QtGui.QApplication.processEvents()'''
			graph2.plot(timeX2,averageY, pen=(0,0,255), name="Angular Velocity")
			pg.QtGui.QApplication.processEvents()
			'''graphAll.showGrid(x=True, y=True)'''
			graph2.showGrid(x=True, y=True)
		####PLOT TOTAL ANGLE VS. TIME
		'''graphAll.plot(timeX1,angleY, pen=(255,0,0), name="Total Angle")'''
		'''pg.QtGui.QApplication.processEvents()'''
		graph3.plot(timeX1,angleY, pen=(255,0,0), name="Total Angle")
		pg.QtGui.QApplication.processEvents()
		'''graphAll.showGrid(x=True, y=True)'''
		graph3.showGrid(x=True, y=True)
	count += 1
ser.close()             # close port
print("port closed")

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

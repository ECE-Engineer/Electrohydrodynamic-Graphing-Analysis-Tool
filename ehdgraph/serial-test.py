import serial
import string
import sys
import subprocess
import os
import time
import tachometergraph
import math
import _thread

graph1 = tachometergraph.TachGraph("PLOT ANGULAR ) VS. TIME")
graph2 = tachometergraph.TachGraph("PLOT ANGULAR VELOCITY VS. TIME")
graph3 = tachometergraph.TachGraph("PLOT TOTAL ANGLE VS. TIME")

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
		total_time += value		#total time passed
		angular_velocity = (angle_change/value)*direction		#angular velocity
		
		if count%3 == 1:
			temp1_anglular_velocity = angular_velocity
			
		if count%3 == 2:
			temp2_angular_velocity = angular_velocity
		
		if count > 3 && count%3 == 0:
			angular_acceleration = (angular_velocity - temp3_anglular_velocity)/value		#angular acceleration
			EHD_force = angular_acceleration*1
			####PLOT ANGULAR ACCELERATION VS. TIME
			graph1.add_point(total_time, EHD_force)
		
		if count > 1 && count%3 == 0:	#implement the smoothing function "moving average"
			temp3_anglular_velocity = angular_velocity	#this is the previous angular velocity
			
			####PLOT ANGULAR velocity VS. TIME
			average = (temp1_anglular_velocity + temp2_angular_velocity + temp3_anglular_velocity) / 3
			graph2.add_point(total_time, average)
		
		####PLOT TOTAL ANGLE VS. TIME
		graph3.add_point(total_time, total_angle)
	count += 1
ser.close()             # close port
print("port closed")

try:
	_thread.start_new_thread(graph1.close_graph())
	_thread.start_new_thread(graph2.close_graph())
	_thread.start_new_thread(graph3.close_graph())
except TypeError:
	print("Finished")
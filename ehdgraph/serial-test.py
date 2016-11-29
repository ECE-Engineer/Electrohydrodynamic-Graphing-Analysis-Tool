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
graph2 = tachometergraph.TachGraph("PLOT ANGULAR SPEED VS. TIME")
graph3 = tachometergraph.TachGraph("PLOT TOTAL ANGLE VS. TIME")

ser = serial.Serial('COM5', 57600, timeout = 5)	# open serial port
#print("port open")
# print(ser.read(10))        # read up to ten bytes (timeout)

# print(ser.name)         # check which port was really used

total_time = 0
temp_anglular_speed = 0
total_angle = 0
count = 0
n = 12			#constant (FIX THIS LATER) number of lines/arms in the encoder
k = 1			#chosen constant (k = Inertia / Radius)

#########################################################################################################
#NOTE : CALCULATIONS FOR DELTA THETA WILL NEED TO BE DRASTICALLY ALTERED FOR ACTUAL SPINNERS#
#########################################################################################################
try:
	while(ser.isOpen):	# THIS WILL CHANGE TO NOT HAVE THE 1000		 and (count < 500)
		line = '{}'.format(ser.readline())
		if (count == 0):
			pass
		elif (line == '{}'.format(b' \r ') or line == ""):
			print("ok")
		else:
			print("DONE")
			print(line)
			args = ("'bnr\\ ")
			temp = line.strip(args)
			value = float(temp.split(",")[1])	# return the time difference between rotations
			angle_change = (math.pi)/(n)	#change in the angle
			total_angle += angle_change			#total angle passed
			total_time += value		#total time passed
			angular_speed = angle_change/value		#angular speed
			
			if count > 1:
				angular_acceleration = (angular_speed - temp_anglular_speed)/value		#angular acceleration
				EHD_force = angular_acceleration*1
				####PLOT ANGULAR ACCELERATION VS. TIME
				graph1.add_point(total_time, EHD_force)
			
			temp_anglular_speed = angular_speed		#this is the previous angular speed
			
			####PLOT ANGULAR SPEED VS. TIME
			graph2.add_point(total_time, angular_speed)
			
			
			####PLOT TOTAL ANGLE VS. TIME
			graph3.add_point(total_time, total_angle)
			
			print(value)   # read a '\n' terminated line
			
		count += 1
except IndexError:
	print("ERROR CAUGHT")

ser.close()             # close port
print("port closed")

try:
	_thread.start_new_thread(graph1.close_graph())
	_thread.start_new_thread(graph2.close_graph())
	_thread.start_new_thread(graph3.close_graph())
except TypeError:
	print("Finished")


# try:
	# while True:
		# pass
# except KeyboardInterrupt:
	# print("Done")


# try:
	# graph1.close_graph()
	# print("111111")
	# graph2.close_graph()
	# print("222222222")
	# graph3.close_graph()
# except KeyboardInterrupt:
	# print("END")

# subprocess.Popen(['writeFromCurrent.py', '{}'.format(arg1), '{}'.format(arg4)], shell = True )
# subprocess.call(['ensemble_test.exe', '-D', '\\\.\{}'.format(comPort), '-x', message])
# import signal
# print 'complete'
#os.kill(ser.pid, signal.SIGTERM)





















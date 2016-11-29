import numpy as np
import pyqtgraph as pg
import time
import os

# y = [1,2,3,4,5,6,7,8,9,10]
# #data = y#np.random.normal(size=1000)

# pw = pg.plot()




# i = 0
# while i < 100:
	# pw.plot(y, title="Graphing Tool", clear=True)
	# pg.QtGui.QApplication.processEvents()
	# y.append(i)
	# i += 1
	
# pw.plot(y, title="Graphing Tool", clear=False)
# pg.QtGui.QApplication.exec_()


# y = [1,2,3,4,5,6,7,8,9,10]
# #data = y#np.random.normal(size=1000)

# pw = pg.plot()




# while True:
	# pw.plot(y, title="Graphing Tool", clear=True)
	# pg.QtGui.QApplication.processEvents()
	# line = input("")
	# reading = float(line)
	# y.append(reading)
	
# pw.plot(y, title="Graphing Tool", clear=False)
# pg.QtGui.QApplication.exec_()


class TachGraph(object):
	pw = None
	x = None
	y = None
	name = None
	
	def __init__(self, name):
		self.pw = pg.plot(title = name)
		self.x = []
		self.y = []
		self.name = name
	
	def add_point(self, valuex, valuey):
		self.x.append(valuex)
		self.y.append(valuey)
		self.pw.plot(self.x, self.y, title="HELLO", clear=True)
		pg.QtGui.QApplication.processEvents()

	def close_graph(self):
		self.pw.plot(self.x, self.y, title="HELLO", clear=False)
		pg.QtGui.QApplication.exec_()

# ## Start Qt event loop unless running in interactive mode or using pyside.
# if __name__ == '__main__':
    # import sys
    # if sys.flags.interactive != 1 or not hasattr(QtCore, 'PYQT_VERSION'):
        # pg.QtGui.QApplication.exec_()
		
		
		
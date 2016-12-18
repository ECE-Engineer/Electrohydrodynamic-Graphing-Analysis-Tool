
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg

app = QtGui.QApplication([])

win = pg.GraphicsWindow(title="Basic plotting examples")
win.resize(1000,600)
win.setWindowTitle('pyqtgraph example: Plotting')

pg.setConfigOptions(antialias=True)

p2 = win.addPlot(title="Multiple curves", row=1, col=1, colspan=3)

p2.plot(np.random.normal(size=100), pen=(255,0,0), name="Red curve")
p2.plot(np.random.normal(size=110)+5, pen=(0,255,0), name="Blue curve")
p2.plot(np.random.normal(size=120)+10, pen=(0,0,255), name="Green curve")

p2.showGrid(x=True, y=True)





win.nextRow()

p4 = win.addPlot(title="Parametric, grid enabled", row=2, col=1)
x = np.cos(np.linspace(0, 2*np.pi, 1000))
y = np.sin(np.linspace(0, 4*np.pi, 1000))
p4.plot(x, y)
p4.showGrid(x=True, y=True)


p4 = win.addPlot(title="Parametric, grid enabled", row=2, col=2)
x = np.cos(np.linspace(0, 2*np.pi, 1000))
y = np.sin(np.linspace(0, 4*np.pi, 1000))
p4.plot(x, y)
p4.showGrid(x=True, y=True)


p4 = win.addPlot(title="Parametric, grid enabled", row=2, col=3)
x = np.cos(np.linspace(0, 2*np.pi, 1000))
y = np.sin(np.linspace(0, 4*np.pi, 1000))
p4.plot(x, y)
p4.showGrid(x=True, y=True)


## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()




'''
import pyqtgraph.examples
pyqtgraph.examples.run()
'''
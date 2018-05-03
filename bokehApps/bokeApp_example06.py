from bokeh.io import curdoc

from bokeh.layouts import column, widgetbox
from bokeh.models import ColumnDataSource, Slider
import numpy as np
from numpy.random import random

from bokeh.plotting import figure


plot = figure()
N = 300
source = ColumnDataSource(data={'x':random(N), 'y':random(N)})

plot.circle('x', 'y', source = source)

slider01 = Slider(title = "slider 01", start = 0, end = 1000, 
	step = 20, value = 1)
	

def callback(attr, old, new):
	N = slider01.value
	source.data = {'x':random(N), 'y':random(N)}


slider01.on_change('value', callback)

layout = column(widgetbox(slider01), plot)


curdoc().add_root(layout)
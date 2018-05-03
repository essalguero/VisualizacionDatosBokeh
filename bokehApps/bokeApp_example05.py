from bokeh.io import curdoc

from bokeh.layouts import column, widgetbox
from bokeh.models import ColumnDataSource, Slider
import numpy as np

from bokeh.plotting import figure


plot = figure()
scale = 1
x = np.linspace(0.3, 10, 300)
y = np.sin(scale / x)
source = ColumnDataSource(data={'x':x, 'y':y})

plot.line('x', 'y', source = source)

slider01 = Slider(title = "slider 01", start = 0, end = 10, 
	step = 0.1, value = 2)
	

def callback(attr, old, new):
	scale = slider01.value
	new_y = np.sin(scale / x)
	source.data = {'x':x, 'y':new_y}


slider01.on_change('value', callback)

layout = column(widgetbox(slider01), plot)


curdoc().add_root(layout)
from bokeh.io import curdoc

from bokeh.layouts import widgetbox
from bokeh.models import Slider

slider01 = Slider(title = "slider 01", start = 0, end = 10, 
	step = 0.1, value = 2)
	
slider02 = Slider(title = "slider 02", start = 0, end = 100, 
	step = 1, value = 20)

layout = widgetbox(slider01, slider02)


curdoc().add_root(layout)
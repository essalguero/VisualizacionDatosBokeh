from bokeh.io import curdoc

from bokeh.layouts import widgetbox
from bokeh.models import Slider

slider = Slider(title = "slider 01", start = 0, end = 10, 
	step = 0.1, value = 2)

layout = widgetbox(slider)


curdoc().add_root(layout)
from bokeh.io import curdoc
from bokeh.plotting import figure

plot = figure()
plot.line([1, 2, 3, 4, 5], [2, 5, 4, 6, 7])

curdoc().add_root(plot)
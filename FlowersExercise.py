from bokeh.sampledata.iris import flowers as df
from bokeh.models import Label
from bokeh.io import output_file

from bokeh.plotting import figure
from bokeh.io import show, output_notebook

from bokeh.plotting import ColumnDataSource #para poder lincar datos de distintos datasets
from bokeh.models import CategoricalColorMapper, HoverTool

import pandas as pd
import numpy as np
import json

from bokeh.layouts import column, row

from bokeh.layouts import gridplot

print(df.columns)

from bokeh.palettes import d3

factores = list(df['species'].unique())
color_mapper = CategoricalColorMapper(factors = factores, 
                                      palette = d3['Category10'][3])

#color_mapper = CategoricalColorMapper(factors = ['GOLD', 'SILVER', 'BRONZE'], palette = ['goldenrod', 'silver', 'saddlebrown'])
plotsList = []
row = 4
for rowVarName in list(df.columns)[0:4]:
    #print(rowVarName)
    rowList = []
    column = 1
    row = row - 1
    for columnVarName in list(reversed(list(df.columns)[0:4])):
        #print(columnVarName)
        currentFigure = figure(plot_width = 200, plot_height = 200)
        currentFigure.circle(columnVarName, rowVarName, size = 10, source = df, color = {'field' : 'species', 'transform': color_mapper} )
        
        currentFigure.min_border_left = 10
        currentFigure.min_border_top = 10
        currentFigure.min_border_right = 10
        currentFigure.min_border_bottom = 10
        
        if (rowVarName == columnVarName):
            #currentFigure.title.text = rowVarName
            if (row != 0):
                citation = Label(x=20, y=150, x_units='screen', y_units='screen',
                     text=rowVarName, render_mode='css',
                     border_line_alpha=1.0,
                     background_fill_color='white', background_fill_alpha=1.0)
            else:
                citation = Label(x=20, y=130, x_units='screen', y_units='screen',
                     text=rowVarName, render_mode='css',
                     border_line_alpha=1.0,
                     background_fill_color='white', background_fill_alpha=1.0)
                
            currentFigure.add_layout(citation)
        
        if row != 0:
            currentFigure.xaxis.visible = False
        else:
            currentFigure.plot_height += 30
            currentFigure.min_border_bottom += 30
            
        if column != 1:
            currentFigure.yaxis.visible = False
        else:
            currentFigure.plot_width += 30
            currentFigure.min_border_left += 30
            
        rowList.append(currentFigure)
        column = column + 1
        #show(currentFigure)
    plotsList.append(rowList)
    


        
layout = gridplot(plotsList)
output_file("flowers.html")
show(layout)
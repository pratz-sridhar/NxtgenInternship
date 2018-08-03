

'''This file is used for plotting the data received from the data.py files. The plotly library is used for visualization of the data.
    The window provides a dropdown menue for selecting a specific zone whose server information is provided as a graph'''


import plotly.offline as py
import plotly.graph_objs as go
from dataframes import *
import warnings
import sys

if not sys.warnoptions:
    warnings.simplefilter("ignore")

x=[]                                                #A list to store all the hostnames of a specific zone
y_one=[]                                            # A list to store the number of days that a server has been up    
y_two=[]                                            # A list to store the number of minutes since a server was last reset
y=[]                                                # A list to store the time since last reset in the format- HH:MM:SS

extract('BLR')                                      # extract data of the BLR servers
x,y_one,y_two,y= process_data()                     # Assigning values of a specific zone
Bangalore_one = go.Bar(x=x,
                        y=y_one,
                        name='Days'
                        )                           # Graph to plot number of days that the server has been active
Bangalore_two = go.Line(x=x,                        
                           y=y_two,
                           text=y,
                            mode='lines+markers',
                           name='Minutes since reset'
                           )                        # Graph to plot the time elapsed since last reset


extract('MUM')                                      # extract data of the MUM servers
x,y_one,y_two,y=process_data()                      # Assigning values of MUM zone
Mumbai_one = go.Bar(x=x,                
                            y=y_one,
                            name='Days'
                            )                       # Bar Graph to show number of days that the servers have been up
Mumbai_two = go.Scatter(x=x,        
                        y=y_two,
                        text=y,
                        name='Minutes since reset'
                        )                           #Line graph to show time elapsed since last reset


extract('FDB')                                      # extract data of the FDB servers
x,y_one,y_two,y=process_data()                      # Assigning values of FDB zone

Faridabad_one = go.Bar(x=x,
                       y=y_one,
                       name='Days'
                           )                        # Bar Graph to show number of days that the servers have been up
Faridabad_two = go.Scatter(x=x,
                           y=y_two,
                           text=y,
                           name='Minutes since reset'
                           )                        #Line graph to show time elapsed since last reset


extract('AMD')                                      # extract data of the AMD servers
x,y_one,y_two,y=process_data()                      # Assigning values of AMD zone
Ahmedabad_one = go.Bar(x=x,
                           y=y_one,
                           name='Days'
                       )                            # Bar Graph to show number of days that the servers have been up
Ahmedabad_two = go.Scatter(x=x,
                           y=y_two,
                           text=y,
                           name='Minutes since reset'
                           )                        #Line graph to show time elapsed since last reset


data = [Bangalore_one, Bangalore_two, Mumbai_one, Mumbai_two, Faridabad_one, Faridabad_two, Ahmedabad_one, Ahmedabad_two] # data variable used to store all graphs



updatemenus = list([                                # This variable is used to provide a dropdownbox for selecting the different zones
    dict(active=-1,
         buttons=list([   
            dict(label = 'BLR',
                 method = 'update',
                 args = [{'visible': [True, True, False, False, False, False, False, False]},
                         {'title':'Uptime information for BLR servers'}]),
            dict(label = 'MUM',
                 method = 'update',
                 args = [{'visible': [False, False, True, True, False, False, False, False]},
                         {'title':'Uptime information for MUM servers'}]),
            dict(label = 'FDB',
                 method = 'update',
                 args = [{'visible': [False, False, False, False, True, True, False, False]},
                         {'title':'Uptime information for FDM servers'}]),
            dict(label = 'AMD',
                 method = 'update',
                 args = [{'visible': [False, False, False, False, False, False, True, True]},
                         {'title':'Uptime information for AMD servers'}]),
        ]),
    )
])

layout = dict(title='Servers', showlegend=True,                             # describes the layout of the window housing all graphs
              updatemenus=updatemenus, xaxis=dict(title= 'SERVER NAMES'))

fig = dict(data=data, layout=layout)
py.plot(fig, filename='update_dropdown')                                    # Plots the data

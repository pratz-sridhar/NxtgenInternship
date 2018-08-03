import plotly.offline as py
import plotly.graph_objs as go
from dataframes import *
import warnings
import sys

if not sys.warnoptions:
    warnings.simplefilter("ignore")

x=[]
y_one=[]
y_two=[]
y=[]

extract('BLR')
x,y_one,y_two,y= process_data()
Bangalore_one = go.Bar(x=x,
                        y=y_one,
                        name='Days'
                        )
Bangalore_two = go.Line(x=x,
                           y=y_two,
                           text=y,
                            mode='lines+markers',
                           name='Minutes since reset'
                           )


extract('MUM')
x,y_one,y_two,y=process_data()
Mumbai_one = go.Bar(x=x,
                            y=y_one,
                            name='Days'
                            )
Mumbai_two = go.Scatter(x=x,
                        y=y_two,
                        text=y,
                        name='Minutes since reset'
                        )


extract('FDB')
x,y_one,y_two,y=process_data()

Faridabad_one = go.Bar(x=x,
                       y=y_one,
                       name='Days'
                           )
Faridabad_two = go.Scatter(x=x,
                           y=y_two,
                           text=y,
                           name='Minutes since reset'
                           )


extract('AMD')
x,y_one,y_two,y=process_data()
Ahmedabad_one = go.Bar(x=x,
                           y=y_one,
                           name='Days'
                       )
Ahmedabad_two = go.Scatter(x=x,
                           y=y_two,
                           text=y,
                           name='Minutes since reset'
                           )


data = [Bangalore_one, Bangalore_two, Mumbai_one, Mumbai_two, Faridabad_one, Faridabad_two, Ahmedabad_one, Ahmedabad_two]



updatemenus = list([
    dict(active=-1,
         buttons=list([   
            dict(label = 'BLR',
                 method = 'update',
                 args = [{'visible': [True, True, False, False, False, False, False, False]},
                         {'title':'Uptime information for BLR servers'}]),
            #dict(label = 'BLR(TIME)',
             #    method = 'update',
              #   args = [{'visible': [False, True, False, False, False, False, False, False]},
               #          {'title':'Number of seconds since last reset of BLR servers'}]),'''
            dict(label = 'MUM',
                 method = 'update',
                 args = [{'visible': [False, False, True, True, False, False, False, False]},
                         {'title':'Uptime information for MUM servers'}]),
            #dict(label = 'MUM(TIME)',
             #    method = 'update',
              #   args = [{'visible': [False, False, False, True, False, False, False, False]},
               #          {'title':'Number of seconds since last reset of MUM servers'}]),'''
            dict(label = 'FDB',
                 method = 'update',
                 args = [{'visible': [False, False, False, False, True, True, False, False]},
                         {'title':'Uptime information for FDM servers'}]),
            #dict(label = 'FDM(TIME)',
             #    method = 'update',
              #   args = [{'visible': [False, False, False, False, False, True, False, False]},
               #          {'title':'Number of seconds since last reset of FDM servers'}]),'''
            dict(label = 'AMD',
                 method = 'update',
                 args = [{'visible': [False, False, False, False, False, False, True, True]},
                         {'title':'Uptime information for AMD servers'}]),
            #dict(label = 'AMD(TIME)',
             #    method = 'update',
              #   args = [{'visible': [False, False, False, False, False, False, False, True]},
               #          {'title':'Number of seconds since last reset of AMD servers'}])'''
        ]),
    )
])

layout = dict(title='Servers', showlegend=True,
              updatemenus=updatemenus, xaxis=dict(title= 'SERVER NAMES'))

fig = dict(data=data, layout=layout)
py.plot(fig, filename='update_dropdown')

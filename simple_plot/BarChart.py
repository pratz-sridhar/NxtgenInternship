import plotly.offline as py
import plotly.graph_objs as go


d1 = []
d2 = []
y = []
def defining(data1=[],data2=[],Labels=[]):
    global d1
    global d2
    global y
    d1=data1
    d2=data2
    y=Labels
def Plotting():
    trace=go.Bar(x=d1, y=d2, text=y, textposition='auto',marker=dict(
            color='rgb(158,202,225)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
            ),opacity=0.6)

    data=[trace]
    layout= go.Layout(title='Uptime for the different servers',xaxis=dict(title=' HOSTNAMES ',titlefont=dict(size=14)), yaxis=dict(title=' SERVER UPTIME ( in days ) ',titlefont=dict(size=14)))
    py.plot(go.Figure(data=data, layout=layout), filename='Uptime')

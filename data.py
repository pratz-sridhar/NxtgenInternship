
''' This File is responsible for retrieving all the data from the CSV files. These .csv files contain all the data which is need to be visualized.
    The pandas library is used to provide for Dataframes to help store and manipulate retrieved data.'''

import pandas as pd
import datetime
import time


se=[]                       # A list to store all the host names
sd=[]                       # A list to store days that each server has been up
st=[]                       # A list to store the time (in minutes) elapsed since the server was reset
ST=[]                       # A lsit to store the time in fotmat- HH:MM:SS


def extract(zone):          # A method to extract all the data of a zone which corresponds to a certain csv file
    global se
    global sd
    global st
    se=[]
    sd=[]
    st=[]
    if zone=='BLR':
        zone='BLR.csv'
    elif zone=='MUM':
        zone='MUM.csv'
    elif zone=='FDB':
        zone='FDB.csv'
    elif zone=='AMD':
        zone='AMD.csv'
    
    df=pd.read_csv(zone)    # here df is a dataframe which stores the data retrieved from the said csv file


    for i in df['HOSTNAME']:
        se.append(i)
    for i in df['DAYS']:
        sd.append(i)
    for i in df['TIME']:
        st.append(i)
        

def process_data():         # A method to convert the time from HH:MM:SS format to minutes equivalent, to enable easier plotting
    number=0
    global se
    global sd
    global st
    global ST

    for i in st:
        i=i+',000'
        x = time.strptime(i.split(',')[0],'%H:%M:%S')
        y=datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
        y=y/(60)
        '''y=0
        for c in i:
            if c.isdigit():
                y=(y*10)+int(c)
            else:
                break'''
        ST.append(y)
    return se,sd,ST,st



    
        



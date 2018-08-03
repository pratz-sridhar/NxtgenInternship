import pandas as pd
import datetime
import time


se=[]
sd=[]
st=[]
ST=[]


def extract(zone):
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
    
    df=pd.read_csv(zone)


    for i in df['HOSTNAME']:
        se.append(i)
    for i in df['DAYS']:
        sd.append(i)
    for i in df['TIME']:
        st.append(i)
        

def process_data():
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



    
        



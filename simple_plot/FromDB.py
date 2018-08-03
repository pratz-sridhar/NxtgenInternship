
import mysql.connector
print()
ah=[]

'''ah2=[]
ah3={}'''
def fromdb():
    global ah1
    con=mysql.connector.connect(host="localhost",user="root",password="",database="fourth")
    cursor=con.cursor()
    if con.is_connected():

        cursor.execute("SELECT * FROM server3")

    for row in cursor.fetchall():
        ah.append(row)
    ah1=dict(ah)

    '''for key in sorted(ah1):
        ah2.append((key,ah1[key]))
    ah3=dict(ah2)'''

    return ah1

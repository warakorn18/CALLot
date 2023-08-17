import pandas as pd
import numpy as np
import mysql.connector
import psycopg2
from datetime import datetime
import time

def Program_Cal() :
    connection = psycopg2.connect(user="admin",
                                  password="Ab123456",
                                  host="191.191.2.197",
                                  port="5432",
                                  database="Totle-2nd-Mask")
    print("connect MySQL")
    mycox = connection.cursor()
    mycox.execute("select * from twomask_cpk;")
    records = mycox.fetchall()
    df = pd.DataFrame(records)

    df.drop([0], axis=1, inplace=True)

    df.to_csv("a.csv",index=False)

    rd = pd.read_csv("a.csv",index_col=False)
    rd.reset_index(drop=True)
    x = input('>>>>')
    rd = rd.loc[rd['6'] == z1]
    # # rd = rd.reset_index()
    print(rd)

    LSL = 4.4
    USL = 4.8
    number = [LSL,USL]
    target = sum(number)/len(number)
    print("Ave >>",target)
    CPK_lost = z1

    def Cpk(mylist, usl, lsl):
            arr = np.array(mylist)
            arr = arr[~np.isnan(arr)]
            arr = arr.ravel()
            sigma = np.std(arr)
            m = np.mean(arr)
            Cpu = float(usl - m) / (3 * sigma)
            Cpl = float(m - lsl) / (3 * sigma)
            Cpk = np.min([Cpu, Cpl])
            print(np.array(mylist))
            return Cpk

    Cpk_front_pos = Cpk(rd["1"],USL,LSL)
    Cpk_front_width = Cpk(rd["2"],USL,LSL)
    Cpk_back_pos = Cpk(rd["3"],USL,LSL)
    Cpk_back_width = Cpk(rd["4"],USL,LSL)

    datacpk_front_pos = '%.4f'%(Cpk_front_pos)
    datacpk_front_width = '%.4f'%(Cpk_front_width)
    datacpk_back_pos = '%.4f'%(Cpk_back_pos)
    datacpk_back_width = '%.4f'%(Cpk_back_width)

    print('Cpk-front_pos   >>>',datacpk_front_pos)
    print('Cpk-front_width >>>',datacpk_front_width)
    print('Cpk-back_pos    >>>',datacpk_back_pos)
    print('Cpk-back_width  >>>',datacpk_back_width)
    print('lost production',CPK_lost)
    pratname = 'ECASD60J337M009KA0+C001/K803'


    dt = datetime.now()

    ts =datetime.timestamp(dt)

    date_time = datetime.fromtimestamp(ts)

    times = date_time.strftime("%d-%m-%Y  %H:%M:%S")
    print("date and time is :",dt)
    print("Result 1:", times)

    connection = psycopg2.connect(user="admin",
                                  password="Ab123456",
                                  host="191.191.2.197",
                                  port="5432",
                                  database="Totle-2nd-Mask")
# connection

    cursor = connection.cursor()


    a = "INSERT INTO cpk_data(cpk_lost ,cpk_front_pos, cpk_front_width, cpk_back_pos, cpk_back_width,partname,d,times) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    b = (CPK_lost, datacpk_front_pos, datacpk_front_width, datacpk_back_pos, datacpk_back_width,pratname,dt,times)
    cursor.execute(a,b)
    connection.commit()
    print("INSERT INTO SUBMIT MY DATABASE PG ADMIN")


try :
    z = '1'
    z1 = '1'
    staus = True
    a = 1
    b = 1
    while staus:
        if staus == True:
            
            while True:
                time.sleep(1)
                x = input('>>>>>>>')
                # x = 3
                if x != z :
                    print('Z1 >>',z)
                    z = x
                    print('Z1.1 >>',z)
                    c = a + b
                    # print(c)
                    a = c   
                    if c >= 3:
                        print('333333333')
                        print('Z2.1 >>',z1)
                        print('Z2 >>',z)
                        Program_Cal()
                        print('sec')
                        c = 2
                        print(c)
                        break
                    break
                else:
                    print('non')
                    z1 = z
            
        else:
            print('111111')

except Exception as e:
    print('>>>>>>>',e)
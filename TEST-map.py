import psycopg2

mydb = psycopg2.connect(                    user ='admin',
                                            host="191.191.2.179",
                                            password="Ab123456",
                                            port='5432',
                                            database='Totle-2nd-Mask'
                                            )
print("connect MySQL")
mycox = mydb.cursor()
mycox.execute("select * from cpk_data ORDER By id ASC;")
records = mycox.fetchall()



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
                if x != z :
                    z = x
                    c = a + b
                    a = c
                    if c == 3 :
                        print('program')
                    else:
                        break
                else:
                    print('non')
                    
        else:
            print('111111')

except Exception as e:
    print('>>>>>>>',e)
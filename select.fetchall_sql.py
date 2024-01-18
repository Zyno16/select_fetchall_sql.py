import mysql.connector
try :
     conn =mysql.connector.connect(
        user ="userpython",
        host ="localhost",
        passwd ="123456",
        database ="arabicinfo"
     )

     cur =conn.cursor()
     cur.execute("select * from emp")
     result =cur.fetchall()
     for x in result:
        print(x)
     print(type(result))#to know the type
     cur.execute("select * from emp where empname like'A%'")
     result1 =cur.fetchall()
     for x in result:
        print(x)
     print(type(result1))#to know the type

except mysql.connector.Error as e:
    print (e)
    

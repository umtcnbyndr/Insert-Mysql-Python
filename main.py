import mysql.connector

def schooldatabase(name,price,imageUrl,description):
    mydb=mysql.connector.connect(host="localhost",user="root",password="zxc159cxz",database="node-app")
    cursor=mydb.cursor()

    sql="INSERT INTO products(name,price,imageUrl,description) VALUES(%s,%s,%s,%s)"
    values=(name,price,imageUrl,description)

    cursor.execute(sql,values)
    
    try:
        mydb.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi ")
        print(f"son eklenen kaydın id {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata",err)
    finally:
        mydb.close()
        print("database bağlantisi kapandi.")

name=input("ürün adi: ")
price=float(input("ürün fiyati: "))
imageUrl=input("ürün fotoğrafi: ")
description=input("ürün durumu: ")

schooldatabase(name,price,imageUrl,description)


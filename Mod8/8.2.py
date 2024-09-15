import mysql.connector


yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user="N1K0",
         password="S4RV4R",
         autocommit=True
         )
def hae_kentta(maakoodi):
    sql =(f"SELECT type, COUNT(*) FROM airports WHERE iso_country ='{maakoodi}'")
    print(sql)
    cursor=yhteys.cursor()
    cursor.execute(sql)
    tulo=cursor.fetchall()
    if cursor.rowcount >0 :
        if tulo:
          for asema, maara in tulo:
            print(f"{asema}:{maara}")
        else:
            print("Virhe")

maakoodi=input("Anna maakoodi (esim. FI)")
hae_kentta(maakoodi)
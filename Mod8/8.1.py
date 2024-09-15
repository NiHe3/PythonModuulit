import mysql.connector
yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user="N1K0",
         password="S4RV4R",
         autocommit=True
         )

def haku(koodi):
    sql=f"SELECT name FROM airport WHERE ident='{koodi}'"

    print(sql)
    cursor=yhteys.cursor()
    cursor.execute(sql)
    tulo=cursor.fetchone()
    if cursor.rowcount >0 :
        if tulo:
            nimi = tulo
            print(f"ICAO koodi {koodi} on lentoasema {nimi}")
        else:
            print("Virhe etsiessä ICAO koodia")

koodi = input("Anna ICAO-koodi")
haku(koodi)
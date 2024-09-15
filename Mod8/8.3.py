import mysql.connector
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user="N1K0",
         password="S4RV4R",
         autocommit=True
         )

def koordinaatit(icao_koodi):
    sql = (f"SELECT latitude_deg, longitude_deg FROM airports WHERE ident ='{icao_koodi}'")
    print(sql)
    cursor = yhteys.cursor()
    cursor.execute(sql)
    tulo = cursor.fetchall()
    if cursor.rowcount > 0:
        if tulo:
            return tulo
        else:
            print("Virhe")
def lasku(lentokentta1, lentokentta2):
    koord1=koordinaatit(lentokentta1)
    koord2=koordinaatit(lentokentta2)

    etaisuus=geodesic(koord1,koord2). kilometers
    print(f"Lentoasemien välinen etäisyys on {etaisuus} kilometriä")

lentokenta1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
lentokenta2 = input("Anna toisen lentokentän ICAO-koodi: ")

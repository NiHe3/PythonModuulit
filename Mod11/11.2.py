from Auto import *

sahko = Sahkoauto("ABC-15", 180,  52.5)
poltto=Polttomootoriauto("ACD-123",165,32.3)

sahko.kiihdyta(120)
poltto.kiihdyta(130)

sahko.kulje(3)
poltto.kulje(3)

print(f"Sähköauto ({sahko.tunnus}, kuljettumatka {sahko.kmatka} KM) \n Polttomoottoriauto ({poltto.tunnus}, Kuljettumatka {poltto.kmatka} KM))")
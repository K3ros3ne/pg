def cislo_text(cislo):
    digit = int(cislo)
    digits = ["nula","jeden", "dva", "tri", "ctyri", "pet", "sest", "sedm", "osm", "devet"]
    number = ["deset", "dvacet", "tricet", "ctyricet", "patdesat", "sestdesat", "sedmdesat", "osmdesat", "devedesat"]
    numberDecad = ["jedenact", "dvana71ct", "trinact", "ctyrnact", "patnact", "sestnact", "sedmnact", "osmnact", "devetenact"]
    
    if digit != 100:
     if  digit < 10:
         answer = digits[digit]    
     if digit > 19:
         digitStr = str(digit)    
         digit1 = int(digitStr[0]) - 1
         digit2 = int(digitStr[1])
         if digit2 == 0:
          answer = number[digit1]
         else:    
          answer = number[digit1] + " " + digits[digit2]
     if (digit > 10 and digit <= 19):
        answer = numberDecad[digit - 11]

    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
     return answer
    if digit == 100:
       return "sto"

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)

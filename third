def je_prvocislo(cislo):
 if cislo <= 1:
  return False
 for i in range(2, int(cislo**0.5) + 1): 
  if cislo % i == 0:                     
     return False                   
 return True

def vrat_prvocisla(maximum):
 prvocisla = []
 for i in range(2, maximum + 1):
    if je_prvocislo(i):
            prvocisla.append(i)
 return prvocisla



if __name__ == "__main__":
    cislo = input("Zadej maximum: ")
    cislo = int(cislo)
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)

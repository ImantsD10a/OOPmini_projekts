
# Klase "Gramata" glabā informāciju par vienu grāmatu

class Gramata:
    def __init__(self, nosaukums, autors, gads):
        # Katras grāmatas īpašības (dati)
        self.nosaukums = nosaukums
        self.autors = autors
        self.gads = gads

    # Šī metode nosaka, kā grāmata tiks parādīta, kad to izdrukā ar print()
    def __str__(self):
        return f"{self.nosaukums} - {self.autors} ({self.gads})"


# Klase "Biblioteka" – glabā visu grāmatu sarakstu
# un satur metodes darbībām ar tām

class Biblioteka:
    def __init__(self):
        # Saraksts, kurā glabāsies visas grāmatas
        self.gramatas = []

 
    # Metode, lai pievienotu jaunu grāmatu
 
    def pievienot_gramatu(self):
        nosaukums = input("Ievadi grāmatas nosaukumu: ")
        autors = input("Ievadi autora vārdu: ")
        gads = input("Ievadi izdošanas gadu: ")

        # Izveido jaunu Gramata objektu un pievieno sarakstam
        self.gramatas.append(Gramata(nosaukums, autors, gads))
        print("Grāmata pievienota!")

    # Metode, kas parāda visas grāmatas
 
    def paradit_gramatas(self):
        if not self.gramatas:  # pārbauda, vai saraksts nav tukšs
            print("Bibliotēka ir tukša.")
        else:
            print("\nGrāmatu saraksts:")
            for i, g in enumerate(self.gramatas, start=1):
                print(f"{i}. {g}")

    
    # Metode grāmatas meklēšanai pēc nosaukuma vai autora
    
    def meklet_gramatu(self):
        teksts = input("Ievadi meklējamo vārdu: ").lower()
        # Izmanto saraksta izteiksmi, lai atlasītu tikai tās grāmatas,
        # kurās meklējamais teksts ir nosaukumā vai autorā
        atrastas = [g for g in self.gramatas if teksts in g.nosaukums.lower() or teksts in g.autors.lower()]

        if atrastas:
            print("Atrastās grāmatas:")
            for g in atrastas:
                print(g)
        else:
            print("Nekas netika atrasts.")

    
    # Metode, kas aprēķina statistiku
    # (vidējo grāmatu izdošanas gadu)
    
    def statistika(self):
        if not self.gramatas:
            print("Nav datu statistikai.")
        else:
            # Izvēlas tikai tos gadus, kas ir ievadīti kā cipari
            gadi = [int(g.gads) for g in self.gramatas if g.gads.isdigit()]

            if gadi:
                videjais = sum(gadi) / len(gadi)
                print(f"Vidējais izdošanas gads: {videjais:.1f}")
            else:
                print("Gadi nav korekti ievadīti.")



# Galvenā izvēlne, kas ļauj lietotājam vadīt programmu

def galvena_izvelne():
    biblioteka = Biblioteka()  # Izveido bibliotēkas objektu

    # Galvenais cikls – darbojas, kamēr lietotājs neizvēlas iziet (0)
    while True:
        print("\n=== BIBLIOTĒKAS SISTĒMA ===")
        print("1. Pievienot grāmatu")
        print("2. Parādīt grāmatas")
        print("3. Meklēt grāmatu")
        print("4. Statistika")
        print("0. Iziet")

        izvele = input("Izvēlies darbību: ")

        # Pārbauda, ko lietotājs izvēlējās un izsauc attiecīgo metodi
        if izvele == "1":
            biblioteka.pievienot_gramatu()
        elif izvele == "2":
            biblioteka.paradit_gramatas()
        elif izvele == "3":
            biblioteka.meklet_gramatu()
        elif izvele == "4":
            biblioteka.statistika()
        elif izvele == "0":
            print("Programma beidza darbu.")
            break
        else:
            print("Nepareiza izvēle! Mēģini vēlreiz.")



# Programmas starts

if __name__ == "__main__":
    galvena_izvelne()

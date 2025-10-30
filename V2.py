import json

# ==========================
# 1. klase – Gramata
# ==========================
class Gramata:
    def __init__(self, nosaukums, autors, gads):
        self.nosaukums = nosaukums
        self.autors = autors
        self.gads = gads

    def __str__(self):
        return f"{self.nosaukums} — {self.autors} ({self.gads})"


# ==========================
# 2. klase – Biblioteka
# ==========================
class Biblioteka:
    def __init__(self):
        self.gramatas = []

    def pievieno_gramatu(self):
        nosaukums = input("Ievadi grāmatas nosaukumu: ")
        autors = input("Ievadi autora vārdu: ")
        try:
            gads = int(input("Ievadi izdošanas gadu: "))
        except ValueError:
            print("Gadam jābūt skaitlim.")
            return
        gramata = Gramata(nosaukums, autors, gads)
        self.gramatas.append(gramata)
        print("Grāmata pievienota.")

    def paradit_gramatas(self):
        if not self.gramatas:
            print("Bibliotēka ir tukša.")
            return
        print("\n--- VISAS GRĀMATAS ---")
        for i, g in enumerate(self.gramatas, 1):
            print(f"{i}. {g}")

    def meklet(self):
        teksts = input("Ievadi meklējamo vārdu (nosaukumā vai autorā): ").lower()
        atrastas = [g for g in self.gramatas if teksts in g.nosaukums.lower() or teksts in g.autors.lower()]
        if atrastas:
            print("\n--- ATRASTĀS GRĀMATAS ---")
            for g in atrastas:
                print(g)
        else:
            print("Nekas netika atrasts.")

    def kartot(self):
        if not self.gramatas:
            print("Nav datu, ko kārtot.")
            return
        print("Kārtot pēc: 1 - nosaukuma | 2 - gada")
        izvele = input("Izvēlies: ")
        if izvele == "1":
            self.gramatas.sort(key=lambda g: g.nosaukums)
            print("Grāmatas sakārtotas pēc nosaukuma.")
        elif izvele == "2":
            self.gramatas.sort(key=lambda g: g.gads)
            print("Grāmatas sakārtotas pēc gada.")
        else:
            print("Nepareiza izvēle.")

    def dzest(self):
        self.paradit_gramatas()
        try:
            numurs = int(input("Ievadi dzēšamās grāmatas numuru: "))
            if 1 <= numurs <= len(self.gramatas):
                dzesta = self.gramatas.pop(numurs - 1)
                print(f"Dzēsta: {dzesta}")
            else:
                print("Nepareizs numurs.")
        except ValueError:
            print("Ievadi skaitli.")

    def statistika(self):
        if not self.gramatas:
            print("Nav datu statistikai.")
            return
        videjais_gads = sum(g.gads for g in self.gramatas) / len(self.gramatas)
        jaunaka = max(self.gramatas, key=lambda g: g.gads)
        vecaka = min(self.gramatas, key=lambda g: g.gads)
        print("\n--- STATISTIKA ---")
        print(f"Vidējais izdošanas gads: {videjais_gads:.1f}")
        print(f"Vecākā grāmata: {vecaka}")
        print(f"Jaunākā grāmata: {jaunaka}")

    def saglabat_faila(self):
        dati = [{"nosaukums": g.nosaukums, "autors": g.autors, "gads": g.gads} for g in self.gramatas]
        with open("biblioteka.txt", "w", encoding="utf-8") as f:
            json.dump(dati, f, ensure_ascii=False, indent=2)
        print("Dati saglabāti failā biblioteka.txt.")

    def ieladet_no_faila(self):
        try:
            with open("biblioteka.txt", "r", encoding="utf-8") as f:
                dati = json.load(f)
            self.gramatas = [Gramata(d["nosaukums"], d["autors"], d["gads"]) for d in dati]
            print("Dati ielādēti no faila biblioteka.txt.")
        except FileNotFoundError:
            # Fails var nebūt, tas nav kļūda — vienkārši sākam ar tukšu bibliotēku
            pass
        except (json.JSONDecodeError, KeyError):
            print("Fails ir bojāts vai satur nepareizu formātu.")


# ==========================
# Galvenā programmas izvēlne
# ==========================
def galvena_izvelne():
    biblioteka = Biblioteka()
    biblioteka.ieladet_no_faila()

    while True:
        print("\n===== BIBLIOTĒKAS SISTĒMA =====")
        print("1. Pievienot grāmatu")
        print("2. Parādīt visas grāmatas")
        print("3. Meklēt grāmatu")
        print("4. Kārtot grāmatas")
        print("5. Dzēst grāmatu")
        print("6. Statistika")
        print("7. Saglabāt failā")
        print("0. Iziet")
        izvele = input("Izvēlies darbību: ")

        if izvele == "1":
            biblioteka.pievieno_gramatu()
        elif izvele == "2":
            biblioteka.paradit_gramatas()
        elif izvele == "3":
            biblioteka.meklet()
        elif izvele == "4":
            biblioteka.kartot()
        elif izvele == "5":
            biblioteka.dzest()
        elif izvele == "6":
            biblioteka.statistika()
        elif izvele == "7":
            biblioteka.saglabat_faila()
        elif izvele == "0":
            print("Programma beidz darbu.")
            break
        else:
            print("Nepareiza izvēle. Lūdzu, izvēlies no saraksta.")

if __name__ == "__main__":
    galvena_izvelne()

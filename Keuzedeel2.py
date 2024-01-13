import random
 
class SlotMachine:
    def __init__(self, rijen, kolommen, symbool_aantal, symbool_waarde, credits):
        self.rijen = rijen
        self.kolommen = kolommen
        self.symbool_aantal = symbool_aantal
        self.symbool_waarde = symbool_waarde
        self.credits = credits



    def spin(self, speler):
        
        lijnen = speler.krijg_aantal_lijnen()
        inzet = speler.krijg_inzet()
        totale_inzet = inzet * lijnen
        if totale_inzet > self.credits:
            print(f"Je bent blut")
            return
        print(f"Je biedt nu €{inzet} op {lijnen} lijnen. Je hebt €{totale_inzet} ingezet")
        self.credits -= totale_inzet
        slots = self.krijg_slotmachine_spin()
        self.print_slotmachine(slots)
        winst, winnende_lijnen = self.controleer_winst(slots, lijnen, inzet)
        print(f"Je hebt €{winst} gewonnen!")
        print(f"de winnende lijn(en):", *winnende_lijnen)
        self.credits + winst

    def controleer_winst(self, kolommen, lijnen, inzet):
        winst = 0
        winnende_lijnen = [] 
        for lijn in range(lijnen):
            symbool = kolommen[0][lijn]
            for kolom in kolommen:
                symbool_te_controleren = kolom[lijn]
                if symbool != symbool_te_controleren:
                    break
            else:
                winst + self.symbool_waarde[symbool] * inzet
                winnende_lijnen.append(lijn + 1)
        return winst, winnende_lijnen

    def krijg_slotmachine_spin(self):
        all_symbols = []
        for symbol, symbol_count in self.symbool_aantal.items():
            for _ in range(symbol_count):
                all_symbols.append(symbol)
        columns = []
        for _ in range(self.kolommen):
            column = []
            current_symbols = all_symbols[:]
            for _ in range(self.rijen):
                value = random.choice(current_symbols)
                current_symbols.remove(value)
                column.append(value)
            columns.append(column)
        return columns

    def print_slotmachine(self, columns):
        for row in range(len(columns[0])):
            for i, column in enumerate(columns):
                if i != len(columns) - 1:
                    print(column[row], end="|")
                else:
                    print(column[row], end="|")
            print()


class Speler:
    def __init__(self, naam, bedrag):
        self.naam = naam
        self.bedrag = bedrag

    def storting(self):
        while True:
            bedrag = input(f"Hoeveel credits wil je mee gokken? ")
            if bedrag.isdigit():
                bedrag = int(bedrag)
                if bedrag > 0:
                    break
                else:
                    print("Het aantal moet boven de 0 zijn")
            else:
                print("Voer een nummer in")
        self.bedrag = bedrag

    def krijg_aantal_lijnen(self):
        while True:
            lijnen = input("Op welke lijnen wil je bieden. 1, 2 of 3? ")
            if lijnen.isdigit():
                lijnen = int(lijnen)
                if 1 <= lijnen <= 3:
                    break
                else:
                    print("1, 2 of 3.")
            else:
                print("Voer een nummer in")
        return lijnen

    def krijg_inzet(self):
        while True:
            bedrag = input("Hoeveel wil je op deze lijn inzetten? €")
            if bedrag.isdigit():
                bedrag = int(bedrag)
                if 1 <= bedrag <= 100:
                    break
                else:
                    print("Het bedrag moet tussen €1 en €100 liggen.")
            else:
                print("Voer een nummer in.")
        return bedrag


def hoofdprogramma():
   
    slotmachine = SlotMachine(
        rijen=3,
        kolommen=3,
        symbool_aantal={
            "∞": 2,
            "♡": 4,
            "☼": 6,
            "✯": 8
        },
        symbool_waarde={
            "∞": 5,
            "♡": 4,
            "☼": 3,
            "✯": 2
        },
        credits=1000
    )

    speler = Speler(naam="Speler", bedrag=0)

    speler.storting()

    while True:
        print(f"Je hebt nu €{speler.bedrag}")
        antwoord = input("Druk op enter om te spelen of q om te stoppen. ")
        if antwoord.lower() == "q":
            break
        slotmachine.spin(speler)
        if speler.bedrag == 0:
            print("Je hebt geen geld meer. Bedankt voor het spelen!")
            break

    print(f"Je hebt nu nog €{speler.bedrag}")
 
 
hoofdprogramma()
  
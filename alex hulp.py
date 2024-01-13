# abstract class Auto():
 #    merk
 #    aantal_deuren=2
#     aantal_cylinders=4
#     kleur="zwart"
 #    aantal_wielen=4
 
#     def vermogen():
#         return aantal_cylinders * 576


# class Nissan(Auto):
#     merk="Nissan"


# auto = Auto(merk="Nissan")
# print(auto.vermogen())

# nissan = Nissan(kleur="rood")

# class Vrachtwagen(Auto):
#     vrachtlengte
#     aantal_wielen=8



# class Mierenhoop():
#     def aantal_mieren(:)
#         Mieren.aantal(this)


# class Mier():
#     Mierenhoop()
#     heeft_voedsel_gevonden
#     positie_voedsel
#     hoeveelheid_voedsel_bij_me
# 
#     def aangetikt_worden():
 #        "Ga naar voedsel"
# 
#     def aantikken_andere_mier(andere_mier):
#         if heeft_voedsel_gevonden:
#             andere_mier.aangetikt_worden)
# 
#     def voedsel_vinden:
#         heeft_voedsel_gevonden = True
#         positie_voedsel = huidige_positie
#     
#    def voedsel_meenemen(hoeveelheid):
#         heeft_voedsel_gevonden = True
#         hoeveelheid_voedserl_gevonden = hoeveelheid



#class SlotMachine():
 #   SYMBOL_COUNTS = {
  #      "∞": 2,3     "♡": 4    "☼": 6,"✯": 8 }

    #symbol_value = {
     #   "∞": 5,
      #  "♡": 4,
        # "☼": 3,
       # "✯": 2
    # }

    #credits = 0

    #def inzet (self, credits):
     #   self.credits = self.credits + credits

    #def opbrengst():

    #def uitbetalen(self):
  #      print(f"U heeft {self.credits} uitbetaald gekregen")
 #       self.credits = 0

   # def rollen(self):
    #    if self.credits <= 0:
     #3       print("Je bent blut")
       #     return
        
        #self.credits = self.credits - 1

        # hier komt de berekening van de uitkomst van het draaien van de wielen
        #uitkomst = 100
        
        #self.credits = self.credits + uitkomst

   





#my_slotmachine = SlotMachine()
#print(my_slotmachine.credits)    // 0
#my_slotmachine.inzet(10)
#print(my_slotmachine.credits)    // 10
#my_slotmachine.rollen()
#my_slotmachine.rollen()
#print(my_slotmachine.credits)    // 208
#my_slotmachine.uitbetalen()
#my_slotmachine.uitbetalen()
    




#main()eafoinaoeinmfoiamfoiamefoamfoiamfioemoifmaeofaekfmaolef

















    class SlotMachine():
    
    SYMBOL_COUNTS = {
        "∞": 2,
        "♡": 4,
        "☼": 6,
        "✯": 8
    }

    symbol_value = {
        "∞": 5,
        "♡": 4,
        "☼": 3,
        "✯": 2
    }

    credits = 0

    def inzet (self, credits):
        self.credits = self.credits + credits

    def opbrengst():
        ...

    def uitbetalen(self):
        print(f"U heeft {self.credits} uitbetaald gekregen")
        self.credits = 0

    def rollen(self):
        if self.credits <= 0:
            print("Je bent blut")
            return
        
        self.credits = self.credits - 1

        # hier komt de berekening van de uitkomst van het draaien van de wielen

        

        
        uitkomst = 100
        
        self.credits = self.credits + uitkomst
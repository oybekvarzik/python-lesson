class Avto:
    def __init__(self, model, rangi, korobka, narx):
        self.model=model
        self.rangi=rangi
        self.korobka=korobka
        self.narx=narx
        self.kilometer=100
    def  get_info(self):
        return f"Mashina modeli {self.model} bolib {self.rangi} rangda va {self.korobka} narxi {self.narx}$ yurgan masofasi {self.kilometer}km"

    def update_km(self):
         self.kilometer+=20

mashina1=Avto("GM", "qora", "mexanik", 15000)
mashina2=Avto("KIA", "oq", "avtomat", 45000)
mashina3=Avto("HUNDYI", "qizil", "avtomat", 55000)
mashina4=Avto("TAYOTA", "green", "avtomat", 65000)
mashina2.update_km()
# print(mashina4.get_info())
# print(mashina2.get_info())

class Avtosalon:
    def __init__(self, salon_nomi):
        self.salon_nomi=salon_nomi
        self.manzil=mazil="qoyliq"
        self.Avtomolbilar_soni=0
        self.avtobillar=[]
    def get_car(self):
        return [car.get_info() for car in self.avtobillar]
    def add_car(self, car):
        self.avtobillar.append(car)
        self.Avtomolbilar_soni+=1

salon1=Avtosalon("K5")
salon1.add_car(mashina1)
salon1.add_car(mashina2)
salon1.add_car(mashina3)

print(salon1.Avtomolbilar_soni)
print(salon1.get_car())
def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('')]
print(see_methods(Avto))
# dict=salon1.__dict__
print(dict)
print(dir(Avto))


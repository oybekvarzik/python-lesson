
class Talaba:
    def __init__(self, ism, familya, t_yil):
        self.ism=ism
        self.familya=familya
        self.t_yil=t_yil
        self.bosqich=1
    def get_info(self):
        return f"{self.ism} {self.familya}. {self.bosqich}-bosqich talabasi"

    def set_bosqich(self, yangi_bosqich):
        self.bosqich=yangi_bosqich
    def update(self):
        self.bosqich+=1

    def get_name(self):
        return self.ism
    def tanishtir(self): # bu metod hisoblanadi
        return f"salom mening ismim {self.ism} familyam {self.familya}  {self.t_yil}  yilda tugulganman"

talaba1=Talaba("Olim", "Olimov", 2000)
talaba2=Talaba("Haydar", "Hakimov" , 1995)
talaba3=Talaba("Ali", "Alimov", 1992)
talaba4=Talaba("alijon", "Valiyev", 1992)
'''
print(talaba4.tanishtir())
print(talaba2.get_name())
print(talaba3.bosqich)
talaba1.bosqich=4
print(talaba3.get_info())
talaba4.set_bosqich(5)
print(talaba4.get_info())
talaba2.update()
print(talaba2.get_info())'''


# yangi Class



class Fan():
    def __init__(self,nomi):
        self.nomi=nomi
        self.talabalar_soni=0
        self.talabalar=[]
    def get_student(self):
        """Fanga yozilgan talabalar royxati"""
        return [talaba.get_info() for talaba in self.talabalar]

    def add_student(self, talaba):
        """Fanga talabalar qowiw"""
        self.talabalar.append(talaba)
        self.talabalar_soni+=1


matem=Fan("Fizik")
print(matem.talabalar_soni)
matem.add_student(talaba1)
matem.add_student(talaba2)
matem.add_student(talaba3)
matem.add_student(talaba4)

print(matem.talabalar[0].get_info())
print(matem.get_student())
print(dir(Talaba))
def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('')]


# print(see_methods(Talaba))
dict=talaba4.__dict__.keys()
dict1=talaba2.__dict__
dict2=talaba3.__dict__

print(dict)
print(dict1)
print(dict2)


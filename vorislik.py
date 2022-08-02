class Shaxs:
    def __init__(self, ism, familiya, passport, tyil):
        self.ism=ism
        self.familiya=familiya
        self.passport=passport
        self.tyil=tyil
    def get_info(self):
        """informatin about person"""
        info=f"{self.ism}  {self.familiya}."
        info+=f"{self.passport}  {self.tyil}"
        return info
    def get_age(self,age):
        """return age of person"""
        return age-self.tyil
inson=Shaxs("ALi","hoshimov", "AA 564751", 1992 )
# print(inson.get_info())
# print(inson.get_age(2022))

"""Voris Class"""

class Talaba(Shaxs):
    def __init__(self, ism , familiya, passport, tyil, ID, manzil):
        super().__init__( ism, familiya, passport, tyil)
        self.ID=ID
        self.bosqich=1
        self.manzil=manzil
        self.fanlar=[]
    def get_id(self):
        return self.ID

    def get_bosqich(self):
        return self.bosqich
    def update(self):
        self.bosqich+=1



# Polimorfizm
    def get_info(self):

        info = f"{self.ism}  {self.familiya}."
        info += f"{self.passport} {self.get_bosqich()} bosqichda oqiydi {self.tyil} da tugulgan bolib , ID raqami: {self.ID} "
        return info

    def fanga_yozil(self,fan):
        self.fanlar.append(fan)

class Fan(Talaba):
    def __init__(self, fanlar):
        super().__init__(fanlar )




fanlar1=Fan("matematika")
# fanlar2=Talaba('ximiya')
fanlar1.fanga_yozil()


# Obyekt ichida obyekt

class Manzil:
    def __init__(self, uy , kocha , tuman , viloyat):
        self.uy=uy
        self.kocha=kocha
        self.tuman=tuman
        self.viloyat=viloyat
    def get_manzil(self):
        manzil=f" {self.viloyat} viloyati  {self.tuman} tuman  "
        manzil+=f"kocha {self.kocha} {self.uy}-xonadon ,  "
        return manzil



talaba1_manzil=Manzil(4, "Olmazor", "Chust", "Namangan")

talaba1=Talaba("Aziz", "Xoliqov", "AA212121", 1995,"N416516518", talaba1_manzil )
print(talaba1.manzil.get_manzil())
#
# talaba1.update()
# talaba1.update()
# get=talaba1.get_info()
# get1=talaba1.get_age(2022)


# print(talaba1.get_info())




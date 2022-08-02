from uuid import uuid4
class Avto:
    """ bu classdan necha mart foydalanganini bildiradi , yani nechi kiwi kirganini bildirar ekan"""

    __numavto=0
    def __init__(self, make, model, rang, yil, narx, km=0):
        """Avtomobilning xususiyatlari"""
        self.make=make
        self.model=model
        self.rang=rang
        self.yil=yil
        self.narx=narx
        self.__km=km
        self.__id=uuid4()
        Avto.__numavto+=1

    @classmethod
    def get_num_avto(cls):
        return cls.__numavto

    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id

    def add_km(self, km):
        """Mashinaga km ha yana km qowiw"""
        if km>=0:
            self.__km+=km

        else:
            print("Mashina km kamaytirib bolmaydi")


# print(avto1.numavto)
# print(Avto.get_num_avto())
# print(avto1.get_num_avto())
# print(avto1.narx)
# avto1.add_km(5200)
# print(avto1.get_km())
# print(avto1.get_id())

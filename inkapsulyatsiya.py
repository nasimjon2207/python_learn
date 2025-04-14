

from uuid import uuid4
class Avto:
    def __init__(self,make,model,rangi,yil,narx,km=0):
        self.make=make
        self.model=model
        self.rangi=rangi
        self.yil=yil
        self.narx=narx
        self.__km=km
        self.__id=uuid4()



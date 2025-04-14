
class shaxs:
    def __init__(self, ism, familiya, passport, tyil):
        self.name=ism
        self.surname=familiya
        self.passport=passport
        self.birth=tyil
        
    def get_info(self):
        info=f"{self.name}, {self.surname} ."
        info+=f" passport:{self.passport}, {self.birth}-yilda tug'ulgan"
        return info
    def get_age(self,yil):
        return yil-self.birth
inson=shaxs('Nasimjon', 'Xudayberdiyev', 'AB7332463',2001)


class Talaba(shaxs):
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam=idraqam
        self.bosqich=1
        self.manzil=manzil
    
    def get_id(self):
        return self.idraqam
    def get_bosqich(self):
        return self.bosqich
    def get_info(self):
        info=f"{self.name}, {self.surname}"
        info+=f" passport:{self.passport}, ID raqam:{self.idraqam}, {self.bosqich}-bosqich {self.birth}-yilda tug'ulgan"
        return info

class Manzil:
    def __init__(self,uy,kucha,tuman,viloyat):
        self.house=uy
        self.street=kucha
        self.district=tuman
        self.viloyat=viloyat
        
    def get_manzil(self):
        manzil=f"{self.viloyat} viloyati, {self.district} tumani, "
        manzil+=f" {self.street} ko'chasi , {self.house}-uy"
        return manzil
    
talaba1_manzil=Manzil(22,"3 tor","Olvalizor","Namangan")
talaba1=Talaba('Mashxura','Maxmudova','AB73324225',2006,'AA12345678910',talaba1_manzil)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
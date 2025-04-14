
class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.name=ism
        self.surname=familiya
        self.birth=tyil
    def get_name(self):
        return self.name
    def get_age(self,year):
        return f"{year-self.birth}-yoshda"
    def get_surname(self):
        return self.surname
    def tanishtir(self):
        return f"Ismim {self.name} {self.surname} {self.birth}-yilda tug'ulganman"
    def get_fullname(self):
        return f"{self.name} {self.surname} {self.birth}"
talaba1=Talaba('Nasimxon','Xudayberdiyev',2011)
talaba2=Talaba('Mashxuraxon', 'Mahmudova', 2010)

class Fan:
    def __init__(self,nomi):
        self.nomi=nomi
        self.talabalar_soni=0
        self.talabalar=[]
        
    def add_student(self,talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni+=1
    def get_name(self):
        return self.nomi
    def get_students(self):
        # talabalar=[]
        # for talaba in self.talabalar:
        #     talabalar.append(talaba.get_fullname())
        # return talabalar
         return [talaba.get_fullname() for talaba in self.talabalar]
def see_method(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]
matem=Fan("Amaliy matematika")
talaba1=Talaba('Nasimjon','Xudayberdiyev',2001)
talaba2=Talaba('Mashxura', 'Mahmudova', 2006)
talaba3=Talaba('Ali',"Valiyev",2000)
talaba4=Talaba('Salim','Olimov',2003)
matem.add_student(talaba1)
matem.add_student(talaba2)
matem.add_student(talaba3)
matem.add_student(talaba4)

    
        
    
        




























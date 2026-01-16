class Drone:
    def __init__(self,DronId,model,pil,durum):
        self.DronId=DronId
        self.model=model
        self.pil=pil
        self.durum=durum

    def UcusYap(self, mesafe):
         self.mesafe=mesafe 
         if self.durum=="beklemede":
          if self.pil<20:
            print("uçuş için  pil ömrü yeterli değiildir.")
          else:
            print(f"{self.DronId} nolu dron   uçuyor...")

          self.pil=self.pil-mesafe    
          print (f"uçuş mesafesi sonrası kalan pil {self.pil}")   
         elif self.durum=="uçuşta":
             print(f"{self.DronId}  zaten uçuşta")
         else:
            print("HATA!!!")   
         

    def SarjEt(self):
        self.pil=100
        print(f"{self.DronId} nolu  dron şarj edildi şimdi pil durumu %100")  

    def __str__(self):
        return f"dron Id:{self.DronId}- model:{self.model}-  pil: {self.pil}-  durum:{self.durum}"


class KargoDron(Drone):
    def __init__(self, DronId, model, pil, durum, Yuk_kapasitesi):
        super().__init__(DronId, model, pil, durum)
        self.yuk=Yuk_kapasitesi


    def UcusYap(self, mesafe):
         self.mesafe=mesafe 
         if self.durum=="beklemede":
          if self.pil<20:
            print("uçuş için  pil ömrü yeterli değiildir.")
          else:
            print(f"{self.DronId} nolu dron  {self.yuk} kg yük ile uçuyor...")

          self.pil=self.pil-2*mesafe    
          print (f"uçuş mesafesi sonrası kalan pil {self.pil}")   
         else:
             print(f"{self.DronId}  zaten uçuşta")
         
         
         
         
class GuvenlikDronu(Drone):
    def __init__(self,DronId, model, pil, durum,gecegorusu):
        super().__init__(DronId,model,pil,durum,)  
        self.geceGorusu=gecegorusu

    def UcusYap(self, mesafe):
        self.mesafe=mesafe 
        if self.pil<20:
            print("uçuş için  pil ömrü yeterli değiildir.")
        else:
            print(f"{self.DronId} nolu dron kızılötesi tarama ile  uçuyor...")
            self.pil=self.pil-2*mesafe    
            print (f"uçuş mesafesi sonrası kalan pil {self.pil}") 


D1=Drone(1,"tesla",70,"beklemede")  
D1.SarjEt()
D1.UcusYap(20)
print("*"*40)

D2=KargoDron(2,"Bmw",90,"beklemede",80)
D2.UcusYap(30)
D2.SarjEt()
print("*"*40)

D3=GuvenlikDronu(3,"Samsung",50,"uçuşta",True)
D3.UcusYap(20)
D3.SarjEt()



         
         
         
         
         
         

    
import random
import csv
import re
from address import addressG
import rstr

class buildingG() :

    def __init__(self) :
        self.number = ""
        self.name = []
        self.phone = ""
        self.water = ""
        self.electricty = ""
        self.gas = ""
        self.apartment = ""
        self.address = ""
        self.contract = ""
        self.manager = ""
        self.parking = ""
        self.warehouse = ""
        self

    def set(self) :

        with open('../files/txt/buildingname.txt', 'r' , encoding='utf8') as f :
            w = f.read().split("  ")
            for x in w :
                self.name.append(x.replace("\n", ""))
        
        


    def get(self, n) :

    
        buildingG.set(self)  

        with open("../files/building.csv" , 'w' , newline ='' , encoding='utf8') as f :
            #num name phome wnum enum gnum anum address contract manager parking warehouse
            thewriter = csv.writer(f)

            for x in range(n) :
                address = []
                address = addressG().get()     #[0] = zcode , [1] = state , [2] = city , [3] = street , [4] = alley , [5] = No.
                for x in address :
                    self.address +=str(x) +  " - "
                self.address = self.address[6:-2]
                self.phone = str(address[0])+rstr.xeger(r'[0-9]{8}')
                self.water = rstr.xeger(r'[0-9]{1}\d[1]{1}\d[0-9]{3}\d[0-9]{8}')
                self.electricty = rstr.xeger(r'[0-9]{1}\d[2]{1}\d[0-9]{3}\d[0-9]{8}')
                self.gas = rstr.xeger(r'[0-9]{1}\d[3]{1}\d[0-9]{3}\d[0-9]{8}')
                self.apartment = str(random.randint(10,20))
                self.contract = "../files/1.pdf"
                self.manager = rstr.xeger(r'[1-9]{1}\d[0-9]{9}')
                with open('../files/help.txt' , 'w' , encoding='utf8') as f :
                    f.write("manager id : " + str(self.manager)+"\n" )
                self.parking = "../files/txt/parking.txt"
                self.warehouse = "../files/txt/warehouse.txt"
                self.number = rstr.xeger(r'[0-9]{5,10}')

                thewriter.writerow([str(self.number) , str(random.choice(self.name)) ,self.phone, self.water , self.electricty , self.gas , self.apartment ,
                 self.address , self.contract , self.manager , self.parking , self.warehouse])

                self.address = ""
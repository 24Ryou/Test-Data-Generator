# aptnum(0-30) - wcode(+aptnum) = ecode = gcode - owner(persons id) - apttype (tinyint 0,1 >> 0 = r , 1 = c) - 
# aptinfo(txt) - aptcharge(num)

from re import A
from secrets import randbelow
from building import buildingG
from Person import personG
import csv 
import pandas as pd
import random
import rstr

class apartmentG :

    def __init__(self) -> None:
        pass

    def set(self) :
        
        self.aptnum = ""
        self.wcode = ""
        self.ecode = ""
        self.gcode = ""
        self.owner = []
        self.apttype = ""
        self.aptinfo = ""
        self.aptcharge = []

    def get(self, n) :

        apartmentG.set(self)


        with open('../files/apartment.csv' , 'w' , newline='' , encoding='utf8') as f :
        
            thewriter = csv.writer(f)

            p = personG().get(n)

            colnames = ["Column1" , "Column2" , "Column3" , "Column4" , "Column5" , "Column6" , "Column7"]
            s = pd.read_csv('../files/person.csv', names=colnames)

           
            self.owner = s.Column4.to_list() 

            b = buildingG().get(5)

            temp = random.randint(0,5)
            #data2 = pd.read_csv('../files/building.csv' , skiprows=temp , header=None)
            with open("../files/building.csv" , newline='' , encoding='utf') as file :
                data = csv.reader(file , delimiter = ',')
                data2 = []
                d = []
                for row in data :
                    d.append(row[:])
                
                data2 = random.choice(d)
            # 3 4 5
            # for x in data2 :
            #   print('\n' + x)
                
            wid = str(data2[3])
            eid = str(data2[4])
            gid = str(data2[5])
            anum = int(data2[6])
            rndnum = random.sample(range(anum), n)
            for i in range(n) :
                
                self.aptnum = str(rndnum[i])
                self.wcode = wid + "-" + self.aptnum
                self.ecode = eid + "-" + self.aptnum
                self.gcode = gid + "-" + self.aptnum
                self.apttype = "0"
                self.aptinfo = "../files/txt/aptinfo.txt"
                self.aptcharge = rstr.xeger(r'[1-9]{1}[0]{7}')

                thewriter.writerow([self.aptnum , self.wcode , self.ecode , self.gcode , self.owner[i] , self.apttype
                , self.aptinfo , self.aptcharge ])








    

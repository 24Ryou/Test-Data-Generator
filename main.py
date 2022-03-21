from json import tool
import random
import csv
import re
import rstr
import pandas as pd
from  tools import *

class personG():

    def __init__(self):
        self.boys = []
        self.girls = []
        self.lastname = []
        self.phone = ""
        self.id = ""
        self.age = ""
        self.gender = ""
        self.access = ""

    def set(self) :

        with open("../files/txt/boys.txt" , 'r' , encoding='utf8') as f:
            #bl =[]
            for x in f:
                self.boys.append(x[:x.find(":")])
            #print(bl)

        with open("../files/txt/girls.txt" , 'r' , encoding='utf') as g:
           # gl =[]
            for x in g:
                self.girls.append(x[:x.find(":")])
            #print(gl)
        """ 
        for i in bl :
            self.boys.append(i)
        for i in gl :
            self.girls.append(i) """

        with open("../files/txt/lastname.txt" , 'r' , encoding='utf') as g:
            ln = g.read().splitlines()

            self.lastname = ln

        
    
    def get(self,n) :

        personG.set(self)


        with open('../files/person.csv' , 'w' , newline='' , encoding="utf8") as f:

            #fieldnames = ['name','lname','phone','id','age','gender','access']
            
            thewriter = csv.writer(f)


            #thewriter.writeheader()
            #thewriter.writerow(names[i] , lnames[i] , phone[i] , id[i] , age[i] , gender[i], 0 )

            for i in range(n) :

                girl = random.choice(self.girls)+""
                boy = random.choice(self.boys)+""
                lastname = random.choice(self.lastname)+""
                self.phone = "09"+str(random.randint(100000000,999999999))
                self.id = str(random.randint(1000000000,9999999999))
                self.age = str(random.randint(18,69))
                self.access = "0"

                g = random.randint(1,2)

                if g == 2 :
                    thewriter.writerow([girl, lastname , self.phone , self.id , self.age , "2" , self.access])
                else :
                   thewriter.writerow([boy, lastname , self.phone , self.id , self.age , "1" , self.access])

class buildingG() :

    def __init__(self) :
        self.bnumber = ""
        self.bname = []
        self.bphone = ""
        self.bwater = ""
        self.belectricty = ""
        self.bgas = ""
        self.bapartment = ""
        self.baddress = ""
        self.bcontract = ""
        self.bmanager = ""
        self.bparking = ""
        self.bwarehouse = ""

    def set(self) :

        with open('../files/txt/buildingname.txt', 'r' , encoding='utf8') as f :
            w = f.read().split("  ")
            for x in w :
                self.bname.append(x.replace("\n", ""))
        
        


    def get(self, n) :

    
        buildingG.set(self)  

        with open("../files/building.csv" , 'w' , newline ='' , encoding='utf8') as f :
            #num name phome wnum enum gnum anum address contract manager parking warehouse
            thewriter = csv.writer(f)

            for x in range(n) :
                address = []
                address = addressG().get()     #[0] = zcode , [1] = state , [2] = city , [3] = street , [4] = alley , [5] = No.
                for x in address :
                    self.baddress +=str(x) +  " - "
                self.baddress = self.baddress[6:-2]
                self.bphone = str(address[0])+rstr.xeger(r'[0-9]{8}')
                self.bwater = rstr.xeger(r'[0-9]{1}\d[1]{1}\d[0-9]{3}\d[0-9]{8}')
                self.belectricty = rstr.xeger(r'[0-9]{1}\d[2]{1}\d[0-9]{3}\d[0-9]{8}')
                self.bgas = rstr.xeger(r'[0-9]{1}\d[3]{1}\d[0-9]{3}\d[0-9]{8}')
                self.bapartment = str(random.randint(10,20))
                self.bcontract = "../files/1.pdf"
                self.bmanager = rstr.xeger(r'[1-9]{1}\d[0-9]{9}')
                with open('../files/help.txt' , 'w' , encoding='utf8') as f :
                    f.write("manager id : " + str(self.bmanager)+"\n" )
                self.bparking = "../files/txt/parking.txt"
                self.bwarehouse = "../files/txt/warehouse.txt"
                self.bnumber = rstr.xeger(r'[0-9]{5,10}')

                thewriter.writerow([str(self.bnumber) , str(random.choice(self.bname)) ,self.bphone, self.bwater , 
                self.belectricty , self.bgas , self.bapartment , self.baddress , self.bcontract , self.bmanager , 
                self.bparking , self.bwarehouse])

                self.baddress = ""  

class addressG() :

    def __init__(self):
        self.state = []    
        self.zcode = []  
        self.city = []
        self.street = []
        self.alley = []
        self.no = ""

    def set(self):

        with open("../files/txt/state.txt" , 'r' , encoding='utf8') as f :

            for x in f :
                self.state.append(x.replace("\n", ""))      #-------------- state

        with open("../files/txt/zcode.txt" , 'r' , encoding='utf8') as f :

            for x in f :
                self.zcode.append(x.replace("\n", ""))      #-------------- zcode

        with open("../files/txt/city2.txt" , 'r' , encoding='utf8') as f :

            data = f.read()
            list = data.split("\n")
            row = []

            for x in list :
                if x != "q" :
                    row.append(x)

                else:
                    self.city.append(row)                   #-------------- city
                    row = []

        with open("../files/txt/street.txt" ,'r' , encoding='utf8') as f :

            for x in f :
                self.street.append(x.replace("\n", ""))     #-------------- street
        

        with open("../files/txt/alley.txt" ,'r' , encoding='utf8') as f :

            for x in f :
                x = x.replace(" ", "")
                self.alley.append(x.replace("\n", ""))     #-------------- alley
        
        self.no = "پلاک"+" "+ str(random.randint(0,99))                     #-------------- No.
    
    def get(self) :
        
        addressG.set(self)
        
        n = random.randint(0,30)
        ex = ["" , str(random.randint(1,35))]
        city = random.choice(self.city[n])+""
        street = random.choice(self.street)+""
        alley = "کوچه" +" "+ random.choice(self.alley) + " " + random.choice(ex)
        address = []

        address.append(self.zcode[n])                       #------------  zcode
        address.append(self.state[n])                       #------------  state
        address.append(city)                                #------------  city
        address.append(street)                              #------------  street
        address.append(alley)                               #------------  alley
        address.append(self.no)                             #------------  No.
       
        return address

# aptnum(0-30) - wcode(+aptnum) = ecode = gcode - owner(persons id) - apttype (tinyint 0,1 >> 0 = r , 1 = c) - 
# aptinfo(txt) - aptcharge(num)

class apartmentG() :

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
        self.bid = ""
        self.aptid = [] # for account class useage

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
            self.bid = str(data[1])
            print("this is bid = " + data[1])    
            wid = str(data2[3])
            eid = str(data2[4])
            gid = str(data2[5])
            anum = int(data2[6])
            rndnum = random.sample(range(anum), n)
            for i in range(n) :
                
                self.aptnum = str(rndnum[i])
                self.aptid.append(self.aptnum)
                self.wcode = wid + "-" + self.aptnum
                self.ecode = eid + "-" + self.aptnum
                self.gcode = gid + "-" + self.aptnum
                self.apttype = "0"
                self.aptinfo = "../files/txt/aptinfo.txt"
                self.aptcharge = rstr.xeger(r'[1-9]{1}[0]{7}')

                thewriter.writerow([self.aptnum , self.wcode , self.ecode , self.gcode , self.owner[i] , self.apttype
                , self.aptinfo , self.aptcharge ])

        
    def getbid(self) : 
        apartmentG.set(self)
        return self.bid

    def getaptid(self) :
        apartmentG.set(self)
        return self.aptid

class accountG():

    def __init__(self) :
        self.password = ""
        
    def set(self) :
        
        self.password = ""
        self.bid = ""
        self.aptid = ""
        self.createdate = ""
        self.transaction  = ""
        self.message = ""
        self.file = ""

    def get(self, n):

       
            #pass - pid - bid -aptid - creationdate - trans - message - file
        with open('../files/account.csv' , 'w' , encoding='utf8') as f :
            thewriter = csv.writer(f)
            b = apartmentG()
            b.get(n)
            bid = b.getaptid()
            d = dateG()
            date = d.gettime(n)
            for i in range(n) :
                self.password = passwordG().passwordGenerator(10)
                self.bid = apartmentG().getbid()
                self.aptid = str(bid[i])
                self.createdate = str(date[i])
                thewriter.writerow([self.password , self.bid , self.aptid , self.createdate , "" , "" , ""])

a = accountG()
a.get(10)




     



    



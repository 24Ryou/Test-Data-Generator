import random

class addressG() :

    def __init__(self):
        self.state = []    
        self.zcode = []  
        self.city = []
        self.street = []
        self.alley = []
        self.no = ""

    def set(self):

        with open("./files/txt/state.txt" , 'r' , encoding='utf8') as f :

            for x in f :
                self.state.append(x.replace("\n", ""))      #-------------- state

        with open("./files/txt/zcode.txt" , 'r' , encoding='utf8') as f :

            for x in f :
                self.zcode.append(x.replace("\n", ""))      #-------------- zcode

        with open("./files/txt/city2.txt" , 'r' , encoding='utf8') as f :

            data = f.read()
            list = data.split("\n")
            row = []

            for x in list :
                if x != "q" :
                    row.append(x)

                else:
                    self.city.append(row)                   #-------------- city
                    row = []

        with open("./files/txt/street.txt" ,'r' , encoding='utf8') as f :

            for x in f :
                self.street.append(x.replace("\n", ""))     #-------------- street
        

        with open("./files/txt/alley.txt" ,'r' , encoding='utf8') as f :

            for x in f :
                x = x.replace(" ", "")
                self.alley.append(x.replace("\n", ""))     #-------------- alley
        
        self.no = random.randint(0,999)                     #-------------- No.
    
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


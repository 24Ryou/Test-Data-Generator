import random
import array
import rstr
import csv
import pandas as pd

class passwordG :

    def passwordGenerator(self , n) :
            # maximum length of password needed
        # this can be changed to suit your password length

        MAX_LEN = n
        # declare arrays of the character that we need in out password
        # Represented as chars to enable easy string concatenation
        DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                            'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                            'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                            'z']

        UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                            'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                            'Z']

        SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                '*', '(', ')', '<']

        # combines all the character arrays above to form one array
        COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

        # randomly select at least one character from each character set above
        rand_digit = random.choice(DIGITS)
        rand_upper = random.choice(UPCASE_CHARACTERS)
        rand_lower = random.choice(LOCASE_CHARACTERS)
        rand_symbol = random.choice(SYMBOLS)

        # combine the character randomly selected above
        # at this stage, the password contains only 4 characters but
        # we want a 12-character password
        temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol


        # now that we are sure we have at least one character from each
        # set of characters, we fill the rest of
        # the password length by selecting randomly from the combined
        # list of character above.
        for x in range(MAX_LEN - 4):
            temp_pass = temp_pass + random.choice(COMBINED_LIST)

            # convert temporary password into array and shuffle to
            # prevent it from having a consistent pattern
            # where the beginning of the password is predictable
            temp_pass_list = array.array('u', temp_pass)
            random.shuffle(temp_pass_list)

        # traverse the temporary password array and append the chars
        # to form the password
        password = ""
        for x in temp_pass_list:
                password = password + x

        return password

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

class dateG() :

    def __init__(self) -> None:
        pass

    def set(self) :
        self.years = ""
        self.months = ""
        self.days = ""
        self.date = []


    def getdate(self, n) :
        
        dateG.set(self)

        for i in range(n) :
            self.years = str(random.randint(2000,2022))
            self.months = str(random.randint(1,12))
            if (self.months == "2"):
                self.days = str(random.randint(1,28))
            elif(self.months == "4" or self.months == "6" or self.months =="9" or self.months =="11") :
                self.days = str(random.randint(1,30))
            else :
                self.days =str(random.randint(1,31))
            s = self.years + "-" + self.months + "-" + self.days
            self.date.append(s)
        return self.date
        
class csv_list() :

    def getlist(self, path) :
        with open(path , newline='' , encoding='utf') as file :
            data = csv.reader(file , delimiter = ',')
            d = []
            for row in data :
                d.append(row[:])
        return d

    def set2csv(self , path , list2) :
        df = pd.read_csv(path)
        headers = list(df.columns)
        with open(path , 'w' , newline='' , encoding='utf8')  as file :
            thewriter = csv.writer(file)
            list2.insert(0,headers)
            thewriter.writerows(list2)
            
    def getcolumn(self, path, column , colnames) :
        df = pd.read_csv(path ,names = colnames , header=None)
       # head = df.columns
       # print(head)
        saved_column = df[f'{column}']
        return saved_column 

    def getfromtxt(self, path) :
        with open(path, 'r' , encoding='utf8') as f:
            list = []
            for x in f:
                list.append(x[:x.find(":")])
            return list
    def getfromtxtlist(self, path , n) :
        with open(path, 'r' , encoding='utf8') as f:
            list = []
            for x in f:
                list.append(x[:x.find(":")])
            return list[:n]
    
    def csv_header(self , path) :
        df = pd.read_csv(path, header=None)
        return df.columns

    def nestlistdata(self, list) :
        lista = []
        for i in range(len(list)) :
            data = list[i]
            lista.append(data[3])
        return lista
            
class rnd() :

    def phone(self) :
        return "09"+str(random.randint(100000000,999999999))
    def phonelist(self , n) :
        list = []
        for i in range(n) :
            list.append("09"+str(random.randint(100000000,999999999)))
        return list
    
    def age(self) :
        return str(random.randint(18,75))
    def agelist(self , n) :
        list = []
        for i in range(n) :
            list.append(str(random.randint(18,75)))
        return list
    
    def id(self) :
        return str(random.randint(1000000000,9999999999))
    def idlist(self , n) :
        list = []
        for i in range(n) :
            list.append(str(random.randint(1000000000,9999999999)))
        return list
    
    def number(self) :
        return rstr.xeger(r'[0-9]{5,10}')
    def numberlist(self , n) :
        list = []
        for i in range(n) :
            list.append(rstr.xeger(r'[0-9]{5,10}'))
        return list

    def utilitycode(self , n) : # n show what utility id need to generate
        if n == 1 :
            return rstr.xeger(r'[0-9]{1}\d[1]{1}\d[0-9]{3}\d[0-9]{8}')
        elif n == 2 :
            return rstr.xeger(r'[0-9]{1}\d[2]{1}\d[0-9]{3}\d[0-9]{8}')
        else :
            return rstr.xeger(r'[0-9]{1}\d[3]{1}\d[0-9]{3}\d[0-9]{8}')
    def utilitycodelist(self , n , m) : # n show what utility id need to generate ,  m == list length to return
        list = []
        for i in range(m) : 
            if n == 1 :
                list.append(rstr.xeger(r'[0-9]{1}\d[1]{1}\d[0-9]{3}\d[0-9]{8}'))
            elif n == 2 :
                list.append(rstr.xeger(r'[0-9]{1}\d[2]{1}\d[0-9]{3}\d[0-9]{8}'))
            else :
                list.append(rstr.xeger(r'[0-9]{1}\d[3]{1}\d[0-9]{3}\d[0-9]{8}'))
        return list

    def numberrange(self, a , b ,n) : # random from a , b in n number
        list = []
        for i in range(n) : 
            list.append(random.randint(a,b))
        return list

    def chargecost(self):
        return rstr.xeger(r'[1-9]{1}[0]{7}')
    def chargecostlist(self, n):
        list = []
        for i in range(n) : 
            list.append(rstr.xeger(r'[1-9]{1}[0]{7}'))
        return list

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
        
        self.no = "پلاک"+" "+ str(random.randint(0,99))     #-------------- No.
    
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

class txt_list() :

    def set2txt(self, path , list) :
        with open('../files/help.txt' , 'w' , encoding='utf8') as f :
            f.write('\n'.join(list))

""" d = csv_list()
print(type(d.getlist('../files/person.csv')[0]))
print(d.set2csv('../files/p.csv',d.getlist('../files/person.csv')))
colnames = ["Column1" , "Column2" , "Column3" , "Column4" , "Column5" , "Column6" , "Column7"]
print(d.getcolumn('../files/p.csv','Column4', colnames)) """

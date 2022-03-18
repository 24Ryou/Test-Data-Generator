import random
import csv

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



#n = 10
#for i in range(n) :
#    g = random.randint(1,2)
#    if g == 2 :
#       thewriter.writerow([str(random.choice(girls)) , str(random.choice(lname)) , "09"+str(random.randint(100000000,999999999)) , str(random.randint(1000000000,9999999999)) , str(random.randint(18,69)),"2" , "0"])
#    else :
#       thewriter.writerow([str(random.choice(boys)) , str(random.choice(lname)) , "09"+str(random.randint(100000000,999999999)) , str(random.randint(1000000000,9999999999)) , str(random.randint(18,69)) , "1", "0"])

        
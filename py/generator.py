import random
from  tools import *

#               -----------------------------------  instances  ------------------------------  

cl = csv_list()
r = rnd()
a = addressG()
tl = txt_list()

#               -----------------------------------  person section  ------------------------------  
          
boysname = cl.getfromtxt("../files/txt/boys.txt")
girlname = cl.getfromtxt("../files/txt/girls.txt")
lastname = cl.getfromtxt("../files/txt/lastname.txt")
phonenumer = r.phonelist(10) #replace with n
id = r.idlist(10) #replace with n
age = r.agelist(10) #replace with n
accesstype = ["0"]*10 #replace with n
random.shuffle(boysname)
random.shuffle(girlname)
random.shuffle(lastname)
random.shuffle(id)
random.shuffle(age)
personlist = []
for i in range(10) : #replace with n
    data = []
    x = random.randint(1,2)
    if x == 1 : #if a male person select boy name
        data.append(boysname[i]) #for create a row of person.csv
        data.append(lastname[i]) #for create a row of person.csv
        data.append(phonenumer[i]) #for create a row of person.csv
        data.append(id[i]) #for create a row of person.csv
        data.append(age[i]) #for create a row of person.csv
        data.append("1") #for create a row of person.csv
        data.append(accesstype[i]) #for create a row of person.csv
        personlist.append(data) # add row to personlist then send list of lists to set2csv for create csv of it
        #print(data)
    else :
        data.append(girlname[i]) #for create a row of person.csv
        data.append(lastname[i]) #for create a row of person.csv
        data.append(phonenumer[i]) #for create a row of person.csv
        data.append(id[i]) #for create a row of person.csv
        data.append(age[i]) #for create a row of person.csv
        data.append("2") #for create a row of person.csv
        data.append(accesstype[i]) #for create a row of person.csv
        personlist.append(data) # add row to personlist then send list of lists to set2csv for create csv of it
        #print(data)
cl.set2csv('../files/person.csv' , personlist)

#               -----------------------------------  building section  ------------------------------  

building_name = cl.getfromtxt("../files/txt/buildingname.txt")
building_number = r.numberlist(10) #replace with n
building_watercode = r.utilitycodelist(1,10) #replace secon number with n , first numbe show type of utility
building_electrictycode = r.utilitycodelist(2,10) #replace secon number with n , first numbe show type of utility
building_gascode = r.utilitycodelist(3,10) #replace secon number with n , first numbe show type of utility
building_apartment = r.numberrange(10,20,10) #replace with n
building_contract = ["../files/1.pdf"]*10 #replace with n
building_parking = ["../files/txt/parking.txt"]*10 #replace with n
builfing_warehouse = ["../files/txt/warehouse.txt"]*10 #replace with n
building_address = []
building_manager = []
building_phone = []
managerlist = [] # use to store in help.txt for have info of manager ids
random.shuffle(building_name)
for i in range(10) : #replace with n
    string = rstr.xeger(r'[1-9]{1}\d[0-9]{9}')
    managerlist.append("manager id : "+string) #create manager id
    building_manager.append(string) #add created manager id to manage list for add to building.csv
for i in range(10) : #replace with n
    address = a.get()
    phone = str(address[0])+rstr.xeger(r'[0-9]{8}')
    building_phone.append(phone)
    building_address.append("-".join(address[1:]))
buildinglist = []
for i in range(10) : #replace with n 
    data = []
    data.append(building_number[i])
    data.append(building_name[i])
    data.append(building_phone[i])
    data.append(building_watercode[i])
    data.append(building_electrictycode[i])
    data.append(building_gascode[i])
    data.append(building_apartment[i])
    data.append(building_address[i])
    data.append(building_contract[i])
    data.append(building_manager[i])
    data.append(building_parking[i])
    buildinglist.append(data)
cl.set2csv("../files/building.csv",buildinglist)
tl.set2txt('../files/help.txt' , managerlist) #write manager id for backup when generate a building

#               -----------------------------------  apartment section  ------------------------------
#just for 1 building (meanin all person in same building)

buildings = cl.getlist('../files/building.csv') #csv to list ====> make it a nested list(list of lists)
persons = cl.getlist('../files/person.csv')
persons_temp = cl.nestlistdata(persons)
random.shuffle(persons_temp)
people = len(persons_temp)
buildings_temp = buildings[random.randint(0,len(buildings)-1)] #choose a radnom index of building (return a list)
colnames = ['0' , '1' , '2', '3', '4', '5', '6', '7', '8', '9', '10']
col = buildings_temp[6]
aptnumber = []
watercode = buildings_temp[3]
electricitycode = buildings_temp[4]
gascode = buildings_temp[5]
apt_waterode = []
apt_electricitycode = []
apt_gascode = []
apt_owner=persons_temp
apt_type = ""
apt_info = ['../files/txt/aptinfo.txt']*10 #replace with n
apt_charge = r.chargecostlist(10)
aptlist = []
#aptnumber.append(random.randint(1,int(col)))
aptnumber = random.sample(range(int(col)), 10)
for i in range(people) :
    wdata = watercode + "-" + str(aptnumber[i])
    edata = electricitycode + "-" + str(aptnumber[i])
    gdata = gascode + "-" + str(aptnumber[i])
    apt_waterode.append(wdata)
    apt_electricitycode.append(edata)
    apt_gascode.append(gdata)
for i in range(10) : 
    apt_type = str(random.randint(0,1))
    data = []
    data.append(aptnumber[i])
    data.append(apt_waterode[i])
    data.append(apt_electricitycode[i])
    data.append(apt_gascode[i])
    data.append(apt_owner[i])
    data.append(apt_type)
    data.append(apt_info[i])
    data.append(apt_charge[i])
    aptlist.append(data)
cl.set2csv('../files/apartment.csv' , aptlist)

#               -----------------------------------  person section  ------------------------------   



#               -----------------------------------  person section  ------------------------------            
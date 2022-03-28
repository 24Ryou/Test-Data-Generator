import random
import array
import rstr
import csv
import pandas as pd
import os

def passwordGenerator(n) :
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

def getfromtxt(path) :
    with open(path, 'r' , encoding='utf8') as f:
        list = []
        for x in f:
            list.append(x[:x.find(":")])
        return list

def phonelist(n) :
    list = []
    for i in range(n) :
        list.append("09"+str(random.randint(100000000,999999999)))
    return list
    
def agelist(n) :
    list = []
    for i in range(n) :
        list.append(str(random.randint(18,75)))
    return list

def idlist(n) :
    list = []
    for i in range(n) :
        list.append(str(random.randint(1000000000,9999999999)))
    return list

def set2csv(path , list2) :
    df = pd.read_csv(path)
    headers = list(df.columns)
    with open(path , 'w' , newline='' , encoding='utf8')  as file :
        thewriter = csv.writer(file)
        list2.insert(0,headers)
        thewriter.writerows(list2)

def utilitycodelist(n , m) : # n show what utility id need to generate ,  m == list length to return
        list = []
        for i in range(m) : 
            if n == 1 :
                list.append(rstr.xeger(r'[0-9]{1}\d[1]{1}\d[0-9]{3}\d[0-9]{8}'))
            elif n == 2 :
                list.append(rstr.xeger(r'[0-9]{1}\d[2]{1}\d[0-9]{3}\d[0-9]{8}'))
            else :
                list.append(rstr.xeger(r'[0-9]{1}\d[3]{1}\d[0-9]{3}\d[0-9]{8}'))
        return list

def getcolumn(path, column , colnames) : 
        df = pd.read_csv(path ,names = colnames, skiprows=[0] , header=None)
       # head = df.columns
       # print(head)
        saved_column = df[column].tolist()
        return saved_column

def chargecostlist(n): #  n =  number of data in list 
        list = []
        for i in range(n) : 
            list.append(rstr.xeger(r'[1-9]{1}[0]{5,7}'))
        return list     

def date2list(n) :
    
        date = []

        for i in range(n) :
            years = str(random.randint(2000,2021))
            months = str(random.randint(1,12))
            if (months == "2"):
                days = str(random.randint(1,28))
            elif(months == "4" or months == "6" or months =="9" or months =="11") :
                days = str(random.randint(1,30))
            else :
                days =str(random.randint(1,31))
            s = years + "-" + months + "-" + days
            date.append(s)
        return date    
    
def dateextract(list) :
    """return 3 list base on input list extract years list, month list, days list

    Args:
        list (list): list of dates with yyyy-m-d formats
    """   
    years = []
    months = []
    days = []
    for i in list :
        years.append(i.split("-")[0])
        months.append(i.split("-")[1])
        days.append(i.split("-")[2])
    return years,months,days

def fileid(n) :
    """generate list for fileid (file.csv)

    Args:
        n (str): number of file id to generate
    """    
    number = list(range(200))
    rnum = random.sample((number),n)
    return rnum
      
def filespath(path) :
    """return all path of files in a directory into list
    """    
    list = os.listdir(path)
    return list

def filesname(list):
    """return all names of files in directory

    Args:
        path (str): path of directiry to search
    """    
    list2 = []
    for i in list:
        list2.append(i.split(".")[0])
    return list2

def filestype(list) :
    """return all files foramt in directory

    Args:
        path (str): path of dir
    """    
    list2 = []
    for i in list:
        list2.append(i.split(".")[-1])
    return list2
    
def checkAG(path,fieldnames,column1,column2) :
    """return age and gender of person in .csv

    Args:
        path (str): path of .csv
    """  
    ages = getcolumn(path,column1,fieldnames)
    gender = getcolumn(path,column2,fieldnames)
    list = []
    n = len(ages)
    for i in range(n) :   
        data = ""
        if(int(gender[i]) == 2):   #set code for gender-age : 21 = female-youngadult 22 = femaleadult 23 = female-middleage
            data +="2"
            if(int(ages[i]) <=25):
                data += "1"
            elif(25 < int(ages[i]) <50):
                data += "2"
            elif(50<=int(ages[i])):
                data += "3"
        elif(int(gender[i]) == 1) :  #set code for gender-age : 11 = male-youngadult 22 = male-adult 23 = male-middleage
            data+= "1"
            if(int(ages[i]) <=25):
                data += "1"
            elif(25 < int(ages[i]) <50):
                data += "2"
            elif(50<=int(ages[i])):
                data += "3"
        list.append(data)
    return list
        
def getphotoAG(list) :
    """return list of photos path - get list fo checkAG >>> output help to asssing right path to person
    base on their age and gender

    Args:
        list (list[str]): list[index] = code that show what folder search for photo
    """ 
    #['boys-adult', 'boys-middleage', 'boys-youngadult', 'girls-adult', 'girls-middleage-r20', 'girls-youngadult']
    p = os.listdir('../files/img')  
    listfiles = []
    listphoto = []
    listfiles = []
    n = len(list)
    for i in range(n) :
        x = str(list[i])
        path = "../files/img/"
        r20 = random.randint(0,19)
        r30 = random.randint(0,29)
        if(x=="11"):    # boys-youngadult
            listfiles = os.listdir(path)
            path += "/"+listfiles[r30]
            listphoto.append(path)
        if(x=="12"):    # boys-adult
            path += p[0]
            listfiles = os.listdir(path)
            path += "/"+listfiles[r30]
            listphoto.append(path)
        if(x=="13"):    # boys-middleage
            path += p[1]
            listfiles = os.listdir(path)
            path += "/"+listfiles[r30]
            listphoto.append(path)
        if(x=="21"):    # girls-youngadult
            path += p[5]
            listfiles = os.listdir(path)
            path += "/"+listfiles[r30]
            listphoto.append(path)
        if(x=="22"):    # girls-adult
            path += p[3]
            listfiles = os.listdir(path)
            path += "/"+listfiles[r30]
            listphoto.append(path)
        if(x=="23"):    # girls-middleage
            path += p[4]
            listfiles = os.listdir(path)
            path += "/"+listfiles[r20]
            listphoto.append(path)
            
    return listphoto
            
def person(n) : # func that generate number of pepople fo csv base on what is 'n' == how much person 
    
    # extracting the .txt files to list

    boy = getfromtxt("../files/txt/boys.txt")  
    girl = getfromtxt("../files/txt/girls.txt")   
    lastname = getfromtxt("../files/txt/lastname.txt")

    # get list of data base on 'n' == number of person we generating

    # * for have more data so cant be the same value, we need to be uniqe 'id' and 'phone'

    id = idlist(n*2) 
    id = random.sample(id , n)
    phone = phonelist(n*2)
    phone = random.sample(phone , n)

    age = agelist(n)
    access = ["0"]*n # we dont need manager accces generate yet, we add manager manually to system. , 0 == tenant access 1 == manager

    # shuffle lists fo better randomization

    random.shuffle(boy)
    random.shuffle(girl)
    random.shuffle(lastname)
    random.shuffle(phone)
    random.shuffle(id)
    random.shuffle(age)

    # generate final list(list of lists) == rows of csv
    person = []
    for i in range(n) :
        data = []
        x = random.randint(1,2) # select beetween boy or girl name base on their gender
        if x == 2 :
            data.append(girl[i])
            data.append(lastname[i])
            data.append(phone[i])
            data.append(id[i])
            data.append(age[i])
            data.append("2") # set the gender to girl
            data.append(access[i])
        else :
            data.append(boy[i])
            data.append(lastname[i])
            data.append(phone[i])
            data.append(id[i])
            data.append(age[i])
            data.append("1") # set the gender to boy
            data.append(access[i])
        person.append(data) # add a row of person data in list
    set2csv('../files/person.csv', person) # send list to create .csv

def apartment(n) :
    """generate number of apartment base on how much person we have use their id too

    Args:
        n (number of person): help to create apartment detail base on their number
    """    
    num = list(range(1,n+1))    # get list of number from 1 to n*2
    number = random.sample(num, n)  # get sample from that list we created for uniq number lis
    waterid = utilitycodelist(1,n)  # generate water code 1 ==  means for water cus haz uniq number in it.
    electricityid = utilitycodelist(2,n) #  2 ==electricity
    gasid = utilitycodelist(3,n)    # 3 == gas
    fieldnames = ['0','1','2','3','4','5','6']   # genaret number of column of person.csv for geting the owner id from it
    path = '../files/person.csv'
    owner = getcolumn(path,"2",fieldnames)    # get the columns of id for us and rerun as list
    parkingid = random.sample(num , n)
    type = ['0']*n  # 0 = residental , 1 = business
    lorem = ['Minim mollit consectetur ex pariatur sint id qui aute duis quis dolore est ipsum.','Fugiat aute enim laboris cillum adipisicing consequat.',
             'Sint quis reprehenderit proident elit eiusmod.','Aute aliquip tempor enim anim est.','Velit irure nisi deserunt ex consectetur ipsum veniam nostrud excepteur.',
             'Dolor velit adipisicing ut veniam Lorem excepteur laboris minim ullamco.','Minim sit ex aute mollit enim.']
    info =[]
    for i in range(n) :
        info.append(random.choice(lorem))
    
    # generate final list(list of lists) == rows of csv
    apartment = []
    for i in range(n) :
        data = []
        data.append(number[i])
        data.append(waterid[i])
        data.append(electricityid[i])
        data.append(gasid[i])
        data.append(owner[i])
        data.append(parkingid[i])
        data.append(type[i])
        data.append(info[i])
        apartment.append(data)
    set2csv('../files/apartment.csv', apartment) # send list to create .csv
    
def account(n) : 
    """generate csv for account table

    Args:
        n (_type_): number of data to create
    """    
    fieldnames = ['0','1','2','3','4','5','6']   # genaret number of column of person.csv for geting the owner id from it
    path = '../files/person.csv'
    username = getcolumn(path,"2",fieldnames)
    password =[]
    for i in range(n) :
        password.append(passwordGenerator(10)) #     10 =  length of passwrod
    fieldnames.append('7')
    path = "../files/apartment.csv"
    aptnumber = getcolumn(path,'0',fieldnames)
    charge = chargecostlist(n)
    date = date2list(n)
    account = []
    for i in range(n) :
        data = []
        data.append(username[i])
        data.append(password[i])
        data.append(aptnumber[i])
        data.append(charge[i])
        data.append(date[i])
        account.append(data)
    set2csv('../files/account.csv',account)
    
def file (n) :
    """how much file generate

    Args:
        n (_type_): number of files in file table(file.csv)
    """    
    id = fileid(n)
    path = '../files/person.csv'
    fieldsnames = ['0','1','2','3','4','5','6']
    column = '2'
    accountid = getcolumn(path , column , fieldsnames)
    column1 = '4'
    column2 = '5'
    listAG = checkAG(path,fieldsnames,column1,column2)
    #print(listAG)
    pathlist = getphotoAG(listAG)
    listtemp = []
    for i in pathlist :
        listtemp.append(i.split("/")[-1])
    filenames = filesname(listtemp)
    filetypes = filestype(listtemp)
    accpath = '../files/account.csv'
    fields = ['0','1','2','3','4']
    date = getcolumn(accpath,'4',fields)
    file = []
    for i in range(n) :
        data = []
        data.append(id[i])
        data.append(accountid[i])
        data.append(filenames[i])
        data.append(filetypes[i])
        data.append(pathlist[i])
        data.append(date[i])
        file.append(data)
    set2csv("../files/file.csv" , file)
        
def messages(n):
    """generate list of message randomly

    Args:
        n (int,str): show how much data we need to generate
    """ 
    id = fileid(n)   
    path = '../files/txt/message.txt'
    listmessage = getfromtxt(path)
    path2 = '../files/person.csv'
    fieldsnames = ['0','1','2','3','4','5','6']
    column = '2'
    accountid = getcolumn(path2 , column , fieldsnames)
    path3 = '../files/account.csv'
    fieldsnames2 = ['0','1','2','3','4']
    column2 = '4'
    date = getcolumn(path3,column2,fieldsnames2)
    messages = []
    random.shuffle(listmessage)
    for i in range(n) :
        data = []
        data.append(id[i])
        data.append(accountid[i])
        data.append(listmessage[i])
        data.append(date[i])
        messages.append(data)
    set2csv('../files/message.csv',messages)

def transaction(n):
    """generate list of transaction base on transaction table

    Args:
        n (int): jow much data we need
    """    
    
    costlist = chargecostlist(n*n)
    path = '../files/account.csv'
    fieldnames = ['0','1','2','3','4']
    column = '4'
    datelist = getcolumn(path,column,fieldnames)
    a = dateextract(datelist)
    years , months , days = a
    column = '2'
    accountid = getcolumn(path , "0" , fieldnames)
    transaction = []
    id = 0
    day = ['10','11','12','13','14','15','16','17','18','19','20']
    string = ["پرداخت شارژ ساختمان"]
    for i in range(len(years)) :
        y = 2022 - int(years[i])
        m = int(months[i])
        while y != 0 :
            id = id + 1
            if m != 12 :
                m = m+1
                data = []
                data.append(id)
                data.append(accountid[i])
                data.append(random.choice(costlist))
                data.append(string[0])
                data.append(str(2022-y) + "-" + str(m) + "-" + random.choice(day))
                transaction.append(data)
            elif m == 12 :
                y = y-1
                m = 1
                data = []
                data.append(id)
                data.append(accountid[i])
                data.append(random.choice(costlist))
                data.append(string[0])
                data.append(str(2022-y) + "-" + str(m) + "-" + random.choice(day))
                transaction.append(data)
    set2csv('../files/transaction.csv' , transaction)
  
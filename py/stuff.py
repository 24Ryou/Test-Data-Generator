import random
import array
import rstr
import csv
import pandas as pd

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
            list.append(rstr.xeger(r'[1-9]{1}[0]{7}'))
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
import random
import csv

with open("D:\\Ali\\Projects\\Git\\Test-Data-Generator\\boys.txt" , 'r' , encoding='utf8') as f:
    bl =[]
    for x in f:
        bl.append(x[:x.find(":")])
    #print(bl)


with open("D:\\Ali\\Projects\\Git\\Test-Data-Generator\\girls.txt" , 'r' , encoding='utf') as g:
    gl =[]
    for x in g:
        gl.append(x[:x.find(":")])
    #print(gl)

boys = girls = []
boys = bl
girls = gl

with open("D:\\Ali\\Projects\\Git\\Test-Data-Generator\\lastname.txt" , 'r' , encoding='utf') as g:
   ln = g.read().splitlines()

lname = ln
with open('D:\\Ali\\Projects\\Git\\Test-Data-Generator\\person.csv' , 'w' , newline='' , encoding="utf8") as f:
    fieldnames = ['name','lname','phone','id','age','gender','access']
    thewriter = csv.writer(f)


    #thewriter.writeheader()
    #thewriter.writerow(names[i] , lnames[i] , phone[i] , id[i] , age[i] , gender[i], 0 )
    n = 10
    for i in range(n) :
        g = random.randint(1,2)
        if g == 2 :
            thewriter.writerow([str(random.choice(girls)) , str(random.choice(lname)) , "09"+str(random.randint(100000000,999999999)) , str(random.randint(1000000000,9999999999)) , str(random.randint(18,69)),"2" , "0"])
        else :
            thewriter.writerow([str(random.choice(boys)) , str(random.choice(lname)) , "09"+str(random.randint(100000000,999999999)) , str(random.randint(1000000000,9999999999)) , str(random.randint(18,69)) , "1", "0"])
        
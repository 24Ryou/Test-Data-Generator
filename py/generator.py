from stuff import *

# ! set with number you want its generate data base on this number

pn = 20

# ? whatevr csv you need you can use to generate(just un-comment it)

# person(pn)
# apartment(pn)
# account(pn)
# file(pn)
# messages(600)
transaction(pn)
orders(pn)


# print([int(s) for s in str(newdatelist[0]).split() if s.isdigit()])

# new_string = ""+str(newdatelist[0])

# emp_str = ""
# for m in new_string:
#     if m.isdigit():
#         emp_str = emp_str + m
# print("Find numbers from string:",emp_str) 
# # print(b)
# date = date2list(pn)
# a = dateextract(date)
# years, months, days = a
# newdatelist = date2list2persian(years,months,days)
# b = dateextract(newdatelist)

# for i in newdatelist:
#     print(str(i))


# path = r"C:\xampp\htdocs\test-bm\data\users"

# list = getlistOfFolders(path)
# # print(list)
# path_users = []
# for i in list : 
#     # shortpath = r"test-bm\data\users"
#     # fullpath = os.path.join(shortpath,i)
#     fullpath = os.path.join(path,i)
#     # print(fullpath)
#     path_users.append(fullpath)

# # print(path_users[10])

# listfiles = []

# for parent in path_users :
#     temp_list = getListOfFiles(parent)
#     for i in temp_list :
#         listfiles.append(os.path.join(parent,i))

# print(listfiles)
# listfiles[even] = contract.jpg
# listfiles[odd] = profile.jpg

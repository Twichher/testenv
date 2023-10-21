from prettytable import PrettyTable 
from operator import itemgetter
import random
id = 1
id_area = 1
class Employees:    
    #название детали - цена - производитель
    def __init__(self, sname, salary, id_area):
        global id
        self.__id = id
        id += 1
        self.__sname = sname
        self.__salary = salary
        self.__id_area = id_area
    def get_id(self): return(self.__id)
    def get_sname(self): return(self.__sname)
    def get_salary(self): return(self.__salary)
    def get_area(self): return(self.__id_area)

class Area:
    def __init__(self, name):
        global id_area
        self.__id_area = id_area
        id_area += 1
        self.__name = name
    def get_name(self): return(self.__name)
    def get_id_area(self): return(self.__id_area)

class Area_Empl:
    def __init__(self, area_id, own_id):
        self.__area_id = area_id
        self.__own_id = own_id
    def get_ownid(self): return(self.__own_id)
    def get_areaid(self): return(self.__area_id)

snames = []
anames = []
with open("snames.txt", "r") as f:
    for line in f: snames.append(line[:-1])
with open("arnames.txt", "r") as f:
    for line in f: anames.append(line[:-1])
salaries = [random.randint(1000, 20000) for i in range(len(snames))]
emp_lis = [Employees(snames[i], salaries[i], id_area + (i // 5))  for i in range(len(snames))]
area_lis = [Area(anames[i]) for i in range(len(snames) // 5)]
emp_dict = { key:value for key, value in zip([i for i in range(1, id+1)], emp_lis)}
area_dict = {key:value for key,value in zip([i for i in range(1, id_area+1)], area_lis)}
table = PrettyTable()
table.field_names = ["ID детали", "Название", "Цена", "ID производителя"]
for i in emp_dict.keys(): 
    table.add_row([emp_dict[i].get_id(), emp_dict[i].get_sname(), emp_dict[i].get_salary(), emp_dict[i].get_area()])
print(table)
table2 = PrettyTable()
table2.field_names = ["ID детали", "Название производителя"]
for i in area_dict.keys(): 
    table2.add_row([area_dict[i].get_id_area(), area_dict[i].get_name()])
print(table2)
corr_id = 1
arr_corr = []
while (corr_id <= len(area_dict.keys())):
    if area_dict[corr_id].get_name()[0] == "А":
        arr_corr.append(corr_id)
    corr_id += 1
print("###Task 1###")
if len(arr_corr) == 0:
    print("Производителей, начинающихся на А нет")
else:
    print("Производители, начинающиеся на А:")
    for i in arr_corr:
        print(area_dict[i].get_name(), end=' : [\n')
        for g in emp_dict.keys():
            if emp_dict[g].get_area() == i:
                print(f"({emp_dict[g].get_id()} - {emp_dict[g].get_sname()} - {emp_dict[g].get_salary()} - {emp_dict[g].get_area()})")
        print(']')
print("###Task 2###")
max_sal = {}
sal_row = 0
for i in area_dict.keys():
    sal_row = 0
    for g in emp_dict.keys():
        if emp_dict[g].get_area() == i:
            if emp_dict[g].get_salary() > sal_row:
                sal_row = emp_dict[g].get_salary()
    max_sal[i] = sal_row
max_sal_sor = sorted(list(max_sal.items()), key=itemgetter(1), reverse=True)
tablesal = PrettyTable()
tablesal.field_names = ["ID производителя", "Название производителя", "Максимальная цена детали у производителя"]
for i,j  in max_sal_sor:
    #print(f"Максимальная зарплата в отделе {i} ({area_dict[i].get_name()}) = {j}")
    tablesal.add_row([i, area_dict[i].get_name(), j])
print(tablesal)
print("###Task 3###")
rarea = [random.choice(list(area_dict.keys())) for i in range(30)]
remp = [random.choice(list(emp_dict.keys())[:10]) for i in range(30)]
setarem = set([(i, j) for i, j in zip(rarea, remp)])
aremtest = [Area_Empl(i[0], i[1]) for i in setarem]
arem = sorted([(i.get_areaid(), i.get_ownid()) for i in aremtest], key = itemgetter(0))
table3 = PrettyTable()
table3.field_names = ["ID производителя", "ID детали", "Название", "Цена делати"]
for i in arem:
    table3.add_row([i[0], i[1], emp_dict[i[1]].get_sname(), emp_dict[i[1]].get_salary()])
print(table3)
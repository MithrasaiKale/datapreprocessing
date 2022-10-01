import csv
dataset1=[]
dataset2=[]

with open("csv1.csv", "r") as f:
    c=csv.reader(f)
    for i in c:
        dataset1.append(i)

with open("dataset2.csv", "r") as f:
    c=csv.reader(f)
    for i in c:
        dataset2.append(i)

header1=dataset1[0]
planetdata1=dataset1[1:]

header2=dataset2[0]
planetdata2=dataset2[1:]

headers=header1+header2

planetdata=[] 
for index,datarow in enumerate(planetdata1):
    planetdata.append(planetdata1[index]+planetdata2[index])
with open("newplanetdata.csv","a+") as t:
    c=csv.writer(t)
    c.writerow(headers)
    c.writerows(planetdata)
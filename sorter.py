import csv
data=[]
with open("csv2.csv", "r") as f:
    c=csv.reader(f)
    for i in c:
        data.append(i)
        
headers=data[0]
planetdata=data[1:]

for a in planetdata:
    a[2]=a[2].lower()
    
planetdata.sort(key=lambda planetdata:planetdata[2])
with open("dataset2.csv", "a+") as f:
    c=csv.writer(f)
    c.writerow(headers)
    c.writerows(planetdata)
    
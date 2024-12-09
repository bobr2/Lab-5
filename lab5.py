import re
import pandas as pd


#Задание1
otvet = []
with open("task1-en.txt", "r") as f:

    for string in f.readlines():
        res = re.findall(r"\bc\w+\b|the \b\w+\b", string)
        otvet.append(res)
otvet = [x for x in otvet if x != []]
#print(otvet)

#Задание 2

with open("task2.html", "r", encoding="utf-8") as f:
    cont = f.read()
    f.close()

reg_string = r'font-family:.([^;]+);'
otvet = re.findall(reg_string, cont)
#print(otvet)

#задание 3
with open("task3.txt", "r", encoding="utf-8") as f:
    table = f.read()
    f.close()
real_table = pd.DataFrame({"id": ["me"], "surname" : ["me"], "email" : ["me"], "data" : ["me"], "website" : ["me"]})

data_id = re.findall(r'\S+', table)


datates = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', table)
for x in datates:
    table = table.replace(x, "")

emails = re.findall(r'[A-Za-z][A-Za-z0-9._%+-]*@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', table)

for x in emails:
    table = table.replace(x, "")


sites = re.findall(r'(?:https?:\/\/|:\/\/)[\w\-\.]+(?:\.[a-z]{2,})(?:\/[^\s]*)*\/', table)

for x in sites:
    table = table.replace(x, "")

surnames = re.findall( r'[A-Z][a-z]+', table)

for x in surnames:
    table = table.replace(x, "")



for n in range(0, min(len(datates), len(datates), len(emails), len(sites))):

    real_table.loc[n] = [n, surnames[n], emails[n], datates[n], sites[n]]

print(real_table)

real_table.to_csv('output.csv', index=False)

    
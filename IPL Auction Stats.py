import pandas
import requests
from bs4 import BeautifulSoup
url="https://www.iplt20.com/auction/2022"
r=requests.get(url)
soup=BeautifulSoup(r.text,"lxml")
a=soup.find("table")
b=a.findAll("th")
headers=[]
for i in b:
    A=i.text
    headers.append(A)
df=pandas.DataFrame(columns=headers)
c=a.findAll("tr")
for i in c[1:]:
    row=i.findAll("td")
    rows=[j.text.strip() for j in row]
    l=len(df)
    df.loc[l]=rows
df.to_csv("IPL Auction Stats.csv")
print(df)




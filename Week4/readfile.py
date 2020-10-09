from bs4 import BeautifulSoup

with open("../labs/carviewer2.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

#print(soup.prettify())
#print(soup.tr)
rows = soup.findAll("tr")
for row in rows:
    #print("-------")
    #print(row)
    dataList=[]
    cols = row.findAll("th")
    for col in cols:
        dataList.append(col.text)
    print(dataList)
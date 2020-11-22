import requests
import json
from xlwt import *

url = "https://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20and%20Imbalance%20Market%20Cost%20View&Date=>2020-11-18"
response = requests.get(url)
data = response.json()

listOfReports = []
#output to console
#print(data)
#add each ResourceName in the JSON to a list.
for item in data["items"]:
    #print(item["ResourceName"])
    listOfReports.append(item["ResourceName"])

#Create .xls and give it headings
w = Workbook()
ws = w.add_sheet('cars')
rowNumber = 0;
ws.write(rowNumber,0,"StartTime")
ws.write(rowNumber,1,"EndTime")
ws.write(rowNumber,2,"ImbalanceVolume")
ws.write(rowNumber,3,"ImbalancePrice")
ws.write(rowNumber,4,"ImbalanceCost")
rowNumber +=1

#for item in ResourceName list...
for ReportName in listOfReports:
    #print(ReportName)
    url = "https://reports.sem-o.com/api/v1/documents/"+ReportName #loop through the urls
    #print(url)
    response = requests.get(url)
    aReport = response.json()
    #getting the ImbalancePrice value from the row array of each report file/url.
    #writing them to the .xls
    for row in aReport["rows"]:
        #print(row["ImbalancePrice"])


        ws.write(rowNumber,0,row["StartTime"])
        ws.write(rowNumber,1,row["EndTime"])
        ws.write(rowNumber,2,row["ImbalanceVolume"])
        ws.write(rowNumber,3,row["ImbalancePrice"])
        ws.write(rowNumber,4,row["ImbalanceCost"])
        rowNumber +=1

w.save("balance.xls")


#other code
#save to a file
filename = "allreports.json"
#writing JSON data
f = open(filename, 'w')
json.dump(data, f, indent=4)
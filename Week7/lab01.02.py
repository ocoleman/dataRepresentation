#Dealing with multiple pages
import requests
import json
from xlwt import *

url = "https://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20and%20Imbalance%20Market%20Cost%20View"
response = requests.get(url)
data = response.json()
totalPages = data["pagination"]["totalPages"]
#print(totalPages)
listOfReports = []

pageNumber = 1
while pageNumber <= totalPages:
    pageUrl = url + "&page="+ str(pageNumber) #adds "&page=1,2,3etc" to the end of the url
    #print(pageUrl)
    data = requests.get(pageUrl).json()
    for item in data["items"]:
        #add each ResourceName in the JSON to a list.
        listOfReports.append(item["ResourceName"])

    pageNumber +=1


#output to console
#print(data)
for ReportName in listOfReports:
    print(ReportName)




#other code
#save to a file
filename = "allreports.json"
#writing JSON data
f = open(filename, 'w')
json.dump(data, f, indent=4)
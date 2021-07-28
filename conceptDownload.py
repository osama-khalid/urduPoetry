#

#Get wordList
import csv
import requests
import time
import pickle
conceptList=[]
file=open('concepts.csv','r').read().split('\n')
for f in file:
    if len(f)>0:
        conceptList.append(f)

conceptMap={}
x=0
for f in conceptList:
    x=x+1
    if x%10==0:
        print(f)
    #f=conceptList[3]
    while(1):
        url='http://ukc.datascientia.eu/api/ukc/concepts?conceptId='+f
        try:
            statuscode=404
            while(statuscode!=200):
                req=requests.get(url,timeout=10)
                statuscode=req.status_code
                if statuscode!=200:
                    time.sleep(10)


            break
        except:
            print(f)
            time.sleep(5)
    time.sleep(1.1)            
    conceptMap[f]=req.json()['name']

file_to_store = open("conceptMaps.pickle", "wb")
pickle.dump(conceptMap, file_to_store)      


with open('Fruits.obj', 'wb') as fp:
    pickle.dump(conceptMap, fp)

with open('Fruits.obj', 'rb') as fp:
    banana = pickle.load(fp)    
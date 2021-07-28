





import threading        # For the Parallelization 


import csv
import requests
import time


def getWord(I,a): 
    nones=[]
    R=[]
    I=int(I)
    done=[]

    with open('dictionary_'+str(I)+'.csv',mode='w',encoding='utf-8') as urduDic:
        foodWrite=csv.writer(urduDic,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        x=0
        with open('LookUpNew.csv', 'r',encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
            for row in csv_reader:
                if len(row)>0:

                    if x%10==I:
                        if row[1] not in R and row[1] not in done:
                            R.append(row[1])
                            data={'Word': row[1],'UserId':'','websiteId': '1','SelectedWord': row[0]}
                            header={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Sec-Fetch-Site": "same-origin","Sec-Fetch-Mode": "navigate","Sec-Fetch-User": "?1","Sec-Fetch-Dest": "document"}
                            url='https://world.rekhta.org/api/v2/shayari/GetWordMeaning?lang=1'
                            #url='https://rekhta.org/nazms/shikva-kyuun-zayaan-kaar-banuun-suud-faraamosh-rahuun-allama-iqbal-nazms'
                            while(1):
                                try:
                                    urlOpen = requests.post(url,headers=header,data=data, allow_redirects=False, timeout=10).json()
                                    r=urlOpen['R']

                                    
                                    if r['U'] is not None:
                                        print([r['E'],r['U'],r['H'],r['M1E'],r['WS'],row[1]])
                                        foodWrite.writerow([r['E'],r['U'],r['H'],r['M1E'],r['WS'],row[1]])
                                    else:
                                        nones.append(row[0])
                                        #print(row[0])
                                    break
                                except:
                                    time.sleep(1)
                                    #print(row[1])
                    x=x+1


    file=open('notFound_'+str(I)+'.csv','w')
    file.write('\n'.join(nones))
a=' '

t1 = threading.Thread(target=getWord,args=('0',a))
t1.daemon =True
t1.start()
t2 = threading.Thread(target=getWord,args=('1',a))
t2.daemon =True
t2.start()


t3 = threading.Thread(target=getWord,args=('2',a))
t3.daemon =True
t3.start()
t4 = threading.Thread(target=getWord,args=('3',a))
t4.daemon =True
t4.start()

t5 = threading.Thread(target=getWord,args=('4',a))
t5.daemon =True
t5.start()
t6 = threading.Thread(target=getWord,args=('5',a))
t6.daemon =True
t6.start()


t7 = threading.Thread(target=getWord,args=('6',a))
t7.daemon =True
t7.start()
t8 = threading.Thread(target=getWord,args=('7',a))
t8.daemon =True
t8.start()

t9 = threading.Thread(target=getWord,args=('8',a))
t9.daemon =True
t9.start()
t10 = threading.Thread(target=getWord,args=('9',a))
t10.daemon =True
t10.start()


a = t1.join()
a= t2.join()
a = t3.join()
a = t4.join()
a = t5.join()
a = t6.join()
a = t7.join()
a = t8.join()
a = t9.join()
a = t10.join()

    
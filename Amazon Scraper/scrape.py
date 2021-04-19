import csv
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
def scraper():
    f=open('amazon.csv','w',newline='')
    data=csv.writer(f)
    headers = (
        {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Accept-language': 'en-US,en;q=0.5'
        }      )
    main=[]
    preq=requests.get(url_name,headers)
    soup=BeautifulSoup(preq.content,features="html.parser")
    product_author_name=[i.text for i in soup.findAll("span",{"class":"a-size-small a-color-base"})]
    data.writerow(product_author_name)
    main.append(product_author_name)
    product_rating=[ratings.text for ratings in soup.findAll("a",{"class":"a-size-small a-link-normal"})]
    data.writerow(product_rating)
    main.append(product_rating)
    df=pd.DataFrame(data=main)
    df.to_excel('amazon_report.xlsx',index=False,header=False)
    print('Done')
    time.sleep(times)
if __name__ == '__main__':
    t=int(input("Enter the time in second you want the scraper to work for the upadtion purpose:- "))
    times=int(input("Enter the time you want to hold the scraper : "))
    url_name = input('Enter the link: ')
    end_time=time.time() + t
    while time.time() < end_time:
        scraper()

from bs4 import BeautifulSoup
import requests
from requests import Request, Session
import lxml
import os

s = requests.Session()
f_read = open(os.path.abspath('just/court_2610/text.txt'), 'r', encoding = 'utf-8')
last_number = f_read.read().split('\n')[-2].split(';')[0].split('/')[-3]
URL = "http://court.gov.ua/logs.php"
URL_number = int(last_number)


def court_2610(URL_number):
    URL_court = "http://court.gov.ua/log_documents/%s/2610/" % URL_number
    inspector = s.get(URL_court)
    inspector_soup = BeautifulSoup(inspector.content, 'lxml')
    DID = inspector_soup.find(id='did').next_element.split('_')[0]
    if DID != u'0':
        f = open(os.path.abspath('just/court_2610/text.txt'), 'a+', encoding = 'utf-8')
        headers = {
        "Host" : "court.gov.ua",
        "Connection" : "keep-alive",
        "Content-Length" : "35",
        "Accept" : "text/plain, */*; q=0.01",
        "Origin" : "http://court.gov.ua",
        "X-Requested-With" : "XMLHttpRequest",
        "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer" : URL_court,
        "Accept-Encoding" : "gzip, deflate",
        "Accept-Language" : "en-US,en;q=0.8,ru;q=0.6,uk;q=0.4",
        "Cookie" : "PHPSESSID=erl2dvg4g4jiksova3bqtfoao6"}
        data = {"doc_ver" : "54_2",
        "did" : DID,
        "ddid" : "2610"}
        req = Request('POST', URL, data=data, headers=headers)
        prepped = req.prepare()
        page = s.send(prepped)
        soup = BeautifulSoup(page.content, 'lxml')
        find_soup = soup.find('p').string.replace('\r',';').replace('I: ','').split('\n')
        f.write(URL_court)
        f.write(';')
        for index in find_soup[1:5]:
            f.write(index)
        f.write('\n')
        f.close()
    print(URL_number)

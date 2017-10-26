import os
import threading
from queue import Queue
from bs4 import BeautifulSoup
import requests
from requests import Request, Session

s = requests.Session()
f_read = open(os.path.abspath('uploads/text.txt'), 'r', encoding = 'utf-8')
last_number = f_read.read().split('\n')[-2].split(';')[0].split('/')[-3]
url_logs = "http://court.gov.ua/logs.php"

class Downloader(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        while True:
            # Получаем url из очереди
            url = self.queue.get()
            # Скачиваем файл
            self.court_2610(url)
            # Отправляем сигнал о том, что задача завершена
            self.queue.task_done()
    def court_2610(self, url):
        inspector = s.get(url)
        inspector_soup = BeautifulSoup(inspector.content, 'lxml')
        try:
            DID = inspector_soup.find(id='did').next_element.split('_')[0]
            if DID != u'0':
                headers = {
                "Host" : "court.gov.ua",
                "Connection" : "keep-alive",
                "Content-Length" : "35",
                "Accept" : "text/plain, */*; q=0.01",
                "Origin" : "http://court.gov.ua",
                "X-Requested-With" : "XMLHttpRequest",
                "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
                "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
                "Referer" : url,
                "Accept-Encoding" : "gzip, deflate",
                "Accept-Language" : "en-US,en;q=0.8,ru;q=0.6,uk;q=0.4",
                "Cookie" : "PHPSESSID=erl2dvg4g4jiksova3bqtfoao6"}
                data = {"doc_ver" : "54_2",
                "did" : DID,
                "ddid" : "2610"}
                req = Request('POST', url_logs, data=data, headers=headers)
                prepped = req.prepare()
                page = s.send(prepped)
                soup = BeautifulSoup(page.content, 'lxml')
                try:
                    find_soup = soup.find('p').string.replace('\r',';').replace('I: ','').split('\n')
                    f = open(os.path.abspath('uploads/text.txt'), 'a+', encoding = 'utf-8')
                    f.write(url)
                    f.write(';')
                    for index in find_soup[1:5]:
                        f.write(index)
                    f.write('\n')
                    f.close()
                    print('niceeeeeeeeeeeeeeeeeee%s'% url)
                except:
                    print('_________________________________________________________%s '% url)
        except (AttributeError, NameError):
            print('FUCK' + url)
        print(url)

def main(urls):
    queue = Queue()
    # Запускаем потом и очередь
    for i in range(300):
        t = Downloader(queue)
        t.setDaemon(True)
        t.start()
    # Даем очереди нужные нам ссылки для скачивания
    for url in urls:
        queue.put(url)
    # Ждем завершения работы очереди
    queue.join()

if __name__ == "__main__":
    urls = []
    for links in list(range(int(last_number)+1, int(last_number)+1000000)):
        urls.append('http://court.gov.ua/log_documents/%s/2610/'% links)
    main(urls)

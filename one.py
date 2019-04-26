import os
import requests
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        r = requests.get(url)
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("解析过程出错")

def AnyansisHTML(html):
    try:
        soup = BeautifulSoup(html,'html.parser')
        string = soup.select('[itemprop]')[0].get('content')
        with open('one.txt','a') as f:
            f.write(string+'\n')
            f.close()
    except:
        print("获取文字过程报错")

def getimage(html,i):
    try:
        soup = BeautifulSoup(html,'html.parser')
        image_url = soup.find_all(class_ = 'one-imagen')[0].img.get('src')
        r = requests.get(image_url)
        root = '/Users/liuchenwei/gitlearning_/img/'
        path = root+str(i)+'.jpg'
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
    except:
        print("下载图片过程出错")


if __name__ == "__main__":
    start_url = 'http://wufazhuce.com/one/'
    j = '0014'
    i=0
    while(j!='2424'):
        url = start_url + j
        j = str(int(j)+1)
        html = getHTMLText(url)
        AnyansisHTML(html)
        getimage(html,i)
        i+=1
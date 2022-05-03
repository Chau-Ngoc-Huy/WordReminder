import requests
import lxml
from bs4 import BeautifulSoup 

def getText(str):
    open = []
    close = []
    i = 0
    while(i < len(str)):
        if str[i] == '<':
            j =  i + 1
            while(str[j] != '>'):
                j = j + 1
            str = str[:i] + str[j+1:]
            i = i - 1
        i = i + 1
    t = str[0]
    while(t == ' '):
        str = str[1:]
        t = str[0]
    return str
def getListText(list):
    result = []
    for i in list:
        result.append(getText(str(i)))
    return result
def translate(vocabulary):

    # vocabulary = input('Enter some word: ')

    url = "https://www.ldoceonline.com/dictionary/" + vocabulary
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }
    f = requests.get(url, headers = headers)
    soup = BeautifulSoup(f.content,'lxml')
    definationHTML = soup.findAll('span', {'class': 'DEF'})
    defination = getListText(definationHTML)
    if (defination == []):
        return ['this word does not exist']
    return defination